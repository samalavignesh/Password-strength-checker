import tkinter as tk
from tkinter import messagebox
import zxcvbn
import re
import webbrowser
import time
import random
import string

def measure_time(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return result, elapsed_time

def pro_info():
    file = open("temp_project_info.html", "w")
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Projects Info</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 20px;
            }
            table {
                border-collapse: collapse;
                width: 100%;
            }
            th, td {
                border: 1px solid #dddddd;
                text-align: left;
                padding: 8px;
            }
            th {
                background-color: #f2f2f2;
            }
            .project-image {
                float: right;
                margin: 10px;
            }
        </style>
    </head>
    <body>

        <img src="C:\\Users\\91824\\OneDrive\\Desktop\\supraja.png" alt="Project Image" class="project-image">
        <br><br>
        <h1>Project Info</h1>
        <p>This project was developed by <b>Team 8 </b>as part of a <b>Cyber Security Internship.</b> <br>
            This project is designed to Secure the Organizations in the Real World from Cyber Frauds performed by Hackers.</p>

        <table>
            <tr style="color: black;background-color:#f5c5c5;">
                <td><b>Project Details</b></td>
                <td><b>Explanation</b></td>
            </tr>
            <tr>
                <td>Project Name</td>
                <td>Password Strength Checker</td>
            </tr>
            <tr>
            <td>Project Description</td>
            <td>The Password Strength Checker project assesses the robustness of passwords, providing a score and estimated time to crack. <br> Implemented in Python with a Tkinter GUI, it utilizes the zxcvbn library for accurate strength analysis</td>
        </tr>
        <tr>
            <td>Project started date</td>
            <td>17-Dec-23</td>
        </tr>
        <tr>
            <td>Project end date</td>
            <td>25-DEC-23</td>
        </tr>
        <tr>
            <td>Project Status</td>
            <td><b>IN PROGRESS</b></td>
        </tr>
        </table>
    <h3>Developer Details </h3>
    <h4><b>Team 8</b></h4>
    <table>
        <tr style="background-color:#f5c5c5;">
            <td>Employee ID</td>
            <td>Employee name</td>
            <td>Email ID</td>
        </tr>
        <tr>
            <td>ST#IS#6042</td>
            <td>S. Pooja</td>
            <td></td>
        </tr>
        <tr>
            <td>ST#IS#6043</td>
            <td>Y. Sushma Sri</td>
            <td></td>
        </tr>
        <tr>
            <td>ST#IS#6044</td>
            <td>S. Vignesh</td>
            <td></td>
        </tr>
        <tr>
            <td>ST#IS#6045</td>
            <td>P. Sireesha</td>
            <td></td>
        </tr>
        <tr>
            <td>ST#IS#6046</td>
            <td>M. Uday Kiran</td>
            <td></td>
        </tr>
        <tr>
            <td>ST#IS#6047</td>
            <td>V. Tharun Reddy</td>
            <td></td>
        </tr>
    </table>
    <h3>Mentor Details</h3>
    <table>
        <tr style="background-color:#f5c5c5;">
            <td>Mentor Names</td>
        </tr>
        <tr><td>Santosh Chaluvadi(CEO)</td></tr>
        <tr><td>Upendar</td></tr>
        <tr><td>Krishna</td></tr>
        </table>
    </body>
    </html>
    '''
    file.write(html_content)
    file.close()
    webbrowser.open("temp_project_info.html")

def suggest_password(password):
    # Ensure at least one uppercase, one lowercase, one digit, and one special character
    missing_criteria = {
        'uppercase': random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']) if not re.search(r'[A-Z]', password) else '',
        'lowercase': random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']) if not re.search(r'[a-z]', password) else '',
        'digit': random.choice(string.digits) if not re.search(r'\d', password) else '',
        'special_char': random.choice(string.punctuation) if not re.search(r'[@$!%*?&#^]', password) else ''
    }

    # Concatenate the characters to form the final password
    suggested_password = password + ''.join(missing_criteria.values())
    
    # Append random characters to ensure the suggested password is always of length 12
    remaining_length = 12 - len(suggested_password)
    random_characters = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(remaining_length))
    suggested_password += random_characters

    messagebox.showinfo("Suggested Password", f"Suggested Password: {suggested_password}")

def rank_passwords(passwords):
    # Rank passwords based on their zxcvbn score
    ranked_passwords = sorted(passwords, key=lambda p: check_password_strength(p)[0]['score'], reverse=True)
    return ranked_passwords

def find_best_password(passwords):
    ranked_passwords = sorted(passwords, key=lambda p: (check_password_strength(p)[0]['score'], len(p)), reverse=True)
    return ranked_passwords[0] if ranked_passwords else None

def crack_times_display(result):
    display_text = ""
    if 'crack_times_display' in result:
        crack_times = result['crack_times_display']
        display_text += f"\nEstimated Time to Crack:\n"
        display_text += f"  Online Attack: {crack_times['online_throttling_100_per_hour']}\n"
        display_text += f"  Offline Attack: {crack_times['offline_slow_hashing_1e4_per_second']}\n"
        display_text += f"  Offline Fast Attack: {crack_times['offline_fast_hashing_1e10_per_second']}\n"
    return display_text

def on_entry_click(event):
    if input_text.get() == "Enter Password to Check":
        input_text.delete(0, tk.END)
        input_text.config(fg='black')

def check_password_strength(password):
    result, elapsed_time = measure_time(zxcvbn.zxcvbn, password)
    return result, elapsed_time

def check_password(password):
    input_text.delete(0, tk.END)
    input_text.insert(0, "Enter Password to Check")
    result_offline, time_offline = check_password_strength(password)
    strength_message = f"\nOffline Password Strength: {result_offline['score']}"
    suggestions = "\nSuggestions:\n" + "\n".join(result_offline['feedback']['suggestions'])
    crack_times = crack_times_display(result_offline)
    password_results.append({
        'password': password,
        'result': strength_message + crack_times + suggestions
    })

    # Find and display the best password so far
    best_password = find_best_password([entry['password'] for entry in password_results])
    if best_password:
        best_password_message = f"\nBest Password So Far: {best_password}"
        password_results[-1]['result'] += best_password_message

    # Update the display in the result window
    update_result_display()

def update_result_display():
    result_text.config(state=tk.NORMAL)
    result_text.delete('1.0', tk.END)
    for entry in password_results:
        result_text.insert(tk.END, f"Password: {entry['password']}\n{entry['result']}\n\n")
    result_text.config(state=tk.DISABLED)

def check_password_criteria():
    password = input_text.get()
    upper_case = re.compile(r'[A-Z]')
    lower_case = re.compile(r'[a-z]')
    digit = re.compile(r'\d')
    special_char = re.compile(r'[@$!%*?&#^]')

    upper_color = 'green' if upper_case.search(password) else 'red'
    lower_color = 'green' if lower_case.search(password) else 'red'
    digit_color = 'green' if digit.search(password) else 'red'
    special_color = 'green' if special_char.search(password) else 'red'

    upper_label.config(fg=upper_color)
    lower_label.config(fg=lower_color)
    digit_label.config(fg=digit_color)
    special_label.config(fg=special_color)

    if all(color == 'green' for color in [upper_color, lower_color, digit_color, special_color]):
        check_password(password)
    else:
        suggest_password(password)

root = tk.Tk()
root.title("Password Checker")
root.geometry("500x500")
root.configure(bg="black")

project_label = tk.Label(root, text="Password Strength Checker!!!", font=("Arial", 18, "bold"), bg="black", fg="white")
project_label.pack(pady=10)

info_button = tk.Button(root, text="Project INFO", font=("Menlo", 11), bg="red", fg="white", command=pro_info)
info_button.pack(pady=10)

input_text = tk.Entry(root, font=("Arial", 14), show="")
input_text.insert(0, "Enter Password to Check")
input_text.bind('<FocusIn>', on_entry_click)
input_text.pack(pady=10)

check_button = tk.Button(root, text="Check Password Strength", command=check_password_criteria,
                         font=("Arial", 14, "bold"), bg="green", fg="white")
check_button.pack(pady=10)

upper_label = tk.Label(root, text="Uppercase: \u2713", fg='red')
upper_label.pack()
lower_label = tk.Label(root, text="Lowercase: \u2713", fg='red')
lower_label.pack()
digit_label = tk.Label(root, text="Digit:\u2713", fg='red')
digit_label.pack()
special_label = tk.Label(root, text="Special Char: \u2713", fg='red')
special_label.pack()

result_text = tk.Text(root, height=10, width=60, state=tk.DISABLED, wrap=tk.WORD)
result_text.pack(pady=10)

password_results = []

root.mainloop()
