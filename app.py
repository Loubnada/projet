from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        date = request.form.get('date')
        time = request.form.get('time')
        # Ici tu peux ajouter une logique pour envoyer un e-mail
        return render_template('index.html', success=True, name=name, email=email, date=date, time=time)
    return render_template('index.html', success=False)

if __name__ == '__main__':
    app.run(debug=True)
