# BMI Health Tracker

A desktop-based Body Mass Index (BMI) Calculator developed using Python, Tkinter, SQLite, and Matplotlib. The application allows users to calculate BMI, categorize results, store measurements, track BMI history, visualize trends, and export records.

## 📌 Project Overview

The BMI Health Tracker provides a simple and user-friendly desktop interface for calculating and managing BMI measurements.

The application combines:

- Python — Application logic
- Tkinter — Graphical user interface
- SQLite — Local database storage
- Matplotlib — BMI trend visualization
- CSV — Measurement data export

## ✨ Features

- 🧮 Calculate BMI using weight and height
- 📊 Display BMI value and corresponding category
- 👤 Store BMI records for multiple users
- 💾 Save measurements in a local SQLite database
- 🔎 Search and browse BMI history by user
- 📈 Visualize BMI trends using graphs
- 📏 Display BMI reference thresholds on graphs
- 📄 Export BMI history to CSV
- ⚠️ Validate user input and display appropriate error messages
- 🕒 Automatically record the date and time of each measurement
- 🎨 Colour-coded BMI results

## 🧮 BMI Calculation

The application calculates BMI using the standard formula:

BMI = Weight (kg) / Height² (m)

### BMI Categories

| BMI Range | Category |
|---|---|
| Below 18.5 | Underweight |
| 18.5 – 24.9 | Normal |
| 25.0 – 29.9 | Overweight |
| 30.0 and above | Obese |

> Note: BMI is a general screening measure and does not account for factors such as muscle mass, body composition, age, or individual health conditions.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core application development |
| Tkinter | Desktop graphical user interface |
| SQLite | Local database management |
| Matplotlib | BMI trend visualization |
| CSV | Data export |

## 📋 Requirements

- Python 3.x
- Tkinter
- Matplotlib

Tkinter and SQLite are generally included with standard Python installations.

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Jisan0178/OIBSIP_Python_Task2.git
