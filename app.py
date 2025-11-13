from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy-Daten (werden später aus DB kommen)
boxen = [
    {'id': 1, 'ausgabe': '2025-11-10', 'rueckgabe': '2025-11-15', 'status': 'ausgeliehen', 'email': 'max@uni.de'},
    {'id': 2, 'ausgabe': '2025-11-09', 'rueckgabe': '2025-11-12', 'status': 'überfällig', 'email': 'lisa@uni.de'}
]

@app.route('/')
def home():
    return render_template('index.html', boxen=boxen, title="Übersicht")

@app.route('/new-loan')
def new_loan():
    return render_template('new_loan.html', title="Neue Leihe")

@app.route('/save-loan', methods=['POST'])
def save_loan():
    box_id = request.form['box_id']
    email = request.form['email']
    ausgabe = request.form['ausgabe']
    rueckgabe = request.form['rueckgabe']
    boxen.append({
        'id': box_id,
        'ausgabe': ausgabe,
        'rueckgabe': rueckgabe,
        'status': 'ausgeliehen',
        'email': email
    })
    return redirect(url_for('home'))

@app.route('/return/<int:box_id>')
def return_box(box_id):
    return render_template('return.html', box_id=box_id, title="Rückgabe")

if __name__ == '__main__':
    app.run(debug=True)