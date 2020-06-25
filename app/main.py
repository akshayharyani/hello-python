from flask import Flask, render_template
import os
import pwd

app = Flask(__name__)

@app.route("/")
def hello():
    name = get_username()
    return render_template("index.html", user_name=name)


def get_username():
    return pwd.getpwuid( os.getuid() )[ 0 ]

if __name__ == "__main__":
    app.run(host='0.0.0.0')
