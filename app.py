from flask import Flask, render_template, send_from_directory
import requests
import threading
import time

app = Flask(__name__)


# Periodic GET requests
def periodic_get_request(url, interval=870):
    return
    while True:
        try:
            response = requests.get(url)
            print(f"Request to {url} completed with status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error with request: {e}")
        time.sleep(interval)

# Start periodic GET requests in a separate thread
url_to_request = "https://accessivytutoring.com/background-task"
thread = threading.Thread(target=periodic_get_request, args=(url_to_request,))
thread.daemon = True
thread.start()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/background-task')
def background_task():
    return send_from_directory(app.root_path, "background_task.txt")


if __name__ == '__main__':
    app.run(debug=True)
