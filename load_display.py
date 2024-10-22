import streamlit as st
import pandas as pd
from db_connection import get_db_connection

# Fetch all items from the collection
db = get_db_connection()
collection = db["Freezer"]
items = list(collection.find())

# Load/refresh data from mongoDB
def load_items(query=None):
    if query:
        items = list(collection.find(query))
    else:
        items = list(collection.find({}))
    df = pd.DataFrame(items)
    return df

def display_df(query=None):
    df = load_items(query)
    column_order = ["item", "storage", "quantity", "brand", "bought_from", "expiration_date", "other"]
    df_display = df[column_order]
    df_display = df_display.rename(columns={
        "item": "Item",
        "storage": "Storage",
        "quantity": "Quantity",
        "brand": "Brand",
        "bought_from": "Bought From",
        "expiration_date": "Expiration Date",
        "other": "Other (size, container, etc)",
    })
    st.dataframe(df_display, use_container_width=True)


# Checkbox column for options
def add_checkbox_column(df):
    selected_indices = []  # List to hold the indices of selected items
    for i in range(len(df)):
        unique_key = f"checkbox_{i}_{df.at[i, '_id']}"
        selected = st.checkbox(df.at[i, 'item'], key=unique_key)
        if selected:
            selected_indices.append(i)  # Add index to selected if checked
    return selected_indices