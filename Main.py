from flask import Flask, render_template, request, redirect, url_for, session, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

USERNAME = 'admin'
PASSWORD = 'password'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            flash('Invalid Credentials. Please try again.')  
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/uw_eigen_idee')
def uw_eigen_idee():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('uw_eigen_idee.html')

@app.route('/duurzaamheid')
def duurzaamheid():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('duurzaamheid.html')

@app.route('/economie')
def economie():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('economie.html')

@app.route('/jeugd')
def jeugd():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('jeugd.html')

@app.route('/kunst_en_cultuur')
def kunst_en_cultuur():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('kunst_en_cultuur.html')

@app.route('/onderhoud_of_verbetering_woning')
def onderhoud_of_verbetering_woning():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('onderhoud_of_verbetering_woning.html')

@app.route('/onderwijs')
def onderwijs():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('onderwijs.html')

@app.route('/samenleven_welzijn_en_basisvaardigheden')
def samenleven_welzijn_en_basisvaardigheden():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('samenleven_welzijn_en_basisvaardigheden.html')

@app.route('/sport_en_recreatie_natuur_en_milieu')
def sport_en_recreatie_natuur_en_milieu():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('sport_en_recreatie_natuur_en_milieu.html')

@app.route('/vieringen_herdenkingen_en_stimulering_woningcorporaties')
def vieringen_herdenkingen_en_stimulering_woningcorporaties():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('vieringen_herdenkingen_en_stimulering_woningcorporaties.html')

@app.route('/volksgezondheid')
def volksgezondheid():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('volksgezondheid.html')

@app.route('/werk_en_inkomen')
def werk_en_inkomen():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('werk_en_inkomen.html')

if __name__ == '__main__':
    app.run(debug=True)
