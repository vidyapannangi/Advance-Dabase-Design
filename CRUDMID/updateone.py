from pymongo import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import pprint

# Define the MongoDB connection URI
uri = "mongodb+srv://kowshikavula14:Smileysmiley183@cluster0.prsfy7f.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'grocery_store' database
    db = client.grocery_store

    # Get reference to 'products' collection
    products_collection = db.products

    # Define the filter to update the product with the given ObjectId
    filter_query = {"_id": ObjectId("65d6404928558977256a9d4a")}

    # Define the update operation to increase the price of the product by 10
    update_operation = {"$inc": {"price": 2}}

    # Print the original document
    pprint.pprint(products_collection.find_one(filter_query))

    # Update the document with the specified operation
    result = products_collection.update_one(filter_query, update_operation)

    # Print the number of documents updated
    print("Documents updated: " + str(result.modified_count))

    # Print the updated document
    pprint.pprint(products_collection.find_one(filter_query))

except Exception as e:
    # Print any exceptions that occur
    print(e)

finally:
    # Close the MongoClient to release resources
    client.close()

