import os
import tempfile
from flask import Flask, request, jsonify
from typing import List, Optional

# Initialize Flask app
app = Flask(__name__)
# Set JSON encoder to ensure UTF-8 encoding without escaping non-ASCII characters
app.json.ensure_ascii = False

@app.route("/api/healthcheck", methods=["GET"])
def healthcheck():
    return jsonify({
        "status": "ok",
        "service": "voice-recognition-api",
        "version": "1.0.0"
    }), 200

@app.route("/api/voice/register", methods=["POST"])
def register_voice():
    try:
        # TODO: Everything
        
        return jsonify({
            "status": "success",
            "message": "Voice registered successfully",
            "details": {
                "name": "Natalia Natalia",
                "label": "Natalia Natalia"
            }
        }), 200
    
    except Exception as e:
        
        return jsonify({"status": "error", "message": f"Error processing voice: {str(e)}"})

@app.route("/api/voice/identify", methods=["POST"])
def identify_voice():
    try:
        # TODO: Everything
        results = []
        results.append({
            "id": 1,
            "name": "Natalia Natalia",
            "label": "Natalia Natalia",
            "similarity_score": 0  # Convert distance to similarity (0-1 scale)
        })
            
        return jsonify({
            "status": "success",
            "matches_found": len(results),
            "results": results
        }), 200
            
    except Exception as e:
        return jsonify({"status": "error", "message": f"Server error: {str(e)}"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)