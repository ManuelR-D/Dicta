import subprocess
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, "src")

SERVERS = [
    {
        "name": "transcription_server",
        "script": "whisperx_api.py",
        "port": 5000
    },
    {
        "name": "voice_recognition_server",
        "script": "voice_api.py",
        "port": 8000
    },
    {
        "name": "voice_sentiment_server",
        "script": "voice_sentiment_api.py",
        "port": 5002
    }
]

processes = []

try:
    for server in SERVERS:
        server_dir = os.path.join(SRC_DIR, server["name"])
        script_path = os.path.join(server_dir, server["script"])
        print(f"Starting {server['name']} on port {server['port']}...")
        proc = subprocess.Popen(
            [sys.executable, script_path],
            cwd=server_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        processes.append(proc)

    print("All servers started. Press Ctrl+C to stop.")

    # Wait for all processes
    for proc in processes:
        proc.wait()

except KeyboardInterrupt:
    print("\nShutting down servers...")
    for proc in processes:
        proc.terminate()
    print("All servers stopped.")