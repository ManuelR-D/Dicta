import os
import sys
import tempfile
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)
# Set JSON encoder to ensure UTF-8 encoding without escaping non-ASCII characters
app.json.ensure_ascii = False


@app.route('/api/predict-sentiment', methods=['POST'])
def predict_sentiment():
    try:
        # TODO: Everything
        return jsonify({
            "emotion": "Happy",
            "probabilities": 0.3
        }), 200
    
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "ok", 
        "version": "1.0.0", 
        "service": "voice-sentiment-api"
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)  # Using port 5002 to avoid conflicts with other services