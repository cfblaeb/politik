# Politik
Brug af åben data fra folketinget til at få lidt indsigt i hvem de er og hvad de laver (http://oda.ft.dk)

# Detaljer
Projektet består af hhv en scraper der henter data fra oda.ft.dk via deres odata interface (not a fan btw) og gemmer det som sql.
Default er bare i en sqlite database, men det kan nemt ændres til hvad som helst sqlalchemy kan snakke med og sqlite er nok den langsomste af dem alle (men kræver ingen setup)
SQL dataene tilgår jeg så via Django ORM. Kunne også bare havde været rå SQL, men på tidspunktet da dette startede var jeg meget glad for django ORM så det bliver det ved med at være.

# Instruktioner
1) Tested på Python 3.7.3 på ubuntu 19.04 men det virker sikkert også må det meste andet.
2) Installer pakker med 
   ```bash
   pip install -r requirements.txt
   ```
3) Så skal der hentes data
   ```bash
   python odatascraper.py
   ```
4) Dette opretter en lokal sqlite database kaldet "politik.sqlite"
5) Start jupyterlab
   ```bash
   jupyter lab
   ```
6) Dette starter jupyter lab i browseren hvor du så kan åbne analyse.ipynb
# Nyheder
* 21/5/2019 Så er der valg igen. Jeg opdatere med seneste pakker og data. 