from pymongo import MongoClient
from pymongo.server_api import ServerApi
import datetime

# Define the MongoDB connection URI
uri = "mongodb+srv://vidyapannangi:test123@cluster0.6woaqse.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'grocery_store' database
    db = client.grocery_store

    # Get reference to 'products' collection
    products_collection = db.products

    # Define multiple documents to be inserted into the 'products' collection
    new_products = [
        {
            "name": "Apples",
            "category": "Fruits",
            "price": 2.0,
            "quantity": 30,
            "added_date": datetime.datetime.utcnow()
        },
        {
            "name": "Milk",
            "category": "Dairy",
            "price": 3.5,
            "quantity": 20,
            "added_date": datetime.datetime.utcnow()
        }
    ]

    # Insert the 'new_products' documents into the 'products' collection
    result = products_collection.insert_many(new_products)

    # Retrieve the IDs of the inserted documents
    document_ids = result.inserted_ids
    print("# of documents inserted: ", len(document_ids))
    print("_ids of inserted documents: ", document_ids)

except Exception as e:
    # Print any exceptions that occur
    print(e)
finally:
    # Close the MongoClient to release resources
    client.close()
