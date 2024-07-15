import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount, get_category, get_date, get_description

class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]
    #Class method has access to the class itself, not an instance
    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            #A dataframe is an object within pandas that allows us to accesss stuff easily, well export this dataframe to a csv file now
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }
        #a is for append
        with open(cls.CSV_FILE, "a", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully")

def add():
    CSV.initialize_csv
    date = get_date("Enter the date of the transaction (dd-mm-yyyy) or enter for today's date: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)

add()