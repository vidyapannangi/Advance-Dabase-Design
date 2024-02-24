from pymongo import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import pprint

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

    # Define the filter to find a specific product
    filter_query = {
        "_id": ObjectId("65da2a5b44169cd034887097")
    }

    # Find one product that matches the filter
    result = products_collection.find_one(filter_query)

    # Print the result
    pprint.pprint(result)

except Exception as e:
    # Print any exceptions that occur
    print(e)
finally:
    # Close the MongoClient to release resources
    client.close()
    # Close the MongoClient to release resources
    client.close()
