from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/dojo")
def coding():
    return "<h1>Dojo!</h1>"

@app.route("/say/<name>")
def say(name):
    return "Hi " + name

# @app.route("/repeat/<num>/hello")
# def repeat(num):
#     num = int(num)
#     return (num* "hello ")

@app.route("/repeat/<num>/<name>")
def repeat(num, name):

    return int(num) * (name+"\n")


# if __name__=="__main__":
    
    
app.run(debug=True)