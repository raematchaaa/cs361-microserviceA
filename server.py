# Pet Training Tips Microservice

# User Story #1: Retrieve Training Tips by Category
# User Story #2: Handle Empty Tip Category Gracefully
# User Story #3: View My Favorite Tips
from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# Load training tips data
with open('training_tips.json', 'r') as f:
    tips_data = json.load(f)

favorite_file = 'favorite_tips.json'

def load_favorites():
    if os.path.exists(favorite_file):
        with open(favorite_file, 'r') as f:
            return json.load(f)
        
    else:
        return {}


@app.route('/tips', methods=['GET'])
def get_tips():
    category = request.args.get('category')
    if not category:
        return jsonify({"error": "Missing 'category' parameter"}), 400
    
    tips = tips_data.get(category.lower())
    if tips:
        return jsonify({"category": category, "tips": tips}), 200
    else:
        return jsonify({"message": f"No training tips available for '{category}' at the moment. Try another category!"}), 200


@app.route('/favorites', methods=['GET'])
def get_favorites():
    username = request.args.get('username')
    if not username:
        return jsonify({"error": "Missing 'username' parameter"}), 400
    
    favorites = load_favorites()
    if username not in favorites:
        return jsonify({"error": f"Username '{username}' not found."}), 404
    
    user_favorites = favorites[username]
    return jsonify({"username": username, "favorites": user_favorites}), 200


if __name__ == '__main__':
    app.run(debug=True)