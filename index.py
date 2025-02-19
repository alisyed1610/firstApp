from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello')
def hello():
    return jsonify({"message": "Hello from Flask on Vercel Deployed by Ali Abdullah Syed!"})

# For local testing
if __name__ == '__main__':
    app.run(debug=True)