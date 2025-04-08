from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello, my name is Hamza"})

@app.route('/bio')
def biodata():
    return jsonify({
        "age": 20,
        "university": "UIT University",
        "city": "Karachi"
    })

@app.route('/study')
def studydetail():
    return jsonify({
        "name": "UIT University",
        "degree": "BS(CS)"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
