from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

# Flask example: Bind to ALL interfaces (0.0.0.0)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Replace 5000 with your port