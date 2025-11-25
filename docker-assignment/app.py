from flask import Flask, jsonify
import logging
import time

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/health')
def health_check():
    logger.info("Health check endpoint called")
    return jsonify({"status": "healthy", "timestamp": time.time()})

@app.route('/GET')
def get_endpoint():
    logger.info("GET endpoint called")
    return jsonify({
        "message": "Successfully connected to GET endpoint",
        "service": "Dockerized Python App",
        "version": "1.0"
    })

@app.route('/')
def home():
    logger.info("Home endpoint called")
    return jsonify({"message": "Welcome to Dockerized Python Application"})

if __name__ == '__main__':
    logger.info("Starting Flask application on port 8080")
    app.run(host='0.0.0.0', port=8080, debug=False)