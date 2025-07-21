# Python Learning & Mini-Projects Collection

This repository contains a variety of Python scripts, Jupyter notebooks, and mini-projects designed to help you learn and practice Python programming. The collection covers basic syntax, data structures, OOP, file handling, exception handling, API usage, and a Flask-based weather web app with WhatsApp integration.

## Table of Contents

- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Key Components](#key-components)
- [Flask Weather + WhatsApp App](#flask-weather--whatsapp-app)
- [Requirements](#requirements)
- [License](#license)

---

## Getting Started

Clone this repository and explore the various scripts and notebooks. Each folder focuses on a different aspect of Python programming.

## Project Structure

```
python/
  ├── day1.ipynb, day2.py, day3.ipynb, graph.ipynb
  ├── python-/
      ├── basic/           # Basic data structures and syntax
      ├── functions/       # Function examples and modules
      ├── filehandling/    # File handling scripts and examples
      ├── loop/            # Looping constructs and examples
      ├── oops/            # Object-Oriented Programming basics
      ├── practise/        # Practice scripts (e.g., weather API)
      ├── csv.csv/         # CSV and Excel file samples
      ├── flask_weather+whatsapp/  # Flask app for weather + WhatsApp
      ├── age_calculater.py, age_oops.py, excpetion.py, while.py, python.md
```

## Key Components

### Basic Python (`basic/`)
- **list.py, set.py, tuples.py, dic.py, DIC1.PY, syntex-python.py**: Scripts demonstrating lists, sets, tuples, dictionaries, and basic Python syntax.

### Functions (`functions/`)
- **fun1.py, app.py, mymodule.py**: Examples of defining and using functions, modules, and mathematical operations.

### File Handling (`filehandling/`)
- **fh1.py, modul.py, text.txt, image.png**: Scripts for reading/writing files and handling different file types.

### Loops (`loop/`, `while.py`)
- **atm.py, loop1.py, loop2.py, loop3.py, while.py**: Examples of for-loops, while-loops, and control flow.

### OOP (`oops/`)
- **basicsOfOops.py**: Introduction to classes and objects in Python.

### Practice (`practise/`)
- **wetherapi.py**: Script to fetch weather data using the AccuWeather API.
- **questions.py**: Placeholder for practice questions.

### Exception Handling
- **excpetion.py**: Basic try-except example.

### Age Calculator
- **age_calculater.py, age_oops.py**: Calculate age and related statistics using input birth year.

## Flask Weather + WhatsApp App

Located in `python-/flask_weather+whatsapp/flask_weather+whatsapp/`:

- **app.py**: Flask web app to fetch and display weather for a city using AccuWeather API. Allows downloading the weather report as a PDF.
- **whatsapp.py**: Script to send WhatsApp messages using `pywhatkit`.
- **templates/index.html**: HTML template for the Flask app.
- **requirements.txt**: Dependencies for the Flask app.
- **dehradun_weather.pdf, Vadodara_weather.pdf**: Example weather reports.

### How to Run the Flask App

1. Install dependencies:
   ```
   pip install Flask requests fpdf
   ```
2. Run the app:
   ```
   python app.py
   ```
3. Open your browser at `http://127.0.0.1:5000/` and enter a city name to get the weather.

## Requirements

- Python 3.x
- See `requirements.txt` in the Flask app folder for web app dependencies.

## License

This project is for educational purposes. 