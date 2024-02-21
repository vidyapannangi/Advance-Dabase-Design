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

    # Filter
    select_products = {"category": "Dairy"}

    # Update operation
    set_field = {"$set": {"discount": 0.1}}

    # Write an expression that updates multiple products with a discount for fruits category.
    result = products_collection.update_many(select_products, set_field)

    # Print updated document
    print("Documents matched: " + str(result.matched_count))
    print("Documents updated: " + str(result.modified_count))
    pprint.pprint(products_collection.find_one(select_products))

except Exception as e:
    print(e)

finally:
    client.close()
