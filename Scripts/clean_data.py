clean_educational_data.py

import pandas as pd
import os

# Define file paths for educational data
edu_file_paths = [
    "Educational_Attainment2018.csv",
    "Educational_Attainment2019.csv",
    "Educational_Attainment2020.csv",
    "Educational_Attainment2021.csv",
    "Educational_Attainment2022.csv"
]

# Combine educational data
def clean_educational_data(output_file="Educational_Attainment_Combined.csv"):
    combined_df = pd.DataFrame()
    for file in edu_file_paths:
        if os.path.exists(file):
            df = pd.read_csv(file)
            year = file.split("Attainment")[1].split(".")[0]  # Extract year
            df['year'] = int(year)
            combined_df = pd.concat([combined_df, df], ignore_index=True)
            print(f"Loaded {file}")
        else:
            print(f"File not found: {file}")
    combined_df.to_csv(output_file, index=False)
    print(f"Combined data saved to {output_file}")

if __name__ == "__main__":
    clean_educational_data()










clean_crime_data.py

import pandas as pd
import os
import re

# Define file paths for crime data
crime_file_paths = [
    "HoustonLargestPD.csv",
    "ChicagoLargestPD.csv",
    "NewYorkLargestPD.csv",
    "PhoenixLargestPD.csv",
    "LosAngelesLargestPD.csv"
]

# Combine and clean crime data
def clean_crime_data(output_file="Cleaned_Crime_Data.csv"):
    combined_df = pd.DataFrame()
    for file in crime_file_paths:
        if os.path.exists(file):
            df = pd.read_csv(file)
            combined_df = pd.concat([combined_df, df], ignore_index=True)
            print(f"Loaded {file}")
        else:
            print(f"File not found: {file}")
    
    # Melt and clean data
    year_columns = combined_df.filter(regex=r"\d{4}").columns
    combined_df = combined_df.melt(id_vars=["series"], value_vars=year_columns, var_name="year", value_name="value")
    combined_df.dropna(subset=["year", "value"], inplace=True)
    combined_df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")

if __name__ == "__main__":
    clean_crime_data()











visualize_data.py

import pandas as pd
import matplotlib.pyplot as plt

# Plot Educational Data Trends
def plot_educational_trends(input_file="Educational_Attainment_Combined.csv"):
    edu_df = pd.read_csv(input_file)
    edu_summary = edu_df.groupby("year")["value"].sum().reset_index()

    plt.figure(figsize=(10, 6))
    plt.plot(edu_summary["year"], edu_summary["value"], marker='o', color='blue')
    plt.title("Educational Data Trends Over Time")
    plt.xlabel("Year")
    plt.ylabel("Total Educational Values")
    plt.grid(True)
    plt.show()

# Plot Crime Trends
def plot_crime_trends(input_file="Cleaned_Crime_Data.csv"):
    crime_df = pd.read_csv(input_file)
    crime_summary = crime_df.groupby("year")["value"].sum().reset_index()

    plt.figure(figsize=(10, 6))
    plt.plot(crime_summary["year"], crime_summary["value"], marker='o', color='red')
    plt.title("Crime Trends Over Time")
    plt.xlabel("Year")
    plt.ylabel("Total Crime Values")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    print("Generating Educational Trends Plot...")
    plot_educational_trends()
    print("Generating Crime Trends Plot...")
    plot_crime_trends()






