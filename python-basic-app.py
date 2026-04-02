from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Ashir app for assignment 07. Attempt 09 - Build 08. Deploying in Minikube at MacOS with Webhook."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)