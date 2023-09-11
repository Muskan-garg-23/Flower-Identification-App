from flask import Flask
app=Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
         return "hello"

if __name__== "__main__":
    app.run(debug=True,port=5501)