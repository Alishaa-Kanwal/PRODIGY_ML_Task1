from flask import Flask, render_template, request
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler, PolynomialFeatures

app = Flask(__name__)

# Load the trained model
model = joblib.load('house_price_predictor.pkl')

# Define the feature list used during training
features = ['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms', 'Avg. Area Number of Bedrooms', 'Area Population']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect data from the form
        data = {
            'Avg. Area Income': float(request.form['AvgAreaIncome']),
            'Avg. Area House Age': float(request.form['AvgAreaHouseAge']),
            'Avg. Area Number of Rooms': float(request.form['AvgAreaRooms']),
            'Avg. Area Number of Bedrooms': float(request.form['AvgAreaBedrooms']),
            'Area Population': float(request.form['AreaPopulation'])
        }

        # Create a DataFrame for the input
        input_data = pd.DataFrame([data])

        # Use the model to make a prediction
        prediction = model.predict(input_data)[0]
        return render_template('result.html', price=f"${prediction:,.2f}")

    except Exception as e:
        return f"Error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)
