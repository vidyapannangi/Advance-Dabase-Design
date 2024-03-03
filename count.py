from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import poplib
import datetime
from pprint import pprint

uri = "mongodb+srv://vidyapannangi:test123@cluster0.6woaqse.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'sample_training' database
    db = client.sample_training

    # Get reference to 'zips' collection
    accounts_collection = db.zips

    # inserting one product
    new = [
    { "$count": "total_zips" }
]

    # Write an expression that inserts the 'new_product' document into the 'products' collection.
    #result = accounts_collection.insert_one(new)
    result = list(accounts_collection.aggregate(new))

    #document_id = result.inserted_id
    #pprint(f"_id of inserted document: {document_id}")
    if result:
        print(result)
    else:
        print("No documents in the collection")


except Exception as e:
    print(e)
finally:
    client.close()
