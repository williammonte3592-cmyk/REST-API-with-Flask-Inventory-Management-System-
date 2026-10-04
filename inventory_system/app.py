from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Database
items = []

@app.route('/')
def home():
    return jsonify({"message": "Inventory API is running!"})

@app.route('/inventory', methods=['GET'])
def get_all():
    return jsonify(items)

@app.route('/inventory/<int:id>', methods=['GET'])
def get_one(id):
    for item in items:
        if item['id'] == id:
            return jsonify(item)
    return jsonify({"error": "Not found"}), 404

@app.route('/inventory', methods=['POST'])
def create():
    data = request.json
    new_id = len(items) + 1
    new_item = {
        "id": new_id,
        "name": data["name"],
        "price": data.get("price", 0),
        "stock": data.get("stock", 0)
    }
    items.append(new_item)
    return jsonify(new_item), 201

@app.route('/inventory/<int:id>', methods=['PATCH'])
def update(id):
    for item in items:
        if item['id'] == id:
            data = request.json
            if "price" in data:
                item["price"] = data["price"]
            if "stock" in data:
                item["stock"] = data["stock"]
            return jsonify(item)
    return jsonify({"error": "Not found"}), 404

@app.route('/inventory/<int:id>', methods=['DELETE'])
def delete(id):
    global items
    items = [item for item in items if item['id'] != id]
    return jsonify({"message": "Deleted"}), 200

@app.route('/fetch/<barcode>', methods=['GET'])
def fetch_from_api(barcode):
    try:
        url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if data.get('status') == 1:
            product = data['product']
            return jsonify({
                'name': product.get('product_name', 'Unknown'),
                'brand': product.get('brands', 'Unknown')
            })
        else:
            return jsonify({'error': 'Product not found'}), 404
    except Exception as e:
        return jsonify({'error': 'API error', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5555)