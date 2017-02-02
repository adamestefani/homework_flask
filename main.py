from flask import Flask

#start the app
app = Flask(__name__)

#first page
@app.route('/main')
def index():
    return "hello world"

if __name__ == "__main__":
    app.run(debug=True)
