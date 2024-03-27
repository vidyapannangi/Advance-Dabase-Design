# Import necessary modules
from bson.objectid import ObjectId
from flask import Flask, render_template, request, redirect, url_for
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Flask app initialization
app = Flask(__name__)

# MongoDB connection URI
uri = "mongodb+srv://vidyapannangi:nRvO4hP602uJJyj0@cluster0.6woaqse.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Specify the database and collection
db = client['recipe_book']
recipes_collection = db['recipes']

# Flask routes
@app.route('/')
def index():
    recipes = recipes_collection.find()
    return render_template('index.html', recipes=recipes)

@app.route('/new_recipe', methods=['GET', 'POST'])
def new_recipe():
    if request.method == 'POST':
        recipe_data = {
            'title': request.form['title'],
            'ingredients': request.form['ingredients'],
            'instructions': request.form['instructions']
        }
        recipes_collection.insert_one(recipe_data)
        return redirect(url_for('index'))
    return render_template('new_recipe.html')

@app.route('/update_recipe/<recipe_id>', methods=['GET', 'POST'])
def update_recipe(recipe_id):
    recipe = recipes_collection.find_one({'_id': ObjectId(recipe_id)})
    if request.method == 'POST':
        new_recipe_data = {
            'title': request.form['title'],
            'ingredients': request.form['ingredients'],
            'instructions': request.form['instructions']
        }
        recipes_collection.update_one({'_id': ObjectId(recipe_id)}, {'$set': new_recipe_data})
        return redirect(url_for('index'))
    return render_template('update_recipe.html', recipe=recipe)

@app.route('/delete_recipe/<recipe_id>', methods=['POST'])
def delete_recipe(recipe_id):
    if request.method == 'POST':
        recipes_collection.delete_one({'_id': ObjectId(recipe_id)})
        return redirect(url_for('index'))
    else:
        return "Method Not Allowed", 405

@app.route('/find_recipe', methods=['GET'])
def find_recipe():
    search_query = request.args.get('search_query', '')  # Get the search query from the form
    # Perform a search query in the database
    recipes = recipes_collection.find({'title': {'$regex': search_query, '$options': 'i'}})
    return render_template('index.html', recipes=recipes)

if __name__ == "__main__":
    app.run(debug=True)
