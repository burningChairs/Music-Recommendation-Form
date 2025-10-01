from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/shoegaze")
def shoegaze():
    return render_template("page1.html")

@app.route("/metal")
def metal():
    return render_template("page2.html")

@app.route("/emo")
def emo():
    return render_template("page3.html")

if __name__ == "__main__":
    app.run(debug=True)
