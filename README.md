# 🍽️ GNOMES Restaurant Recommender

A web-based restaurant recommendation system designed to help users discover great places to eat in Dallas, Texas.

This project was developed by the GNOMES team as part of a collaborative application development project using GitHub, Flask, HTML/CSS, JavaScript, and a structured CSV dataset.

---

## 📌 Project Overview

The GNOMES Restaurant Recommender is an interactive web application that helps users decide where to eat in Dallas. Users can select optional preferences for cuisine, price range, and dietary needs. The app then filters a restaurant dataset and uses a fun jackpot-style spinner to randomly recommend a matching restaurant.

---

## 🚀 Features

- 🔍 Filter restaurants by cuisine, price, and dietary preference
- 🎰 Interactive jackpot-style restaurant spinner
- 📊 Uses a structured dataset stored in `restaurants.csv`
- 🌐 Web interface built with HTML, CSS, and JavaScript
- ⚡ Flask backend with JSON endpoint for filtered restaurant options
- 🧩 Designed for team collaboration using GitHub

---

## 🛠️ Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- CSV dataset
- GitHub Codespaces
- GitHub for collaboration and version control

---

## 📂 Project Structure

```text
gnomes-restaurant-recommender/
│
├── app.py                  # Main Flask application logic
├── restaurants.csv         # Dallas restaurant dataset
├── requirements.txt        # Project dependencies
├── templates/              # HTML templates
│   ├── index.html
│   └── results.html
├── .gitignore
└── README.md
```

---

## ⚙️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/your-username/gnomes-restaurant-recommender.git
```

### 2. Navigate into the project folder

```bash
cd gnomes-restaurant-recommender
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

### 5. Open your browser and go to

```text
http://127.0.0.1:5001/
```

---

## 🎰 How It Works

1. The user selects optional filters for cuisine, price, and dietary preference.
2. Flask reads restaurant data from `restaurants.csv`.
3. The `/spin-options` endpoint filters restaurants based on selected preferences.
4. Matching restaurants are returned to the frontend.
5. The jackpot spinner randomly selects one restaurant from the filtered list.
6. The selected restaurant is displayed with details including cuisine, price, dietary tags, and description.

---

## 🤝 Team Collaboration

This project was built collaboratively using GitHub. Team members contributed to different areas including:

- Backend logic
- Frontend design
- Dataset preparation
- Recommendation/filtering logic
- Documentation
- Testing and debugging

---

## 📍 Future Improvements

- Add restaurant ratings
- Add neighborhood/location filtering
- Improve recommendation scoring
- Add restaurant images
- Add links to restaurant websites
- Deploy the application online
- Add saved favorites or user history

---

## 📄 License

This project was created for educational purposes.