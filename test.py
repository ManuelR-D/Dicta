import requests

BASE_URLS = {
    "transcription": "http://localhost:5000",
    "voice_recognition": "http://localhost:8000",
    "voice_sentiment": "http://localhost:5002"
}

def test_transcription_server():
    print("Testing transcription_server...")
    # Health
    r = requests.get(f"{BASE_URLS['transcription']}/api/health")
    print("/api/health:", r.status_code, r.json())
    # Transcribe (dummy payload)
    r = requests.post(f"{BASE_URLS['transcription']}/api/transcribe", json={})
    print("/api/transcribe:", r.status_code, r.json())

def test_voice_recognition_server():
    print("Testing voice_recognition_server...")
    # Health
    r = requests.get(f"{BASE_URLS['voice_recognition']}/api/healthcheck")
    print("/api/healthcheck:", r.status_code, r.json())
    # Register (dummy payload)
    r = requests.post(f"{BASE_URLS['voice_recognition']}/api/voice/register", json={})
    print("/api/voice/register:", r.status_code, r.json())
    # Identify (dummy payload)
    r = requests.post(f"{BASE_URLS['voice_recognition']}/api/voice/identify", json={})
    print("/api/voice/identify:", r.status_code, r.json())

def test_voice_sentiment_server():
    print("Testing voice_sentiment_server...")
    # Health
    r = requests.get(f"{BASE_URLS['voice_sentiment']}/api/health")
    print("/api/health:", r.status_code, r.json())
    # Predict sentiment (dummy payload)
    r = requests.post(f"{BASE_URLS['voice_sentiment']}/api/predict-sentiment", json={})
    print("/api/predict-sentiment:", r.status_code, r.json())

if __name__ == "__main__":
    test_transcription_server()
    print("-" * 40)
    test_voice_recognition_server()
    print("-" * 40)
    test_voice_sentiment_server()