from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

# Now hello.py is accessible on http://localhost:5000
# Verify it is
