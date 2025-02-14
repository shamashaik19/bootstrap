from flask import Flask, jsonify
import random

app = Flask(__name__)

def generate_otp():
    return ''.join(random.choice('0123456789') for _ in range(6))

@app.route('/otp', methods=['GET'])
def get_otp():
    otp = generate_otp()
    return jsonify({"OTP": otp})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Runs on port 5000

