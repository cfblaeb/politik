import requests as rq
import pandas as pd
from sqlalchemy import create_engine


def scrape(table):
    """
    Ved meget lidt om microsofts odata protokol, så i stedet for at prøve at lave en generel odata funktion
    så er det her bare en specifik ft.dk odata scraper.

    :param table: Det table du gerne vil hente
    :return:
    """

    # ft.dk tillader kun at du henter 100 rækker per kald
    # derfor så starte vi med at spørge om hvor mange rækker der er i alt
    totalcount = int(rq.get('http://oda.ft.dk/api/{}'.format(table), params={"$inlinecount": "allpages"}).json()['odata.count'])
    ccount = 0
    print(f"Linjer der skal hentes: {totalcount}")
    # herefter henter vi indtil vi har hentet alt
    while ccount < totalcount:
        r = rq.get(f'http://oda.ft.dk/api/{table}', params={"$skip": ccount})
        for row in r.json()['value']:
            yield row

        ccount += 100
        if ccount % 1000 == 0:
            print(f"Hentet {ccount}/{totalcount}")

#her er NOGEN af de tables der er tilgængelige...et par af dem eksistere vist ikke...
list_of_tables = [
    "Afstemning",
    "Afstemningstype",
    "Aktstykke",
    "Aktør",
    "AktørAktør",
    "AktørAktørRolle",
    "Aktørtype",
    "Almdel",
    "Dagsordenspunkt",
    "DagsordenspunktDokument",
    "DagsordenspunktSag",
    "Debat",
    "Dokument",
    "DokumentAktør",
    "DokumentAktørRolle",
    "Dokumentkategori","Dokumenttype",
    "Dokumentstatus","Emneord",
    "EmneordSag","Emneordstype",
    "KolloneBeskrivelse",
    "TabelBeskrivelse","Møde",
    "MødeAktør",
    "Mødestatus","Mødetype",
    "Nyhed",
    "Omtryk","Periode","Sag",
    "SagAktør","SagAktørRolle",
    "SagDokumentRolle","Sagskategori",
    "Sagsstatus",
    "Sagstrin",
    "SagstrinAktør","SagstrinAktørRolle",
    "SagstrinSagstrin",
    "SagstrinDokument",
    "Sagstrinsstatus",
    "SagstrinTale","Sagstrinstype",
    "Sagstype",
    "Stemme"]

# opret forbindelse til sqlite database
con = create_engine('sqlite:///politik.sqlite')


# hent alle tables
for tab in list_of_tables:
    print(tab)
    try:
        pd.DataFrame.from_dict(scrape(tab)).to_sql(tab, con, index=False, if_exists='replace')
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(e)
        print(f"Fejl ved hentning af {tab}")
