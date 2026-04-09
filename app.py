from flask import Flask, render_template, request
import csv

app = Flask(__name__)

def load_restaurants():
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

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    cuisine = request.form.get("cuisine", "any").strip().lower()
    price   = request.form.get("price", "any").strip().lower()
    dietary = request.form.get("dietary", "any").strip().lower()

    restaurants = load_restaurants()
    
    filtered = []
    for r in restaurants:
        match_cuisine = cuisine == "any" or r["cuisine"].lower() == cuisine
        match_price   = price == "any"   or r["price"].lower() == price
        match_dietary = dietary == "any" or dietary in r["dietary_tags"]

        if match_cuisine and match_price and match_dietary:
            filtered.append(r)

    return render_template("results.html", recommendations=filtered)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
