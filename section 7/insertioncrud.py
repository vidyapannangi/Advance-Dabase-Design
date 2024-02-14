from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime
from pprint import pprint

uri = "mongodb+srv://vidyapannangi:test123@cluster0.6woaqse.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'bank' database
    db = client.bank

    # Get reference to 'accounts' collection
    accounts_collection = db.accounts

    # Inserting multiple accounts
    new_accounts = [
        {
            "account_holder": "Vidya",
            "account_id": "MDB123456789",
            "account_type": "savings",
            "balance": 10000,
            "last_updated": datetime.datetime.utcnow(),
        },
        {
            "account_holder": "Gayathri",
            "account_id": "MDB987654321",
            "account_type": "checking",
            "balance": 25000,
            "last_updated": datetime.datetime.utcnow(),
        }
    ]

    # Write an expression that inserts the 'new_accounts' documents into the 'accounts' collection.
    result = accounts_collection.insert_many(new_accounts)

    inserted_ids = result.inserted_ids
    pprint(f"_ids of inserted documents: {inserted_ids}")

except Exception as e:
    print(e)
finally:
    client.close()
