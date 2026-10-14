# ⚖️ BMI Health Tracker

> A Python-based desktop application for calculating Body Mass Index (BMI), managing user measurements, tracking BMI history, visualizing trends, and exporting records to CSV.

---

## 📌 Project Overview

The **BMI Health Tracker** is a desktop-based BMI calculator developed using Python, Tkinter, SQLite, and Matplotlib. It provides a user-friendly graphical interface to calculate BMI, identify BMI categories, save measurements, review previous records, and visualize changes over time.

This project was developed as part of my **Python Programming Internship at Oasis Infobyte (OIBSIP)**.

### ✨ Key Highlights

- 🧮 Calculate BMI using height and weight.
- 🎨 Display BMI values with colour-coded categories.
- 👤 Maintain records for multiple users.
- 💾 Store measurements in a local SQLite database.
- 🔎 Search and browse BMI history.
- 📈 Visualize BMI trends using graphs.
- 📏 Display BMI reference thresholds on graphs.
- 📄 Export measurement records to CSV.
- ⚠️ Validate user input and display error messages.
- 🕒 Record the date and time of measurements.

---

## ✨ Features

### 🧮 BMI Calculation
- Calculates BMI using weight in kilograms and height in metres.
- Displays the calculated BMI value.
- Identifies the corresponding BMI category.
- Uses colour-coded results for easier interpretation.

### 👤 User Management and Records
- Supports recording measurements for multiple users.
- Saves each measurement with the user's name.
- Stores weight, height, BMI, category, and timestamp.
- Maintains records locally using SQLite.

### 🔎 BMI History
- Browse previously saved measurements.
- Search and review records by user name.
- View historical BMI values and categories.
- Check the date and time of each measurement.

### 📈 BMI Trend Visualization
- Visualizes a user's BMI measurements over time.
- Displays recorded BMI values on a graph.
- Includes reference lines for standard BMI thresholds.
- Helps users observe changes in their recorded measurements.

### 📄 CSV Export
- Exports BMI records to a CSV file.
- Allows exported data to be opened in spreadsheet applications.
- Supports further analysis using tools such as Excel, Google Sheets, and Python.

### ⚠️ Input Validation
- Checks that the user's name is not empty.
- Validates weight and height inputs.
- Rejects invalid or non-positive measurements.
- Displays appropriate error messages for invalid input.

---

## 🧮 BMI Calculation

The application uses the standard BMI formula:

\[
\text{BMI} = \frac{\text{Weight (kg)}}{\text{Height (m)}^2}
\]

**Example:**

If a person's weight is 65 kg and height is 1.70 metres:

\[
\text{BMI} = \frac{65}{1.70 \times 1.70} \approx 22.49
\]

The calculated BMI is approximately **22.49**.

### 📊 BMI Categories

| BMI Range | Category |
|---|---|
| Below 18.5 | Underweight |
| 18.5–24.9 | Normal |
| 25.0–29.9 | Overweight |
| 30.0 and above | Obese |

> **Note:** These are general adult BMI screening categories. BMI does not directly measure body fat or account for every factor affecting individual health. This application is intended for educational and tracking purposes, not medical diagnosis.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 Python 3 | Core programming language and application logic |
| 🖥️ Tkinter | Desktop graphical user interface |
| 🗄️ SQLite | Local database storage |
| 📈 Matplotlib | BMI trend graphs and visualization |
| 📄 CSV | Exporting measurement records |
| 🕒 datetime | Recording measurement dates and times |

---

## ⚙️ Requirements

Before running the application, make sure you have:

- Python 3.x installed.
- Tkinter available in your Python installation.
- Matplotlib installed.
- A Windows, macOS, or Linux environment with a graphical desktop.

**Note:** SQLite and `datetime` are included with standard Python installations. Tkinter is usually included with Python on Windows, but some Linux installations require a separate system package.

---

## 📦 Installation

### 1. Install Python

Download Python from the official website:

https://www.python.org/downloads/

On Windows, enable **Add Python to PATH** during installation if that option is available.

