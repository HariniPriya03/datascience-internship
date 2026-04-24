from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

model = joblib.load('model.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.is_json:
        # JSON request (API use case)
        data = request.get_json()
        hours = data.get('hours')
        if hours is None:
            return jsonify({'error': 'Missing "hours" in input'}), 400
        prediction = model.predict(np.array([[hours]]))
        return jsonify({'predicted_score': round(float(prediction[0]), 2)})
    else:
        # Form submission (web UI)
        hours = request.form.get('hours')
        error = None
        predicted_score = None

        try:
            hours_float = float(hours)
            prediction = model.predict(np.array([[hours_float]]))
            predicted_score = round(float(prediction[0]), 2)
        except (ValueError, TypeError):
            error = "Please enter a valid number for hours."

        return render_template('index.html', predicted_score=predicted_score, error=error)

if __name__ == '__main__':
    app.run(debug=True)
