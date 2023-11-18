# Podcast Tracker

Proiect Individual 2023.

#### 1. Titlul proiectului: Podcast Tracker

#### 2. De ce ați ales acest proiect?

● Temă de actualitate.

● Interes față de podcasturi.

● Motivație proprie. Dorința de a utiliza o astfel de aplicație.

● Motivație proprie. Dorința de a învăța și utiliza tehnologiile necesare pentru realizarea
proiectului (Python, Django, folosire API).

● Potențiali utilizatori: Persoanele care ascultă podcasturi.

#### 3. Descrierea proiectului și a rezultatelor propuse a fi realizate?

● Descriere generală:

Podcasturile sunt o formă de conținut audio și, uneori, video. Scopul proiectului,
Podcast tracker, este de a oferi utilizatorilor o metodă eficientă de centralizare și salvare a
episoadelor de podcast urmărite. Utilizatorii vor putea salva episoadele urmărite, dar și
episoadele pe care doresc să le urmărească. De asemenea, pot lasa note și comentarii
publice pentru fiecare episod.

● Rezultatul propus: Un site web intuitiv și ușor de utilizat care oferă aceste
funcționalități.

Proiectul constă în folosirea unor limbaje de programare de nivel înalt, API și baza de
date pentru a crea un site web. Pe acest site web, prin intermediul unui API, vom furniza
diferite show-uri de tip podcast și episoadele aferente acestor show-uri, acestea vor fi
manipulate și salvate în baza de date. Utilizatorii, prin intermediul autentificării, vor putea
folosi diverse funcționalități ale platformei specificate mai jos.

##### Cerințe funcționale ale proiectului:

- Autentificare. Utilizatorii trebuie să se poată autentifica folosind adrese de email,
  nume de utilizatori și parole. Aplicația trebuie să ofere opțiunea de recuperare a parolei.

- Introducerea de conținut printr-un API. Se va folosi un API care furnizează baza
  de date cu emisiuni de tip podcast și episoade aferente emisiunilor pentru utilizatori. Aceste
  informații vor fi publice pentru fiecare utilizator, fie că acesta este logat sau nu. Se va folosi
  API-ul gratuit limitat oferit de Spotify sau API-ul gratuit limitat oferit de Podchaser.

- Convertirea datelor primite prin API pentru vizualizare de către utilizator.
  Pentru ca toate datele să fie vizibile într-un format ușor de înțeles și intuitiv de folosit,
  aplicația va garanta conversia datelor primite prin API într-un format bine structurat. Se vor
  folosi diverse șabloane din framework-ul Django pentru structurarea datelor în backend, iar
  pentru partea de frontend se va folosi HTML și JavaScript pentru o vizualizare modernă a
  fiecărui show/episod (fiecare episod va conține o poză de tip thumbnail, iar lângă vor fi
  afișate date relevante precum: Show, Număr episod, Nume episod, Invitat, Descriere,
  Durată, Dată apariție).

- Sistem rating. Pentru fiecare episod disponibil pe platformă, fiecare utilizator logat
  va putea lăsa o notă de la 1 până la 5 stele. Aceste rating-uri vor fi calculate, iar media de
  rating a fiecărui episod va fi vizibilă.

- Listă de urmărire. Pentru fiecare episod disponibil pe platformă, fiecare utilizator
  logat va putea salva episodul într-o listă. Platforma va oferi două tipuri de liste deja
  construite în spatele aplicației pentru fiecare utilizator, episoade salvate ca fiind vizionate și
  episoade salvate pentru vizionare ulterioară. În urma salvării unor episoade în liste,
  utilizatorii pot vizualiza episoadele salvate.

- Comentarii publice. Pentru fiecare episod disponibil pe platforma, fiecare utilizator
  logat va putea adăuga comentarii publice. Aceste comentarii pot fi vizualizate de orice
  utilizator fie ca acesta este logat sau nu.

##### Cerințe non-funcționale ale proiectului:

- Performanță. Aplicația trebuie să fie rapidă și să ofere răspuns utilizatorilor,
  indiferent de volumul de date.

- Securitate. Datele utilizatorilor trebuie să fie securizate și protejate împotriva
  accesului neautorizat.

- Ușurință de utilizare. Interfața utilizator trebuie să fie intuitivă și ușor de înțeles
  pentru toți utilizatorii.

- Corectitudine date. Aplicația trebuie să conțină doar informații reale despre
  episoadele oferite.

##### Indicatorii de performanță propuși:

Indicatori de performanta esentiali:

- Adaugarea printr-un API a unui număr minim de show-uri de tip podcast. Număr
  minim propus: 5 show-uri.

- Adaugarea printr-un API a unui număr minim de episoade ale show-urilor deja
  existente. Număr minim propus: 10 episoade/show.

- Implicarea utilizatorilor. Un număr minim de utilizatori activi pentru a asigura
  funcționarea corectă a functionalitatilor. Număr minim utilizatori propus: 10.
  Alți indicatori de performanta non-esentiali:

- Urmărirea ratei de folosire a funcționalităților. Se monitorizează modul în care
  utilizatorii utilizează funcționalitățile oferite.

- Urmărirea conținutului oferit. Măsoară numărul de show-uri și episoade disponibile,
  numărul de comentarii și notele.

##### Arhitectura

Arhitectura este de tip client-server. Clientul este reprezentat de către un browser, iar
partea de server va fi implementată folosind framework-ul Django.

#### 4. Ce tehnologii veți utiliza în cadrul proiectului?

- Limbaje de programare: Python, HTML, JavaScript

- Web framework: Django

- Bază de date relațională SQL

- Funcții/rutine/open source:

- API pentru furnizarea show-urilor/episoadelor

- Funcții, rutine Django: models, views, templates, authentication, REST framework

- Git pentru controlul versiunii
