from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Handwerker Leads API"

@app.route('/api/test')
def test():
    return {"status": "online"}

@app.route('/api/lead', methods=['POST'])
def capture_lead():
    # Später implementieren
    return {"status": "success"}

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
