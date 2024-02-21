from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import pprint

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

    # Filter by some condition (for example, products with price less than 2000)
    documents_to_delete = {"price": {"$lt": 2000}}

    # Search for sample document before delete
    print("Searching for sample target document before delete: ")
    pprint.pprint(products_collection.find_one(documents_to_delete))

    # Write an expression that deletes the target documents.
    result = products_collection.delete_many(documents_to_delete)

    # Search for sample document after delete
    print("Searching for sample target document after delete: ")
    pprint.pprint(products_collection.find_one(documents_to_delete))

    # Print the number of documents deleted
    print("Documents deleted: " + str(result.deleted_count))

except Exception as e:
    print(e)

finally:
    # Close the MongoClient to release resources
    client.close()
