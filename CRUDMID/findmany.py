from pymongo import MongoClient
from pymongo.server_api import ServerApi
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

    # Define the filter to find products with price greater than 10
    filter_query = {"price": {"$gt": 10}}

    # Find products that match the filter
    cursor = products_collection.find(filter_query)

    # Initialize a counter to keep track of the number of documents found
    num_docs = 0

    # Iterate over the cursor to print each document and increment the counter
    for document in cursor:
        num_docs += 1
        pprint.pprint(document)
        print()

    print("# of documents found: " + str(num_docs))

except Exception as e:
    # Print any exceptions that occur
    print(e)

finally:
    # Close the MongoClient to release resources
    client.close()
