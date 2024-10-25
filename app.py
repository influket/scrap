from flask import Flask, render_template, jsonify
import time

app = Flask(__name__)

# A variable to track progress
progress = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start-scraping')
def start_scraping():
    global progress
    progress = 0

    # Simulate a scraping process
    for i in range(1, 101):
        time.sleep(0.1)  # Simulate time taken for scraping
        progress = i

    return jsonify(status="completed")

@app.route('/progress')
def get_progress():
    return jsonify(progress=progress)

if __name__ == '__main__':
    app.run(debug=True)
