from flask import Flask, render_template, request
import requests
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('action1') == 'VALUE1':
            target = "http://192.168.72.128:5000/change_time"
            requests.get(target)

    return render_template('time.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
