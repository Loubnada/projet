from flask import Flask, render_template, request

app = Flask(__name__)

# Page d'accueil avec le formulaire
@app.route('/')
def home():
    return render_template('index.html')

# Page pour traiter la réservation
@app.route('/reserver', methods=['POST'])
def reserver():
    nom = request.form['nom']
    service = request.form['service']
    date = request.form['date']
    heure = request.form['heure']
    return render_template('confirmation.html', nom=nom, service=service, date=date, heure=heure)

if __name__ == '__main__':
    app.run(debug=True)
