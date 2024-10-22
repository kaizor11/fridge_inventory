import streamlit as st
from db_connection import get_db_connection

# Add Item Form
def add_item_form():
    st.sidebar.subheader("Add Item")
    with st.sidebar.form(key='add_item_form'):
        item = st.text_input("Item Name")
        storage = st.selectbox("Stored in", ["Fridge", "Freezer"])
        quantity = st.number_input("Quantity", min_value=1)
        brand = st.text_input("Brand")
        bought_from = st.selectbox("Bought from", ["Costco", "Weee!/99 Ranch", "Ralph's/Trader Joe's, etc", "Other"])
        expiration_date = st.date_input("Expiration Date")
        other = st.text_input("Other details")

        submit_button = st.form_submit_button(label="Add item")
        if submit_button:
            db = get_db_connection()
            collection = db["Freezer"]
            expiration_date_str = expiration_date.isoformat() if expiration_date else None
            collection.insert_one({
                'item': item, 
                'storage': storage, 
                'quantity': quantity, 
                'brand': brand, 
                'bought_from': bought_from,
                'expiration_date': expiration_date_str, 
                'other': other})
            st.sidebar.success(f"Added {item}")
            # st.experimental_rerun()  # Rerun the app to refresh the table