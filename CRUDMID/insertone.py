from pymongo import MongoClient
from pymongo.server_api import ServerApi
import datetime

# Define the MongoDB connection URI
uri = "mongodb+srv://vidyapannangi:test123@cluster0.6woaqse.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Get reference to the 'grocery_store' database
    db = client.grocery_store

    # Get reference to the 'products' collection
    products_collection = db.products

    # Define a document to be inserted into the 'products' collection
    new_product = {
        "name": "Bananas",
        "category": "Fruits",
        "price": 1.5,
        "quantity": 50,
        "added_date": datetime.datetime.utcnow()
    }

    # Insert the 'new_product' document into the 'products' collection
    result = products_collection.insert_one(new_product)

    # Retrieve the ID of the inserted document
    document_id = result.inserted_id
    print("_id of inserted document: ", document_id)

except Exception as e:
    # Print any exceptions that occur
    print(e)
finally:
    # Close the MongoClient to release resources
    client.close()
