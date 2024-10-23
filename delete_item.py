import streamlit as st
from datetime import datetime, timedelta
import pandas as pd
from load_display import load_items

# Add Item Form
def delete_item_form(collection):
    df = load_items()
    st.sidebar.subheader("Delete item")
    with st.sidebar.form(key='delete_item_form'):
        # Submit button to delete items
        indices_input = st.text_input("Indicies to delete (separated by spaces)")
        if st.form_submit_button("Delete selected items"):
            # Convert input string to a list of integers
            try:
                indices_to_delete = sorted([int(x) for x in indices_input.split()], reverse=True) # +1 because st works in 1-based indexing
                if all(index in df.index for index in indices_to_delete):
                    # Select the rows corresponding to the indices
                    selected_items = df.iloc[indices_to_delete]

                    # Delete items from MongoDB using their `_id`
                    for _, row in selected_items.iterrows():
                        collection.delete_one({'_id': row['_id']})  # Use MongoDB document ID to delete

                    # Drop rows from DataFrame
                    df = df.drop(indices_to_delete)

                    # Reset the DataFrame index after deletion
                    df = df.reset_index(drop=True)

                else:
                    st.error("Out of range")

            except ValueError:
                st.error("Please enter valid integer indices")
                indices_to_delete = []


# OUT OF RANGE ERROR