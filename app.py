from flask import Flask

### WSGI Application
app = Flask(__name__)

@app.route('/') # Decorater
def welcome():
    return "This is Joseph Mourinho. I have 2 UCL. One is with PortoFC."


@app.route('/epl') # Decorater
def epl():
    return "I have also won 1 EPL."


if __name__ == '__main__':
    app.run(debug=True)