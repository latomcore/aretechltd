from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Default route
@app.route('/')
def index():
    return render_template('index.html')

# Sample API route 1
@app.route('/api/v1/notify', methods=['POST'])
def process_notify():
    data = request.json
    # Process the notification here
    return jsonify({"status": "200", "message": "Notification received", "data": data})

# Sample API route 2
@app.route('/api/v1/data', methods=['POST'])
def process_data():
    data = request.json
    # Process request data here 
    return jsonify({"status": "200", "message": "Request received", "data": data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
