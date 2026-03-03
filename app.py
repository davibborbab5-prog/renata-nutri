from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("landing.html")

@app.route("/submit", methods=["POST"])
def submit():
    nome = request.form.get("nome")
    email = request.form.get("email")
    whatsapp = request.form.get("whatsapp")
    objetivo = request.form.get("objetivo")

    print("Novo lead:")
    print(nome, email, whatsapp, objetivo)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
    