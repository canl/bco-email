from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

def validate_trader_id(trader_id):
    # Validate trader ID: at least 10 alphanumeric characters
    return bool(re.match(r'^[a-zA-Z0-9]{10,}$', trader_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/novation-service', methods=['POST'])
def novation_service():
    data = request.json
    
    # Validate trader IDs
    for entry in data['entries']:
        if not validate_trader_id(entry['trade_id']):
            return jsonify({
                'success': False,
                'message': f'Invalid trade ID: {entry["trade_id"]}. Must be at least 10 alphanumeric characters.'
            }), 400
    
    # Here you would typically make the actual novation service call
    # For now, we'll just return a success response
    return jsonify({
        'success': True,
        'message': 'Trades successfully novated'
    })

if __name__ == '__main__':
    app.run(debug=True) 