import pandas as pd
import numpy as np
import csv
import seaborn as sns
import pandas as pd
from scipy.stats import pearsonr
import zipfile
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import tkinter as tk

root = tk.Tk()
root.title("Loan Application Predictor")
root.geometry('900x500')
main_frame = tk.LabelFrame(
    root,
    bg = "#F3D5B9",
    text = 'Inputs',
)


def save_results():
    # Retrieve the selected values from the variables
    global list_headings
    global inp_gender
    global inp_property_type
    global inp_loan_amount
    global inp_loan_type
    global inp_loan_purp
    global inp_lien_status
    global inp_owner_occ
    global heading_variable_pairs
    # global inp_income 
    list_headings = ['Gender', 'Property Type', 'Loan Amount', 'Loan Type', 
                     'Loan Purpose', 'Lien Status', 'Owner Occupancy']

    # no median family income for census

    # inp_gender = gender_var.get()
    inp_gender = gender_var.get()
    inp_property_type = property_type.get()
    inp_loan_amount = loan_amount.get()
    inp_loan_amount = int(inp_loan_amount)
    inp_loan_type = loan_type.get()
    inp_loan_purp = loan_purp.get()
    inp_lien_status = lien_status.get()
    inp_owner_occ = owner_occ.get()
    inp_income = income.get()
    inp_income = int(inp_income)
    list_variables = [inp_gender, inp_property_type, inp_loan_amount, inp_loan_type, inp_loan_purp, inp_lien_status, inp_owner_occ, inp_income]
    heading_variable_pairs = {}
    heading_variable_pairs = {'loan_amount_000s':[inp_loan_amount//1000], 'hud_median_family_income':[inp_income//1000],
       'prop_type_cat_1':[1 if inp_property_type == "One-to-four family dwelling (other than manufactured housing)" else 0], 
       'prop_type_cat_2':[1 if inp_property_type == 'Manufactured housing' else 0], 
       'prop_type_cat_3':[1 if inp_property_type == 'Multifamily dwelling' else 0],
       'owner_occu_cat_1':[1 if inp_owner_occ == 'Owner-occupied as a principal dwelling' else 0], 
       'owner_occu_cat_2':[1 if inp_owner_occ == 'Not Owner-occupied as a principal dwelling' else 0], 
       'owner_occu_cat_3':[1 if inp_owner_occ ==  'Not Applicable' else 0],
       'loan_type_cat_1':[1 if inp_loan_type == loan_type_options[0] else 0], 
       'loan_type_cat_2':[1 if inp_loan_type == loan_type_options[1] else 0], 
       'loan_type_cat_3':[1 if inp_loan_type == loan_type_options[2] else 0],
       'loan_type_cat_4':[1 if inp_loan_type == loan_type_options[3] else 0], 
       'loan_purp_cat_1':[1 if inp_loan_purp == loan_purpose_options[0] else 0], 
       'loan_purp_cat_2':[1 if inp_loan_purp == loan_purpose_options[1] else 0],
       'loan_purp_cat_3':[1 if inp_loan_purp == loan_purpose_options[2] else 0], 
       'lien_status_cat_1':[1 if inp_lien_status == lien_status_options[0] else 0], 
       'lien_status_cat_2':[1 if inp_lien_status == lien_status_options[0] else 0],
       'lien_status_cat_3':[1 if inp_lien_status == lien_status_options[0] else 0]}
    root.destroy()


# The background image
bgimg= tk.PhotoImage(file = "background.png")
limg= tk.Label(root, i=bgimg)
limg.pack()

main_frame = tk.LabelFrame(
    root,
    text = 'Inputs',
)
main_frame.place(anchor = 'c', relx = 0.5, rely=0.21)

# Initalizing all parameter variables
gender_var = tk.StringVar()
loan_amount = tk.StringVar()
property_type = tk.StringVar()
loan_type = tk.StringVar()
loan_purp = tk.StringVar()
lien_status = tk.StringVar()
owner_occ = tk.StringVar()
income = tk.StringVar()

# LABLES
gender_label = tk.Label(main_frame, text="What is your gender?").grid(row = 1, column = 0)
property_type_label = tk.Label(main_frame, text="What is your property type?").grid(row = 2, column = 0)
loan_amount_label = tk.Label(main_frame, text = 'How Much are you applying for?').grid(row = 3, column = 0)
loan_type_label = tk.Label(main_frame, text="What Type of Loan are you Applying for?").grid(row = 4, column = 0)
loan_purp_label = tk.Label(main_frame, text="Why are you applying for the Loan?").grid(row = 5, column = 0)
lien_status_label = tk.Label(main_frame, text="What is your Lien Status?").grid(row = 6, column = 0)
owner_occ_label = tk.Label(main_frame, text="Are you planning on Residing in the Residence?").grid(row = 7, column = 0)
income_label = tk.Label(main_frame, text="What is your Current Income?").grid(row = 8, column = 0)
# loan_label = tk.Label(main_frame, text = 'Loan Outcome').grid(row = 9, column = 0)

# OPTIONS
gender_options = ['Male', 'Female', 'Other']
property_type_options = ['One-to-four family dwelling (other than manufactured housing)', 'Manufactured housing', 'Multifamily dwelling']
loan_type_options = ['Conventional','FHA-insured','VA-guaranteed','FSA/RHS-guaranteed']
loan_purpose_options = ['Refinancing','Home purchase','Home improvement']
lien_status_options = ['Secured by a first lien','Not Applicable','Secured by a subordinate lien','Not Secured by a lien']
owner_occ_options = ['Owner-occupied as a principal dwelling','Not Owner-occupied as a principal dwelling','Not Applicable']

gender_menu = tk.OptionMenu(main_frame, gender_var, *gender_options).grid(row = 1, column = 1)
property_type_menu = tk.OptionMenu(main_frame, property_type, *property_type_options).grid(row = 2, column = 1)
loan_amount_menu = tk.Entry(main_frame, textvariable=loan_amount).grid(row = 3, column = 1)
loan_type_menu = tk.OptionMenu(main_frame, loan_type, *loan_type_options).grid(row = 4, column = 1)
loan_purp_menu = tk.OptionMenu(main_frame, loan_purp, *loan_purpose_options).grid(row = 5, column = 1)
lien_status_menu = tk.OptionMenu(main_frame, lien_status,*lien_status_options).grid(row = 6, column = 1)
owner_occ_menu = tk.OptionMenu(main_frame, owner_occ,*owner_occ_options).grid(row = 7, column = 1)
owner_occ_menu = tk.Entry(main_frame, textvariable=income).grid(row = 8, column = 1)

# Saving all current chosen variables when the user presses save
save_button = tk.Button(root, text="Save Results", command=save_results)
save_button.place(anchor = 'c', relx = 0.5, rely = 0.8)

# def unzip_data() -> list:
#     """Get json data (all business data from yelp)."""
#     zip_path = 'table.zip'

#     directory_csv = 'GENAI-2024'

#     with zipfile.ZipFile(zip_path, 'r') as zip_ref:
#         zip_ref.extract('table.csv', directory_csv)

#     csv_file_path = os.path.join(directory_csv, 'table.csv')
#     df = pd.read_csv(csv_file_path)
#     return df

# dataframe = unzip_data()

# # Function to calculate and annotate correlation
# def correlation(y, ax=None, **kws):
#     r, _ = pearsonr(dataframe['loan_status'], y)
#     ax = ax or plt.gca()
#     ax.annotate(f'ρ = {r:.2f}', xy=(.1, .9), xycoords=ax.transAxes)


# # Create a seaborn pairplot
# pp = sns.pairplot(data=dataframe, y_vars=['loan_status'], x_vars=dataframe.columns)


# # Apply the correlation annotation to the pairplot
# pp.map_lower(correlation)


# # Convert the Matplotlib plot to a Tkinter canvas
# canvas = FigureCanvasTkAgg(pp.fig, master=root)
# canvas.draw()
# canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


# # Add a quit button
# quit_button = tk.Button(root, text="Quit", command=root.quit)
# quit_button.pack(side=tk.BOTTOM)


root.mainloop()