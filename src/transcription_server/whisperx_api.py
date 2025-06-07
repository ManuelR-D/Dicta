import os
import sys
from flask import Flask, request, jsonify, send_from_directory

@app.route('/api/transcribe', methods=['POST'])
def transcribe():
    try:
        # TODO: Everything
        return jsonify({"segments": [{
            "id": 1,
            "start": "00:00:28,956",
            "end": "00:00:29,017",
            "speaker": "Natalia Natalia",
            "text": "Hola Mundo"
        },{
            "id": 2,
            "start": "00:00:30,956",
            "end": "00:00:31,017",
            "speaker": "Piru",
            "text": "Mundo Hola"
        },]})
    
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok", "version": "1.0.0", "service": "whisperx-api"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)