# app.py
from flask import Flask, request
from prometheus_client import Counter, Histogram, generate_latest

app = Flask(__name__)

REQUEST_COUNT = Counter('demo_requests_total', 'Total HTTP requests', ['method', 'endpoint'])
ERROR_COUNT = Counter('demo_errors_total', 'Total errors')
REQUEST_LATENCY = Histogram('demo_request_latency_seconds', 'Request latency')

@app.route('/')
@REQUEST_LATENCY.time()
def index():
    REQUEST_COUNT.labels(request.method, '/').inc()
    return "Hello, World!"

@app.route('/fail')
@REQUEST_LATENCY.time()
def fail():
    REQUEST_COUNT.labels(request.method, '/fail').inc()
    ERROR_COUNT.inc()
    return "Error!", 500

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
