from flask import Flask
from pyngrok import ngrok
from threading import Thread

# Launch Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to House Price Prediction API!"

# Run Flask app
def run():
    app.run(port=6000)

# Start the app in the background
Thread(target=run).start()

# Expose the app with ngrok
public_url = ngrok.connect("6000").public_url
print(f"🔗 Public URL: {public_url}")