### 2. Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/Jisan0178/OIBSIP_Python_Task2.git
```

### 3. Navigate to the Project Folder

```bash
cd OIBSIP_Python_Task2
```

### 4. Install Dependencies

Install the required packages using:

```bash
python -m pip install -r requirements.txt
```

If you do not have a `requirements.txt` file yet, install Matplotlib directly:

```bash
python -m pip install matplotlib
```

---

## ▶️ How to Run

1. Open the project folder in **Visual Studio Code**.
2. Open the integrated terminal.
3. Make sure the required dependencies are installed.
4. Run the Python file:

```bash
python bmi_cal.py
```


The BMI Health Tracker window should open, allowing you to enter measurements and use the available features.

---

## 🚀 How to Use the Application

1. Launch the BMI Health Tracker.
2. Enter the user's name.
3. Enter the weight in kilograms.
4. Enter the height in metres.
5. Click **Calculate BMI**.
6. Review the calculated BMI and its category.
7. Save the measurement if your application provides a separate save action; otherwise, the application may save it automatically.
8. Use **View History** to browse or search previous measurements.
9. Enter the relevant user's name and select **View BMI Trend** to view the graph.
10. Use **Export CSV** to export stored measurement records.

> The exact button names and workflow may vary slightly depending on your final implementation.

---

## 💾 Data Storage

The application uses **SQLite** for persistent local storage of BMI measurements.

The following files may be created while using the application:

```text
bmi_data.db
bmi_export.csv
```

### 🗄️ `bmi_data.db`

The database stores measurement records such as:

- User name
- Weight
- Height
- BMI value
- BMI category
- Date and time of measurement

The database allows records to remain available between application sessions.

### 📄 `bmi_export.csv`

This file contains BMI records exported from the application. It can be opened in spreadsheet software or processed using Python.

> These files are generated during application use. If your application creates them locally, you generally do not need to commit them to GitHub.

---

## 📈 BMI Trend Visualization

The application uses Matplotlib to generate graphs of a user's recorded BMI measurements.

The visualization can help users:

- Observe changes in BMI over time.
- Compare previous measurements.
- Identify general trends in their records.
- Compare recorded values with standard BMI reference thresholds.

The graph is intended to support personal record tracking rather than provide a medical assessment.

---

## 🔎 BMI History and Search

The history feature allows users to review previously stored measurements.

Depending on the implemented controls, users can:

- Browse historical records.
- Search for records by user name.
- Review BMI values and categories.
- Check measurement timestamps.

SQLite provides the underlying local storage for these records.

---

## 📄 Exporting Data to CSV

The CSV export feature makes it possible to use recorded measurements outside the application.

Exported records can be opened with:

- Microsoft Excel
- Google Sheets
- LibreOffice Calc
- Python and Pandas

This feature is useful for reviewing, organizing, and analysing saved measurement history.

---

## 📁 Project Structure

```text
OIBSIP_Python_Task2/
│
├── bmi_cal.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── bmi_data.db          # Generated locally
└── bmi_export.csv       # Generated during export
```

> **Note:** The Python filename and generated data filenames should match your actual implementation. The database and CSV files may not exist until you run the application or export records.

---

## 📦 Dependencies

The main external dependency is:

```text
matplotlib
```

A minimal `requirements.txt` file can contain:

```text
matplotlib
```

Tkinter, SQLite, `datetime`, and `csv` are standard Python modules or components and generally do not need to be installed using pip.

Install the dependencies with:

```bash
python -m pip install -r requirements.txt
```

---


## 🎥 Project Demo

Watch the demonstration of the BMI Health Tracker:

**[Watch the Project Demo](https://lnkd.in/p/dWfcB4BW)**


---

## 🧠 Learning Outcomes

Through this project, I gained practical experience with:

- Python programming and application logic.
- Creating desktop interfaces using Tkinter.
- Calculating BMI and classifying results.
- Managing local records with SQLite.
- Creating data visualizations using Matplotlib.
- Exporting data into CSV format.
- Validating user input and handling errors.
- Organizing project files and documenting software using GitHub.

---

## 🎓 Project Information

- **Project Name:** BMI Health Tracker
- **Project Type:** Python Desktop GUI Application
- **Primary Language:** Python
- **Purpose:** BMI calculation and measurement history tracking
- **Internship:** Oasis Infobyte — OIBSIP Python Programming

---

## 👨‍💻 Developer

**Jisan Ali**

🎓 B.Tech — Computer Science and Engineering (AI & ML)

Python Programming Intern — Oasis Infobyte (OIBSIP)

This project was developed as part of my Python programming learning journey and internship experience at Oasis Infobyte.

---

## 🔗 Links

- **GitHub Repository:** [OIBSIP Python Task 2](https://github.com/Jisan0178/OIBSIP_Python_Task2)
- **Oasis Infobyte Website:** [https://oasisinfobyte.com/](https://oasisinfobyte.com/)

---
