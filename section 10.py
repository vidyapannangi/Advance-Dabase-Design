from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb+srv://vidyapannangi:test123@cluster0.6woaqse.mongodb.net/?retryWrites=true&w=majority')

# Access a specific database
db = client['mydatabase']

# Access a specific collection
collection = db['mycollection']


# Create Operation
def create_document(document):
    """
    Creates a new document in the collection.
    """
    result = collection.insert_one(document)
    return result.inserted_id


# Read Operation
def read_documents(query={}):
    """
    Retrieves documents from the collection based on the provided query.
    If no query is provided, retrieves all documents.
    """
    return collection.find(query)


# Update Operation
def update_document(query, update):
    """
    Updates a document in the collection based on the provided query.
    """
    result = collection.update_one(query, {"$set": update})
    return result.modified_count


# Delete Operation
def delete_document(query):
    """
    Deletes a document from the collection based on the provided query.
    """
    result = collection.delete_one(query)
    return result.deleted_count


# Example Usage
if __name__ == "__main__":
    # Create Operation Example
    new_document = {"name": "John", "age": 30}
    created_id = create_document(new_document)
    print(f"Document created with ID: {created_id}")

    # Read Operation Example
    documents = read_documents({"age": {"$gt": 25}})
    print("Documents with age greater than 25:")
    for doc in documents:
        print(doc)

    # Update Operation Example
    update_query = {"name": "John"}
    update_data = {"age": 35}
    updated_count = update_document(update_query, update_data)
    print(f"Number of documents updated: {updated_count}")

    # Delete Operation Example
    delete_query = {"name": "John"}
    deleted_count = delete_document(delete_query)
    print(f"Number of documents deleted: {deleted_count}")
