from flask import Flask, request
from datetime import datetime
import os
from datetime import datetime, timedelta


app = Flask(__name__)
time = 0


@app.route("/", methods=["GET"])
def home():
    print(time)
    return """
<meta http-equiv="refresh" content="1" /> 
Hello World!<br>The current time is {}.""".format(datetime.strftime(datetime.now() - timedelta(seconds=time*5), "%d %B %Y %X"))

@app.route("/change_time", methods=["GET"])
def change_time():
    if request.method == 'GET':
        global time
        time += 1
        return "f"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
