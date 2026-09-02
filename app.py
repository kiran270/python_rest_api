from flask import Flask, jsonify, request
from datetime import datetime
import os

app = Flask(__name__)

# In-memory storage for demo
items = []

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'message': 'Welcome to Flask REST API',
        'version': '1.0.0',
        'timestamp': datetime.utcnow().isoformat()
    })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat()
    }), 200

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify({
        'items': items,
        'count': len(items)
    }), 200

@app.route('/api/items', methods=['POST'])
def create_item():
    data = request.get_json()
    
    if not data or 'name' not in data:
        return jsonify({'error': 'Name is required'}), 400
    
    item = {
        'id': len(items) + 1,
        'name': data['name'],
        'description': data.get('description', ''),
        'created_at': datetime.utcnow().isoformat()
    }
    
    items.append(item)
    return jsonify(item), 201

@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    
    if item is None:
        return jsonify({'error': 'Item not found'}), 404
    
    return jsonify(item), 200

@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    item = next((item for item in items if item['id'] == item_id), None)
    
    if item is None:
        return jsonify({'error': 'Item not found'}), 404
    
    item['name'] = data.get('name', item['name'])
    item['description'] = data.get('description', item['description'])
    item['updated_at'] = datetime.utcnow().isoformat()
    
    return jsonify(item), 200

@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    item = next((item for item in items if item['id'] == item_id), None)
    
    if item is None:
        return jsonify({'error': 'Item not found'}), 404
    
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'message': 'Item deleted successfully'}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
