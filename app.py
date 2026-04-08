from flask import Flask, render_template, request
import csv

app = Flask(__name__)

def load_restaurants():
    restaurants = []
    try:
        with open("restaurants.csv", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row["dietary_tags"] = [tag.strip().lower() for tag in row["dietary_tags"].split(",")]
                restaurants.append(row)
    except FileNotFoundError:
        print("CSV file not found yet.")
    return restaurants

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    cuisine = request.form.get("cuisine")
    price = request.form.get("price")
    dietary = request.form.get("dietary")

    restaurants = load_restaurants()
    
    # TEMP: just return empty results for now
    return render_template("results.html", recommendations=[])

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
