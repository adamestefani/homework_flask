from flask import Flask, request

#start the app
app = Flask(__name__)

#rest to receive and return the same text
@app.route('/text/<string:text>', methods=['GET'])
def return_text(text):
    return text


#run app
if __name__ == "__main__":
    app.run(debug=True)


