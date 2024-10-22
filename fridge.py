# cd '.\OneDrive\桌面\Fridge Inventory\'

# Needs to be first line
import streamlit as st
st.set_page_config(page_title="Fridge Inventory", layout="wide")

import pandas as pd
from db_connection import get_db_connection
from add_item_form import add_item_form
from query_form import query_form
from delete_item import delete_item_form
from load_display import load_items, display_df, add_checkbox_column

# Set up the title for the main page
st.title("Fridge Inventory")

# Fetch all items from the collection
db = get_db_connection()
collection = db["Freezer"]
items = list(collection.find())

# Load data
if 'df' not in st.session_state:
    st.session_state.df = load_items()  # Load items initially

# Sidebar
st.sidebar.subheader("Choose an operation")
option = st.sidebar.selectbox(label="", label_visibility="collapsed", options=("Query", "Add item", "Delete item"))

# Display respective form based on the selection
if option == "Query":
    query = query_form()
    display_df(query)
elif option == "Add item":
    add_item_form()
    display_df()
elif option == "Delete item":
    delete_item_form(st.session_state.df, collection)
    display_df()

# # Selection (NOT USED)
# selected_indices = add_checkbox_column(st.session_state.df)
# if selected_indices:
#     selected_items = st.session_state.df.iloc[selected_indices].copy()
#     selected_items['select'] = True  # Mark selected items
# else:
#     selected_items = pd.DataFrame(columns=st.session_state.df.columns)

# if not selected_items.empty:
#     with st.expander("Options"):
#         if st.button("Delete Selected Items"):
#             # # Delete selected items from MongoDB
#             # for _, row in selected_items.iterrows():
#             #     collection.delete_one({'_id': row['_id']})  # Use MongoDB document ID to delete
#             # st.success("Selected items deleted successfully")
            
#             # # Refresh the DataFrame after deletion
#             # display_df()
#             # st.write("Updated Items in Database")
#             delete_item(selected_items, collection)

# else:
#     st.write("No items selected for deletion")

# st.expander("Options")
# delete_item_form(selected_items, collection)