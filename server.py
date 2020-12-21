# IMPORTURI:
from flask import Flask, render_template, url_for, request, redirect
import csv


# INSTRANTIEREA CLASEI "FLASK()"
# ##  IN CARE "__NAME__ " = "/ __MAIN__":
app = Flask(__name__)
# ## print(__name__)


# RUTA 1 - "HOME":
@app.route('/<string:nume_pagina>')
def pagina_html(nume_pagina):
    return render_template(nume_pagina)


# BAZA DE DATE 1 - "TEXT" -- FUNC. "SCRIE IN FISIER()":
def scrie_in_fisier(date):

    # DESCHIDERE FISIER -- PT. "APPEND":
    with open('database.txt', mode='a') as baza_de_date:

        # VARIABILE PRELUATE:
        email = date['email']
        subiect = date['subiect']
        mesaj = date['mesaj']

        # FUNC. SCRIERE:
        fisier = baza_de_date.write(f'\n{email}, {subiect}, {mesaj}')


# BAZA DE DATE 2 - "EXCEL" -- FUNC. "SCRIE IN FISIER()":
def scrie_in_csv(date):

    # DESCHIDERE FISIER -- PT. "APPEND":
    with open('database.csv', mode='a', newline='') as baza_de_date_excel:

        # VARIABILE PRELUATE:
        email = date['email']
        subiect = date['subiect']
        mesaj = date['mesaj']

        # FUNC. SCRIERE:
        scriitor_csv = csv.writer(
            baza_de_date_excel, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # SCRIERE RAND:
        scriitor_csv.writerow([email, subiect, mesaj])


# RUTA 2 -- "FORMULAR DE TRIMITERE":
@app.route('/formular_de_trimitere', methods=['POST', 'GET'])
def formular_de_trimitere():

    # CONDITIA - DACA EXISTA MET. "POST" IN REQUEST:
    if request.method == 'POST':

        # BLOC GESTIONARE ERORI:
        try:
            # PRELUARE DATE CA DICTIONARE:
            date = request.form.to_dict()

            # APELAREA FUNC.:
            # scrie_in_fisier(date)
            scrie_in_csv(date)

            # IESIRE - REDIRECTIONARE:
            return redirect('thanks.html')

        except:

            # IESIRE:
            return 'Nu a fost salvata in baza de date!'

    else:
        # IESIRE:
        return 'Ceva a fost gresit, incercati dinou!'
