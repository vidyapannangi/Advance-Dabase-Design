from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb+srv://vidyapannangi:test123@cluster0.6woaqse.mongodb.net/?retryWrites=true&w=majority')

# Access a specific database
db = client['mydatabase']
