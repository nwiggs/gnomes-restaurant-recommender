from flask import Flask, render_template, request, jsonify
import csv
import random

app = Flask(__name__)

def load_restaurants():
    """Load restaurants from CSV and process dietary tags."""
    restaurants = []
    try:
        with open("restaurants.csv", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row["dietary_tags"] = [tag.strip().lower() for tag in row["dietary_tags"].split(",") if tag.strip()]
                restaurants.append(row)
    except FileNotFoundError:
        print("CSV file not found yet.")
    return restaurants

def get_filter_options(restaurants):
    """Extract unique cuisines, prices, and dietary options from restaurants."""
    cuisines = set()
    prices = set()
    dietary = set()
    
    for r in restaurants:
        if r.get("cuisine"):
            cuisines.add(r["cuisine"])
        if r.get("price"):
            prices.add(r["price"])
        dietary.update(r.get("dietary_tags", []))
    
    return {
        "cuisines": sorted(list(cuisines)),
        "prices": sorted(list(prices)),
        "dietary": sorted(list(dietary))
    }

def filter_restaurants(restaurants, cuisine, price, dietary):
    """Filter restaurants based on cuisine, price, and dietary criteria."""
    filtered = []
    
    for r in restaurants:
        # Handle cuisine filter (case-insensitive, treat "Any" as match-all)
        cuisine_lower = cuisine.lower() if cuisine else "any"
        match_cuisine = (cuisine_lower == "any" or 
                        r.get("cuisine", "").lower() == cuisine_lower)
        
        # Handle price filter (case-sensitive)
        match_price = (price.lower() == "any" or 
                      r.get("price", "") == price)
        
        # Handle dietary filter (case-insensitive, treat "Any" as match-all)
        dietary_lower = dietary.lower() if dietary else "any"
        match_dietary = (dietary_lower == "any" or 
                        dietary_lower in r.get("dietary_tags", []))
        
        if match_cuisine and match_price and match_dietary:
            filtered.append(r)
    
    return filtered

@app.route("/")
def home():
    restaurants = load_restaurants()
    options = get_filter_options(restaurants)
    return render_template("index.html", options=options, restaurants=restaurants)

@app.route("/spin-options", methods=["POST"])
def spin_options():
    """API endpoint for getting filtered restaurant options via AJAX."""
    data = request.get_json()
    
    cuisine = data.get("cuisine", "Any")
    price = data.get("price", "Any")
    dietary = data.get("dietary", "Any")
    
    # Load all restaurants
    restaurants = load_restaurants()
    
    # Filter based on criteria
    filtered = filter_restaurants(restaurants, cuisine, price, dietary)
    
    # If no results with current filters, return message
    if not filtered:
        return jsonify({
            "ok": False,
            "message": "No restaurants match your filters. Try adjusting them!",
            "restaurants": []
        })
    
    # Prepare response message
    filter_info = []
    if cuisine.lower() != "any":
        filter_info.append(cuisine)
    if price.lower() != "any":
        filter_info.append(f"${price.count('$')}" if price.startswith("$") else price)
    if dietary.lower() != "any":
        filter_info.append(dietary.capitalize())
    
    message = f"Found {len(filtered)} restaurant{'s' if len(filtered) != 1 else ''}"
    if filter_info:
        message += f" ({', '.join(filter_info)})"
    message += ". Ready to spin!"
    
    return jsonify({
        "ok": True,
        "message": message,
        "restaurants": filtered
    })

@app.route("/recommend", methods=["POST"])
def recommend():
    """Legacy endpoint for form-based recommendations."""
    cuisine = request.form.get("cuisine", "Any")
    price = request.form.get("price", "Any")
    dietary = request.form.get("dietary", "Any").strip().lower()

    restaurants = load_restaurants()
    filtered = filter_restaurants(restaurants, cuisine, price, dietary)

    return render_template("results.html", recommendations=filtered)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
