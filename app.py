from flask import Flask

app = Flask(name)

@app.route("/")
def home():
    return "Prediction Market MVP funcionando"

if name == "main":
    app.run(debug=True)
