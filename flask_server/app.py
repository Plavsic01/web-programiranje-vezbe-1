from crypt import methods
from flask import Flask, redirect,render_template, request

app = Flask(__name__)

studenti = [
    {"broj_indeksa":"1234/123456","ime":"Andrej","prezime":"Plavsic","prosecna_ocena":"8"},
    {"broj_indeksa":"1234/654321","ime":"Olivera","prezime":"Plavsic","prosecna_ocena":"10"},
    {"broj_indeksa":"1234/123321","ime":"Vanja","prezime":"Plavsic","prosecna_ocena":"9"},
    {"broj_indeksa":"2020/123456","ime":"Bosko","prezime":"Plavsic","prosecna_ocena":"7"}
]

@app.route("/",methods=["GET","POST"])
def home():
    return render_template("index.html",studenti=studenti)



@app.route("/dodaj-studenta",methods=["GET","POST"])    
def dodaj_studenta():
    if request.method == "POST":
        student = dict(request.form)
        studenti.append(student)
        return redirect("/")
    return render_template("form_dodavanje.html")


@app.route("/brisanje-studenta/<int:id>")
def brisanje_studenta(id):
    id = id - 1
    studenti.pop(id)
    return redirect("/")


@app.route("/izmena-studenta/<int:id>",methods=["GET","POST"])
def izmena_studenta(id):
    index = id - 1
    student = studenti[index]
    if request.method == "GET":    
        return render_template("form_za_izmenu.html",student=student,id=id)
    else: 
        studenti[index] = dict(request.form)       
        return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)


