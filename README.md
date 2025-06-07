# Dicta

Para iniciar los servicios ejecutar `python start.py`. Este script inicia 3 servicios.

```
python .\start.py
Starting transcription_server on port 5000...
Starting voice_recognition_server on port 8000...
Starting voice_sentiment_server on port 5002...
All servers started. Press Ctrl+C to stop.
```

Para testear los servicios iniciados ejecutar `python test.py`. Este script hace requests a los servicios en localhost.

```
python .\test.py
Testing transcription_server...
/api/health: 200 {'service': 'whisperx-api', 'status': 'ok', 'version': '1.0.0'}
/api/transcribe: 200 {'segments': [{'end': '00:00:29,017', 'id': 1, 'speaker': 'Natalia Natalia', 'start': '00:00:28,956', 'text': 'Hola Mundo'}, {'end': '00:00:31,017', 'id': 2, 'speaker': 'Piru', 'start': '00:00:30,956', 'text': 'Mundo Hola'}]}
----------------------------------------
Testing voice_recognition_server...
/api/healthcheck: 200 {'service': 'voice-recognition-api', 'status': 'ok', 'version': '1.0.0'}
/api/voice/register: 200 {'details': {'label': 'Natalia Natalia', 'name': 'Natalia Natalia'}, 'message': 'Voice registered successfully', 'status': 'success'}
/api/voice/identify: 200 {'matches_found': 1, 'results': [{'id': 1, 'label': 'Natalia Natalia', 'name': 'Natalia Natalia', 'similarity_score': 0}], 'status': 'success'}
----------------------------------------
Testing voice_sentiment_server...
/api/health: 200 {'service': 'voice-sentiment-api', 'status': 'ok', 'version': '1.0.0'}
/api/predict-sentiment: 200 {'emotion': 'Happy', 'probabilities': 0.3}
```