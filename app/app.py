from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the model
model_path = "/app/model/model.pkl"
model = joblib.load(model_path)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        if not data or 'features' not in data:
            return jsonify({'error': 'Invalid input! Expected {"features": [...]}'})
        
        features = data['features']
        prediction = model.predict([features])
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
