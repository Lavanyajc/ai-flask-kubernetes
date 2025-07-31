from flask import Flask, request, jsonify
import numpy as np
import pickle

model = pickle.load(open("model.pkl", "rb"))

app = Flask(__name__)

@app.route('/')
def home():
    return "AI Model is live!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        features = np.array(data['features']).reshape(1, -1)  # Ensure correct shape
        prediction = model.predict(features)
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
