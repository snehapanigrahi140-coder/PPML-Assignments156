import pandas as pd
# Put sample.csv and sample.json in this same folder before running.
try:
    print("CSV data:\n", pd.read_csv("sample.csv"))
except FileNotFoundError:
    print("sample.csv not found. Add the file to this folder.")
try:
    print("\nJSON data:\n", pd.read_json("sample.json"))
except ValueError:
    print("sample.json not found or contains invalid JSON.")
