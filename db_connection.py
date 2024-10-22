import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def get_db_connection():
    uri = "mongodb+srv://kaizor:dbqqylwxxnwan@fridgeinventory.bgjx0.mongodb.net/?retryWrites=true&w=majority&appName=FridgeInventory"

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    # # Send a ping to confirm a successful connection
    # try:
    #     client.admin.command('ping')
    #     print("Pinged your deployment. You successfully connected to MongoDB!")
    # except Exception as e:
    #     print(e)

    # try:
    #     # List all databases on the server
    #     databases = client.list_database_names()
    #     print("Connected successfully!")
    #     print("Databases:", databases)
    # except Exception as e:
    #     print("Failed to connect to MongoDB:", e)
    db = client['FridgeInventory']

    return db