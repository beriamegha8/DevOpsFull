from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.route('/')
def home():
    pod_name = os.getenv('HOSTNAME', 'Not running in Kubernetes')
    container_id = socket.gethostname()
    port = os.getenv('PORT', '5000')
    
    return jsonify({
        'message': 'Jenkins is running',
        'pod_name': pod_name,
        'container_id': container_id,
        'port': port
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', '5000'))
    app.run(host='0.0.0.0', port=port)