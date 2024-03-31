"""
from reactpy import component, html, run

@component
def IdentifyGender():
    def handle_gender_choice(event):
        gender = event.get('target', {}).get('value')
        print("Selected gender:", gender)
    
    return html.form(
        html.label({"for": "male"}, "Male"),
        html.input({"type": "radio", "name": "gender", "id": "male", "value": "male", "on_change": handle_gender_choice}),
        html.label({"for": "female"}, "Female"),
        html.input({"type": "radio", "name": "gender", "id": "female", "value": "female", "on_change": handle_gender_choice}),
        html.label({"for": "other"}, "Other"),
        html.input({"type": "radio", "name": "gender", "id": "other", "value": "other", "on_change": handle_gender_choice})
    )


@component
def IdentifyRace():
    def handle_race_choice(event):
        race = event.get('target', {}).get('value')
        print("Selected race:", race)
    
    return html.form(
        html.label({"for": "native"}, "American Indian or Alaska Native"),
        html.input({"type": "radio", "name": "race", "id": "native", "value": "native", "on_change": handle_race_choice}),
        html.label({"for": "asian"}, "Asian"),
        html.input({"type": "radio", "name": "race", "id": "asian", "value": "asian", "on_change": handle_race_choice}),
        html.label({"for": "black"}, "Black or African American"),
        html.input({"type": "radio", "name": "race", "id": "black", "value": "black", "on_change": handle_race_choice}),
        html.label({"for": "hawaiian"}, "Native Hawaiian or Other Pacific Islander"),
        html.input({"type": "radio", "name": "race", "id": "hawaiian", "value": "hawaiian", "on_change": handle_race_choice}),
        html.label({"for": "white"}, "White"),
        html.input({"type": "radio", "name": "race", "id": "white", "value": "white", "on_change": handle_race_choice})
    )



American Indian or Alaska Native (DONE)
Asian (DONE)
Black or African American (DONE)
Native Hawaiian or Other Pacific Islander (DONE)
White (DONE)
*Co-applicant race 
*Information not provided by applicant in mail, Internet, or telephone application
*No co-applicant
*Not applicable


@component
def IdentityForm():
    return html.div(
        IdentifyGender(),
        IdentifyRace()
    )

run(IdentityForm)
"""
import pandas as pd
import numpy as np
import csv

list_variables = []
list_headings = ['Gender']

def save_results():
    # Retrieve the selected values from the variables
    selected_gender = gender_var.get()
    selected_property_type = property_type_var.get()
    list_variables.append(selected_gender)
    list_variables.append(property_type_var)

    heading_variable_pairs = {}
    for i in range(len(list_headings) - 1):
        heading_variable_pairs[list_headings[i]] = list_variables[i]

    with open('main.csv', 'w') as f:
        for key in heading_variable_pairs.keys():
            f.write("%s,%s\n"%(key,heading_variable_pairs[key]))
    with open('main.csv', mode ='r')as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            print(lines)

import tkinter as tk

root = tk.Tk()
root.title("INSERT PROGRAM TITLE HERE")
root.geometry('900x500')
main_frame = tk.LabelFrame(
    root,
    text = 'Inputs',
)
main_frame.place(anchor = 'c', relx = 0.5, rely=0.21)

# Initalizing all parameter variables
gender_var = tk.StringVar()
property_type_var = tk.StringVar()

# BUTTONS FOR GENDER
gender_label = tk.Label(main_frame, text="What is your gender?")
gender_label.pack(padx=25, pady=15)
# BUTTONS FOR PROPERTY TYPE
property_type_label = tk.Label(root, text="What is your property type?")
property_type_label.pack(padx=25, pady=15)

# Create three frames for the columns
# main_frame = tk.Frame(root)

# # Pack the frames side by side
# gender_left_frame.pack(side="left", fill="both", expand=True)
# gender_middle_frame.pack(side="left", fill="both", expand=True)
# gender_right_frame.pack(side="right", fill="both", expand=True)

# Create radio buttons in each frame
# gender_button1 = tk.Radiobutton(gender_right_frame, text="Male", variable=gender_var, value="Male")
# gender_button2 = tk.Radiobutton(gender_left_frame, text="Female", variable=gender_var, value="Female")
# gender_button3 = tk.Radiobutton(gender_middle_frame, text="Other", variable=gender_var, value="Other")
gender_menu = tk.OptionMenu(main_frame, 'Male', 'Female', 'Other')


# Pack the radio buttons within each frame
# radio_button1.pack(side="top", anchor="w")
# radio_button2.pack(side="top", anchor="w")
# radio_button3.pack(side="top", anchor="w")

# Saving all current chosen variables when the user presses save
save_button = tk.Button(root, text="Save Results", command=save_results)
save_button.pack(pady=10)

root.mainloop()