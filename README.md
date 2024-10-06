Descriere
Am implementat o galerie de fotografii pe web. Userii care isi creeaza cont pot
publica fotografii, care sunt vizibile in pagina de home a website-ului.

Frontend
Partea de frontend este implementata cu ajutorul a HTML, CSS, Flask, Jinja2 si
Bootstrap. Toate paginile pornesc de la template-ul base.html, care contine cod
HTML pentru o bara de navigare, prin care utilizatorul poate naviga pe paginile
site-ului. Aceasta bara este de tip collapsible (prin minimizarea ferestrei, se
apare un hamburger menu icon prin care se pot accesa paginile). Un utilizator
neautentificat are acces la urmatoarele pagini:
- Home: pagina principala a siteului, unde sunt afisate, pe categorii, toate
pozele din galerie (pozele apartinand tuturor user-ilor)
- Sign Up: pagina prin care un vizitator al site-ului isi poate crea cont
- Login: pagina prin care un utilizator isi poate introduce credentialele
pentru a se loga
- About Me: pagina care explica pe scurt scopul site-ului
Dupa ce intra in cont, ultilizatorul are acces si la urmatoarele pagini:
- Photo Gallery: pagina in care sunt dispuse fotografiile adaugate de user-ul
logat, afisate sub forma de thumbnail in functie de categorii
- Upload: pagina prin care user-ul poate incarca noi fotografii
- Logout: utilizatorul este intrebat daca doreste sa iasa din cont
Fiecare pagina are un fisier .html aferent, in care este extins fisierul
base.html pentru a obtine efectul dorit pentru fiecare pagina. In paginile
in care sunt afisate fotografiile (Home si Photo Gallery), pentru fiecare
fotografie este afisat un thumbnail. Prin click pe thumbnail, se afiseaza
imagina in format full-size.

Backend
Partea de backend este realizata cu ajutorul Python. Fisierul __init__.py
configureaza o aplicatie Flask si o baza de date SQLite in care sunt stocate
informatii despre useri si fisierele incarcate de acestia. In fisierul main.py
se implementeaza functiile python care permit incarcarea fotografiilor si
afisarea lor in pagina home si in pagina de galerie a fiecarui user. Pentru
fiecare fotografie incarcata, este generat si un thumbnail, care este afisat in
locul fotografiei full-sized. Fisierul auth.py contine implementarea functiilor
care asigura functionalitatile de login/logout si creare de cont (sign up).
Fisierul models.py defineste doua modele in SQLAlchemy pentru retinerea datelor
despre utilizatori si despre fotografii intr-un database. User reprezinta un
utilizator, fiind reprezentat de urmatoarele atribute: id, email, prenume si 
parola (care este retinuta in database sub forma hash). Photo reprezinta o
fotografie adaugata, fiind identificata prin filename, numele dat de user,
categorie, data incarcarii si user_id (id-ul utilizatorului care a incarcat
fotografia).

Docker Containerization
Proiectul contine un Dockerfile prin care se poate construi si rula serverul.
