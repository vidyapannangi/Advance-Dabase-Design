from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import pprint

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

    # Filter by ObjectId
    document_to_delete = {"_id": ObjectId("65da2a5b44169cd034887097")}

    # Search for document before delete
    print("Searching for target document before delete: ")
    pprint.pprint(products_collection.find_one(document_to_delete))

    # Write an expression that deletes the target product.
    result = products_collection.delete_one(document_to_delete)

    # Search for document after delete
    print("Searching for target document after delete: ")
    pprint.pprint(products_collection.find_one(document_to_delete))

    # Print the number of documents deleted
    print("Documents deleted: " + str(result.deleted_count))

except Exception as e:
    print(e)

finally:
    # Close the MongoClient to release resources
    client.close()
