# House Price Prediction using Scikit-learn and Flask

This project is a web application that predicts house prices based on user inputs using a trained machine learning model developed with Scikit-learn and deployed using Flask.

## Features
- Predicts house prices based on features like location, area, number of rooms, etc.
- Uses a pre-trained model saved using `pickle` for efficient loading.
- Provides a user-friendly web interface for data input and prediction display.

## Prerequisites
- Python 3.11+
- Flask
- Scikit-learn
- Pandas
- NumPy
- Pickle
- Ngrok (for exposing the local server to the internet)

## Installation
1. Clone this repository:
   ```bash
   git clone <repository-link>
   cd house-price-prediction
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

4. Expose the application using ngrok:
   ```bash
   ngrok http 5000
   ```

## Usage
1. After starting the Flask server, visit the provided URL (e.g., `http://127.0.0.1:5000`).
2. Enter the required house features in the input fields.
3. Click on the "Predict" button to view the predicted house price.

## Model Details
- The model was trained using Scikit-learn and saved using `pickle` as `model.pkl`.
- The model file is loaded in the Flask application as follows:
  ```python
  import pickle
  with open('model.pkl', 'rb') as file:
      model = pickle.load(file)
  ```

## Handling Outliers
Outliers were treated using:
- **IQR Method:** Identifying values below `Q1 - 1.5*IQR` or above `Q3 + 1.5*IQR`.
- **Winsorization:** Capping extreme values to the 5th and 95th percentiles.
- **Log Transformation:** Applied for skewed distributions.

## Troubleshooting
**Port 5000 Already in Use:**
- Identify and stop the conflicting process:
  ```bash
  lsof -i :5000
  kill -9 <PID>
  ```
- Alternatively, run the app on a different port:
  ```bash
  python app.py --port=8080
  ```

**Ngrok Authentication Error:**
- Ensure you have logged into your ngrok account and your free session isn’t occupied.
- If necessary, end active sessions from the [Ngrok Dashboard](https://dashboard.ngrok.com/agents).

## Future Improvements
- Enhance UI with improved layout and better input validation.
- Add support for additional house features to improve prediction accuracy.
- Implement user authentication for secure access.

## Contact
For questions or suggestions, feel free to reach out at:
- Email: erdnachiket@gmail.com
- GitHub: [nachidixit](https://github.com/nachidixit)

