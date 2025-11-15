# 🌦 Weather App (Python CLI)

A simple and clean **Python command-line Weather Application** that fetches real-time weather data using the OpenWeather REST API.  
This project demonstrates practical skills such as HTTP requests, JSON parsing, error handling, and user interaction in a CLI environment.

---

## 🚀 Project Overview

This application allows you to:

- Search weather by city name  
- View temperature, humidity, feels-like temperature, and description  
- Get real-time weather data from OpenWeather API  
- Handle errors such as invalid API key, city not found, and network issues  

The API key is hardcoded in the script for simplicity.

---

## 🧠 Key Features

- REST API consumption using `requests`
- JSON response parsing
- Proper error handling (401, 404, timeout, network errors)
- Clean and modular function design
- Interactive CLI interface
- Beginner-friendly real-world API integration project

---

## 📁 Project Structure

```
weather-app/
│
├── README.md
└── src/
    └── main.py
```

---

## ▶️ Running the Project

Inside the project folder:

```
python src/main.py
```

Before running, make sure you updated this line inside `main.py`:

```
API_KEY = "YOUR_API_KEY_HERE"
```

Replace it with your real OpenWeather API key.

---

## 🧰 Tech Stack

- Python 3.x  
- Requests library (must be installed):  
```
pip install requests
```

---

## 👨‍💻 Author

**Berke Arda Türk**  
Data Science & AI Enthusiast | Computer Science (B.ASc)  
[🌐 Portfolio Website](https://berke-turk.web.app/) • [💼 LinkedIn](https://www.linkedin.com/in/berke-arda-turk/) • [🐙 GitHub](https://github.com/Mood07)
