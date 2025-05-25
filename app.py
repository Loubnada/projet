from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reserver', methods=['POST'])
def reserver():
    nom = request.form['nom']
    service = request.form['service']
    date = request.form['date']
    heure = request.form['heure']
    
    # Ici tu peux enregistrer la réservation dans une base de données ou un fichier
    print(f"Réservation reçue : {nom}, {service}, {date}, {heure}")
    
    return render_template('confirmation.html', nom=nom, service=service, date=date, heure=heure)

if __name__ == '__main__':
    app.run(debug=True)
