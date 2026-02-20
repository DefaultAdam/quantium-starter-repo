import pandas as pd

# manually list the files
files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv"
]

frames = []

for file in files:
    df = pd.read_csv(file)

    # keep only Pink Morsels
    df = df[df["product"] == "pink morsel"]

    # create sales column
    df["sales"] = df["quantity"] * df["price"]

    # keep required columns
    df = df[["sales", "date", "region"]]

    frames.append(df)

# combine into one dataset
final_df = pd.concat(frames, ignore_index=True)

# export result
final_df.to_csv("formatted_sales.csv", index=False)

print("formatted_sales.csv created successfully")