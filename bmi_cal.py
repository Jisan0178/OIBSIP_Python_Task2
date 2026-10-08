import tkinter as tk
from tkinter import messagebox
import sqlite3
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import csv


FONT = "Arial"

COLORS = {
    "background": "#18152B",
    "card": "#25213A",
    "card_light": "#302A4A",
    "purple": "#8B5CF6",
    "purple_hover": "#A78BFA",
    "white": "#FFFFFF",
    "text": "#E5E7EB",
    "muted": "#AAA4BD",
    "border": "#49405F",
    "blue": "#38BDF8",
    "green": "#22C55E",
    "orange": "#F59E0B",
    "red": "#EF4444"
}


plt.rcParams.update({
    "font.family": FONT,
    "font.size": 10,
    "axes.titlesize": 16,
    "axes.titleweight": "bold",
    "axes.labelsize": 11,
    "axes.labelweight": "semibold",
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.fontsize": 9
})


def create_database():
    try:
        connection = sqlite3.connect("bmi_data.db")
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bmi_records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                weight REAL NOT NULL,
                height REAL NOT NULL,
                bmi REAL NOT NULL,
                category TEXT NOT NULL,
                date TEXT NOT NULL
            )
        """)

        connection.commit()
        connection.close()

    except sqlite3.Error as error:
        messagebox.showerror(
            "Database Error",
            f"Unable to create or open database.\n\n{error}"
        )


def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"

    elif bmi < 25:
        return "Normal"

    elif bmi < 30:
        return "Overweight"

    else:
        return "Obese"


def get_category_color(category):
    if category == "Underweight":
        return COLORS["blue"]

    elif category == "Normal":
        return COLORS["green"]

    elif category == "Overweight":
        return COLORS["orange"]

    else:
        return COLORS["red"]


def calculate_bmi():
    name = name_entry.get().strip()
    weight_text = weight_entry.get().strip()
    height_text = height_entry.get().strip()

    if not name:
        messagebox.showwarning(
            "Input Required",
            "Please enter your name."
        )
        return

    if not weight_text or not height_text:
        messagebox.showwarning(
            "Input Required",
            "Please enter both weight and height."
        )
        return

    try:
        weight = float(weight_text)
        height = float(height_text)

        if weight <= 0:
            messagebox.showerror(
                "Invalid Weight",
                "Weight must be greater than 0."
            )
            return

        if height <= 0:
            messagebox.showerror(
                "Invalid Height",
                "Height must be greater than 0."
            )
            return

        bmi = weight / (height ** 2)

        category = get_category(bmi)
        result_color = get_category_color(category)

        bmi_value_label.config(
            text=f"{bmi:.2f}",
            fg=result_color
        )

        bmi_category_label.config(
            text=category.upper(),
            fg=result_color
        )

        save_record(
            name,
            weight,
            height,
            bmi,
            category
        )

        weight_entry.delete(0, tk.END)
        height_entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numbers for weight and height."
        )


def save_record(name, weight, height, bmi, category):
    try:
        connection = sqlite3.connect("bmi_data.db")
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO bmi_records
            (name, weight, height, bmi, category, date)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            name,
            weight,
            height,
            bmi,
            category,
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))

        connection.commit()
        connection.close()

    except sqlite3.Error as error:
        messagebox.showerror(
            "Database Error",
            f"Unable to save BMI record.\n\n{error}"
        )


def show_history():
    history_window = tk.Toplevel(window)
    history_window.title("BMI History")
    history_window.geometry("850x600")
    history_window.configure(
        bg=COLORS["background"]
    )
    history_window.resizable(False, False)

    title = tk.Label(
        history_window,
        text="BMI HISTORY",
        font=(FONT, 20, "bold"),
        bg=COLORS["background"],
        fg=COLORS["white"]
    )
    title.pack(pady=(25, 5))

    subtitle = tk.Label(
        history_window,
        text="View saved BMI records",
        font=(FONT, 10),
        bg=COLORS["background"],
        fg=COLORS["muted"]
    )
    subtitle.pack()

    search_frame = tk.Frame(
        history_window,
        bg=COLORS["background"]
    )
    search_frame.pack(pady=20)

    search_entry = tk.Entry(
        search_frame,
        width=30,
        font=(FONT, 11),
        bg=COLORS["card_light"],
        fg=COLORS["white"],
        insertbackground=COLORS["white"],
        relief="flat"
    )
    search_entry.pack(
        side=tk.LEFT,
        ipady=8,
        padx=(0, 10)
    )

    history_text = tk.Text(
        history_window,
        width=96,
        height=24,
        font=(FONT, 10),
        bg=COLORS["card"],
        fg=COLORS["text"],
        insertbackground=COLORS["white"],
        relief="flat",
        padx=15,
        pady=15
    )
    history_text.pack(padx=25)

    def load_history():
        history_text.delete("1.0", tk.END)

        search_name = search_entry.get().strip()

        try:
            connection = sqlite3.connect("bmi_data.db")
            cursor = connection.cursor()

            if search_name:
                cursor.execute("""
                    SELECT name, weight, height, bmi, category, date
                    FROM bmi_records
                    WHERE name LIKE ?
                    ORDER BY id DESC
                """, (f"%{search_name}%",))

            else:
                cursor.execute("""
                    SELECT name, weight, height, bmi, category, date
                    FROM bmi_records
                    ORDER BY id DESC
                """)

            records = cursor.fetchall()
            connection.close()

            if not records:
                history_text.insert(
                    tk.END,
                    "\nNo records found."
                )
                return

            for record in records:
                name, weight, height, bmi, category, date = record

                history_text.insert(
                    tk.END,
                    f"Name      : {name}\n"
                    f"Weight    : {weight:.2f} kg\n"
                    f"Height    : {height:.2f} m\n"
                    f"BMI       : {bmi:.2f}\n"
                    f"Category  : {category}\n"
                    f"Date      : {date}\n"
                    f"{'-' * 80}\n"
                )

        except sqlite3.Error as error:
            messagebox.showerror(
                "Database Error",
                f"Unable to read BMI records.\n\n{error}"
            )

    search_button = tk.Button(
        search_frame,
        text="SEARCH",
        command=load_history,
        font=(FONT, 10, "bold"),
        bg=COLORS["purple"],
        fg=COLORS["white"],
        activebackground=COLORS["purple_hover"],
        activeforeground=COLORS["white"],
        relief="flat",
        cursor="hand2",
        padx=20,
        pady=7
    )
    search_button.pack(side=tk.LEFT)

    load_history()


def show_graph():
    user_name = name_entry.get().strip()

    if not user_name:
        messagebox.showwarning(
            "Name Required",
            "Enter the user's name to view the BMI trend."
        )
        return

    try:
        connection = sqlite3.connect("bmi_data.db")
        cursor = connection.cursor()

        cursor.execute("""
            SELECT bmi, date
            FROM bmi_records
            WHERE name LIKE ?
            ORDER BY id ASC
        """, (f"%{user_name}%",))

        records = cursor.fetchall()
        connection.close()

        if not records:
            messagebox.showinfo(
                "No Records",
                f"No BMI records found for {user_name}."
            )
            return

        bmi_values = []
        dates = []

        for bmi, date in records:
            bmi_values.append(bmi)

            dates.append(
                datetime.datetime.strptime(
                    date,
                    "%Y-%m-%d %H:%M:%S"
                )
            )

        figure = plt.figure(
            figsize=(10, 6),
            facecolor=COLORS["background"]
        )

        axis = figure.add_subplot(111)
        axis.set_facecolor(COLORS["card"])

        axis.plot(
            dates,
            bmi_values,
            marker="o",
            markersize=7,
            linewidth=2.5,
            color=COLORS["purple_hover"],
            label="BMI"
        )

        for date, bmi in zip(dates, bmi_values):
            axis.annotate(
                f"{bmi:.1f}",
                (date, bmi),
                xytext=(0, 10),
                textcoords="offset points",
                ha="center",
                color=COLORS["white"],
                fontsize=9
            )

        axis.axhline(
            y=18.5,
            linestyle="--",
            linewidth=1,
            color=COLORS["blue"],
            label="18.5"
        )

        axis.axhline(
            y=25,
            linestyle="--",
            linewidth=1,
            color=COLORS["green"],
            label="25"
        )

        axis.axhline(
            y=30,
            linestyle="--",
            linewidth=1,
            color=COLORS["red"],
            label="30"
        )

        axis.set_title(
            f"BMI Trend - {user_name}",
            color=COLORS["white"],
            pad=15
        )

        axis.set_xlabel(
            "Date",
            color=COLORS["text"]
        )

        axis.set_ylabel(
            "BMI",
            color=COLORS["text"]
        )

        axis.tick_params(
            colors=COLORS["muted"]
        )

        for spine in axis.spines.values():
            spine.set_color(COLORS["border"])

        axis.grid(
            True,
            linestyle=":",
            alpha=0.35
        )

        axis.xaxis.set_major_formatter(
            mdates.DateFormatter("%b %d")
        )

        axis.legend(
            facecolor=COLORS["card_light"],
            edgecolor=COLORS["border"],
            labelcolor=COLORS["white"]
        )

        figure.tight_layout()
        plt.show()

    except sqlite3.Error as error:
        messagebox.showerror(
            "Database Error",
            f"Unable to read BMI records.\n\n{error}"
        )

    except ValueError:
        messagebox.showerror(
            "Date Error",
            "Unable to process the saved date."
        )


def export_to_csv():
    try:
        connection = sqlite3.connect("bmi_data.db")
        cursor = connection.cursor()

        cursor.execute("""
            SELECT name, weight, height, bmi, category, date
            FROM bmi_records
            ORDER BY id DESC
        """)

        records = cursor.fetchall()
        connection.close()

        if not records:
            messagebox.showinfo(
                "No Data",
                "There are no BMI records to export."
            )
            return

        with open(
            "bmi_export.csv",
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "Name",
                "Weight",
                "Height",
                "BMI",
                "Category",
                "Date"
            ])

            writer.writerows(records)

        messagebox.showinfo(
            "Export Successful",
            "BMI records have been exported to bmi_export.csv."
        )

    except sqlite3.Error as error:
        messagebox.showerror(
            "Database Error",
            f"Unable to read BMI records.\n\n{error}"
        )

    except OSError as error:
        messagebox.showerror(
            "File Error",
            f"Unable to create CSV file.\n\n{error}"
        )


def create_input(parent, label_text):
    frame = tk.Frame(
        parent,
        bg=COLORS["card"]
    )

    label = tk.Label(
        frame,
        text=label_text,
        font=(FONT, 10, "bold"),
        bg=COLORS["card"],
        fg=COLORS["text"]
    )
    label.pack(
        anchor="w",
        pady=(0, 6)
    )

    entry = tk.Entry(
        frame,
        font=(FONT, 11),
        bg=COLORS["card_light"],
        fg=COLORS["white"],
        insertbackground=COLORS["white"],
        relief="flat",
        highlightthickness=1,
        highlightbackground=COLORS["border"],
        highlightcolor=COLORS["purple"]
    )

    entry.pack(
        fill="x",
        ipady=9
    )

    return frame, entry


def create_action_button(parent, text, command):
    button = tk.Button(
        parent,
        text=text,
        command=command,
        font=(FONT, 9, "bold"),
        bg=COLORS["card_light"],
        fg=COLORS["text"],
        activebackground=COLORS["purple"],
        activeforeground=COLORS["white"],
        relief="flat",
        cursor="hand2",
        pady=9
    )

    button.pack(
        fill="x",
        pady=4
    )

    return button


create_database()

window = tk.Tk()
window.title("BMI Health Tracker")
window.geometry("760x720")
window.configure(
    bg=COLORS["background"]
)
window.resizable(False, False)


header = tk.Frame(
    window,
    bg=COLORS["background"]
)
header.pack(
    fill="x",
    padx=40,
    pady=(30, 10)
)


title = tk.Label(
    header,
    text="BMI HEALTH TRACKER",
    font=(FONT, 25, "bold"),
    bg=COLORS["background"],
    fg=COLORS["white"]
)
title.pack(
    anchor="w"
)


subtitle = tk.Label(
    header,
    text="Calculate and track your Body Mass Index",
    font=(FONT, 10),
    bg=COLORS["background"],
    fg=COLORS["muted"]
)
subtitle.pack(
    anchor="w",
    pady=(5, 0)
)


content = tk.Frame(
    window,
    bg=COLORS["background"]
)
content.pack(
    fill="both",
    expand=True,
    padx=40,
    pady=20
)


left_card = tk.Frame(
    content,
    bg=COLORS["card"],
    width=320,
    height=470
)
left_card.pack(
    side="left",
    fill="y",
    padx=(0, 12)
)
left_card.pack_propagate(False)


input_title = tk.Label(
    left_card,
    text="PERSONAL DETAILS",
    font=(FONT, 14, "bold"),
    bg=COLORS["card"],
    fg=COLORS["purple_hover"]
)
input_title.pack(
    anchor="w",
    padx=25,
    pady=(25, 20)
)


name_frame, name_entry = create_input(
    left_card,
    "Full Name"
)
name_frame.pack(
    fill="x",
    padx=25,
    pady=(0, 15)
)


weight_frame, weight_entry = create_input(
    left_card,
    "Weight (kg)"
)
weight_frame.pack(
    fill="x",
    padx=25,
    pady=(0, 15)
)


height_frame, height_entry = create_input(
    left_card,
    "Height (m)"
)
height_frame.pack(
    fill="x",
    padx=25,
    pady=(0, 20)
)


calculate_button = tk.Button(
    left_card,
    text="CALCULATE BMI",
    command=calculate_bmi,
    font=(FONT, 11, "bold"),
    bg=COLORS["purple"],
    fg=COLORS["white"],
    activebackground=COLORS["purple_hover"],
    activeforeground=COLORS["white"],
    relief="flat",
    cursor="hand2",
    pady=12
)
calculate_button.pack(
    fill="x",
    padx=25
)


right_card = tk.Frame(
    content,
    bg=COLORS["card"],
    width=320,
    height=470
)
right_card.pack(
    side="left",
    fill="y"
)
right_card.pack_propagate(False)


result_title = tk.Label(
    right_card,
    text="BMI RESULT",
    font=(FONT, 14, "bold"),
    bg=COLORS["card"],
    fg=COLORS["purple_hover"]
)
result_title.pack(
    anchor="w",
    padx=25,
    pady=(25, 10)
)


score_label = tk.Label(
    right_card,
    text="BMI SCORE",
    font=(FONT, 9, "bold"),
    bg=COLORS["card"],
    fg=COLORS["muted"]
)
score_label.pack(
    pady=(25, 0)
)


bmi_value_label = tk.Label(
    right_card,
    text="--",
    font=(FONT, 45, "bold"),
    bg=COLORS["card"],
    fg=COLORS["purple_hover"]
)
bmi_value_label.pack()


bmi_category_label = tk.Label(
    right_card,
    text="READY",
    font=(FONT, 13, "bold"),
    bg=COLORS["card"],
    fg=COLORS["muted"]
)
bmi_category_label.pack(
    pady=(0, 30)
)


button_frame = tk.Frame(
    right_card,
    bg=COLORS["card"]
)
button_frame.pack(
    fill="x",
    padx=25
)


create_action_button(
    button_frame,
    "VIEW HISTORY",
    show_history
)


create_action_button(
    button_frame,
    "VIEW BMI TREND",
    show_graph
)


create_action_button(
    button_frame,
    "EXPORT CSV",
    export_to_csv
)


footer = tk.Label(
    window,
    text="Developed by Jisan Ali © 2026",
    font=(FONT, 9),
    bg=COLORS["background"],
    fg=COLORS["muted"]
)
footer.pack(
    pady=(0, 20)
)


window.mainloop()