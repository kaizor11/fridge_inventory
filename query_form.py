import streamlit as st
from datetime import datetime, timedelta
from db_connection import get_db_connection

# Query Form
def query_form():
    st.sidebar.subheader("Query Items")
    with st.sidebar.form(key='query_form'):
        # Input for item name
        item_query = st.text_input("Item Name")

        # Input for storage
        storage_query = st.selectbox("Stored in", ["All", "Fridge", "Freezer"])

        # # Checkbox to query for quantity
        # quantity_check = st.checkbox("Filter by Quantity")
        # quantity_query = None
        # if quantity_check:
        #     quantity_query = st.number_input("Quantity", min_value=1)

        # Input for brand
        brand_query = st.text_input("Brand")

        # Bought from
        options = ["Costco", "Weee!/99 Ranch", "Ralph's/Trader Joe's, etc", "Other"]
        bought_query = st.multiselect("Bought from:", options)

        # Expiration date
        days_until_expiration = st.number_input("Days until Expiration", min_value=0)

        # Input for "other" field
        other_query = st.text_input("Other Details")

        query = {}
        if item_query:
            query['item'] = {"$regex": item_query, "$options": "i"}
        if storage_query:
            if storage_query == "All":
                pass
            else:
                query['storage'] = storage_query
        # if quantity_check and quantity_query is not None:
        #     query['quantity'] = quantity_query
        if brand_query:
            query['brand'] = {"$regex": brand_query, "$options": "i"}
        if bought_query:
            query['bought_from'] = {"bought_from":{"$in": bought_query}}
        if days_until_expiration:
            expiration_date = (datetime.now() + timedelta(days=days_until_expiration)).isoformat()
            query['expiration_date'] = {"$lte": expiration_date}
        if other_query:
            query['other'] = {"$regex": other_query, "$options": "i"}

        submit_button = st.form_submit_button(label="Search")
        
        if submit_button:
            return query