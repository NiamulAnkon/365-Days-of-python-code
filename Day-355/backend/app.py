from flask import *

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])

def calculate():
    data = request.get_json()
    operation = data['operation']
    num1 = data['num1']
    num2 = data['num2']
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return jsonify({'error': 'Division by zero!'}), 400
        result = num1 / num2
    else:
        return jsonify({'error': 'Invalid operation!'}), 400

    return jsonify({'result': result})

if __name__ == "__main__":
    app.run(debug=True)