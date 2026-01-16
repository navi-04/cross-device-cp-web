from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

# File to store clipboard items
DATA_FILE = 'clipboard_data.json'

def load_data():
    """Load clipboard data from file"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_data(data):
    """Save clipboard data to file"""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@app.route('/')
def index():
    """Render main page"""
    return render_template('index.html')

@app.route('/api/items', methods=['GET'])
def get_items():
    """Get all clipboard items"""
    data = load_data()
    return jsonify(data)

@app.route('/api/items', methods=['POST'])
def add_item():
    """Add new clipboard item"""
    content = request.json.get('content', '').strip()
    if not content:
        return jsonify({'error': 'Content cannot be empty'}), 400
    
    data = load_data()
    new_item = {
        'id': datetime.now().timestamp(),
        'content': content,
        'timestamp': datetime.now().isoformat()
    }
    data.insert(0, new_item)  # Add to beginning
    save_data(data)
    
    return jsonify(new_item), 201

@app.route('/api/items/<float:item_id>', methods=['DELETE'])
def delete_item(item_id):
    """Delete clipboard item"""
    data = load_data()
    data = [item for item in data if item['id'] != item_id]
    save_data(data)
    
    return jsonify({'success': True})

if __name__ == '__main__':
    # Run on all network interfaces (0.0.0.0) to allow access from other devices
    app.run(host='0.0.0.0', port=5000, debug=True)
