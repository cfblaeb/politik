# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Afstemning(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    kommentar = models.TextField(blank=True, null=True)
    konklusion = models.TextField(blank=True, null=True)
    mødeid = models.BigIntegerField(blank=True, null=True)
    nummer = models.BigIntegerField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    sagstrinid = models.FloatField(blank=True, null=True)
    typeid = models.BigIntegerField(blank=True, null=True)
    vedtaget = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'Afstemning'


class Afstemningstype(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Afstemningstype'


class Aktstykke(models.Model):

    class Meta:
        managed = False
        db_table = 'Aktstykke'


class Aktr(models.Model):
    biografi = models.TextField(blank=True, null=True)
    efternavn = models.TextField(blank=True, null=True)
    fornavn = models.TextField(blank=True, null=True)
    gruppenavnkort = models.TextField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    navn = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    periodeid = models.FloatField(blank=True, null=True)
    slutdato = models.TextField(blank=True, null=True)
    startdato = models.TextField(blank=True, null=True)
    typeid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Aktør'


class Aktraktr(models.Model):
    fraaktørid = models.BigIntegerField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    rolleid = models.BigIntegerField(blank=True, null=True)
    slutdato = models.TextField(blank=True, null=True)
    startdato = models.TextField(blank=True, null=True)
    tilaktørid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AktørAktør'


class Aktraktrrolle(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    rolle = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AktørAktørRolle'


class Aktrtype(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Aktørtype'


class Almdel(models.Model):

    class Meta:
        managed = False
        db_table = 'Almdel'


class Dagsordenspunkt(models.Model):
    forhandling = models.TextField(blank=True, null=True)
    forhandlingskode = models.TextField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    kommentar = models.TextField(blank=True, null=True)
    kørebemærkning = models.TextField(blank=True, null=True)
    mødeid = models.BigIntegerField(blank=True, null=True)
    nummer = models.TextField(blank=True, null=True)
    offentlighedskode = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    sagstrinid = models.FloatField(blank=True, null=True)
    superid = models.FloatField(blank=True, null=True)
    titel = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dagsordenspunkt'


class Dagsordenspunktdokument(models.Model):
    dagsordenspunktid = models.BigIntegerField(blank=True, null=True)
    dokumentid = models.BigIntegerField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DagsordenspunktDokument'


class Dagsordenspunktsag(models.Model):
    dagsordenspunktid = models.BigIntegerField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    sagid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DagsordenspunktSag'


class Debat(models.Model):

    class Meta:
        managed = False
        db_table = 'Debat'


class Dokument(models.Model):
    dagsordenudgavenummer = models.TextField(blank=True, null=True)
    dato = models.TextField(blank=True, null=True)
    frigivelsesdato = models.TextField(blank=True, null=True)
    grundnotatstatus = models.TextField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    kategoriid = models.BigIntegerField(blank=True, null=True)
    modtagelsesdato = models.TextField(blank=True, null=True)
    offentlighedskode = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    paragraf = models.TextField(blank=True, null=True)
    paragrafnummer = models.TextField(blank=True, null=True)
    procedurenummer = models.TextField(blank=True, null=True)
    spørgsmålsid = models.FloatField(blank=True, null=True)
    spørgsmålsordlyd = models.TextField(blank=True, null=True)
    spørgsmålstitel = models.TextField(blank=True, null=True)
    statusid = models.BigIntegerField(blank=True, null=True)
    titel = models.TextField(blank=True, null=True)
    typeid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dokument'


class Dokumentaktr(models.Model):
    aktørid = models.BigIntegerField(blank=True, null=True)
    dokumentid = models.BigIntegerField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    rolleid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DokumentAktør'


class Dokumentaktrrolle(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    rolle = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DokumentAktørRolle'


class Dokumentation(models.Model):

    class Meta:
        managed = False
        db_table = 'Dokumentation'


class Dokumentkategori(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    kategori = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dokumentkategori'


class Dokumentstatus(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dokumentstatus'


class Dokumenttype(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dokumenttype'


class Eusag(models.Model):

    class Meta:
        managed = False
        db_table = 'EUsag'


class Emneord(models.Model):
    emneord = models.TextField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    typeid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Emneord'


class Emneorddokument(models.Model):

    class Meta:
        managed = False
        db_table = 'EmneordDokument'


class Emneordsag(models.Model):
    emneordid = models.BigIntegerField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    sagid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EmneordSag'


class Emneordstype(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Emneordstype'


class Fil(models.Model):
    dokumentid = models.BigIntegerField(blank=True, null=True)
    dokumentoffentlighedskode = models.TextField(blank=True, null=True)
    dokumentstatus = models.TextField(blank=True, null=True)
    filurl = models.TextField(blank=True, null=True)
    format = models.TextField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    titel = models.TextField(blank=True, null=True)
    variantkode = models.TextField(blank=True, null=True)
    versionsdato = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Fil'


class Forslag(models.Model):

    class Meta:
        managed = False
        db_table = 'Forslag'


class Kollonebeskrivelse(models.Model):
    beskrivelse = models.TextField(blank=True, null=True)
    feltnavn = models.TextField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    tabelnavn = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'KolloneBeskrivelse'


class Mde(models.Model):
    dagsordenurl = models.TextField(blank=True, null=True)
    dato = models.TextField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    lokale = models.TextField(blank=True, null=True)
    mødestatusid = models.BigIntegerField(blank=True, null=True)
    mødetypeid = models.BigIntegerField(blank=True, null=True)
    nummer = models.TextField(blank=True, null=True)
    offentlighedskode = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    periodeid = models.BigIntegerField(blank=True, null=True)
    starttidsbemærkning = models.TextField(blank=True, null=True)
    titel = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Møde'


class Mdeaktr(models.Model):
    aktørid = models.BigIntegerField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    mødeid = models.BigIntegerField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MødeAktør'


class Mdestatus(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Mødestatus'


class Mdetype(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Mødetype'


class Nyhed(models.Model):

    class Meta:
        managed = False
        db_table = 'Nyhed'


class Omtryk(models.Model):
    begrundelse = models.TextField(blank=True, null=True)
    dato = models.TextField(blank=True, null=True)
    dokumentid = models.BigIntegerField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Omtryk'


class Periode(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    kode = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    slutdato = models.TextField(blank=True, null=True)
    startdato = models.TextField(blank=True, null=True)
    titel = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Periode'


class Sag(models.Model):
    afgørelse = models.TextField(blank=True, null=True)
    afgørelsesdato = models.TextField(blank=True, null=True)
    afgørelsesresultatkode = models.TextField(blank=True, null=True)
    afstemningskonklusion = models.TextField(blank=True, null=True)
    baggrundsmateriale = models.TextField(blank=True, null=True)
    begrundelse = models.TextField(blank=True, null=True)
    deltundersagid = models.FloatField(blank=True, null=True)
    fremsatundersagid = models.FloatField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    kategoriid = models.FloatField(blank=True, null=True)
    lovnummer = models.TextField(blank=True, null=True)
    lovnummerdato = models.TextField(blank=True, null=True)
    nummer = models.TextField(blank=True, null=True)
    nummernumerisk = models.TextField(blank=True, null=True)
    nummerpostfix = models.TextField(blank=True, null=True)
    nummerprefix = models.TextField(blank=True, null=True)
    offentlighedskode = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    paragraf = models.TextField(blank=True, null=True)
    paragrafnummer = models.FloatField(blank=True, null=True)
    periodeid = models.BigIntegerField(blank=True, null=True)
    resume = models.TextField(blank=True, null=True)
    retsinformationsurl = models.TextField(blank=True, null=True)
    rådsmødedato = models.TextField(blank=True, null=True)
    statsbudgetsag = models.NullBooleanField()
    statusid = models.BigIntegerField(blank=True, null=True)
    titel = models.TextField(blank=True, null=True)
    titelkort = models.TextField(blank=True, null=True)
    typeid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sag'


class Sagaktr(models.Model):
    aktørid = models.BigIntegerField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    rolleid = models.BigIntegerField(blank=True, null=True)
    sagid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SagAktør'


class Sagaktrrolle(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    rolle = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SagAktørRolle'


class Sagdokument(models.Model):
    bilagsnummer = models.TextField(blank=True, null=True)
    dokumentid = models.BigIntegerField(blank=True, null=True)
    frigivelsesdato = models.TextField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    rolleid = models.BigIntegerField(blank=True, null=True)
    sagid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SagDokument'


class Sagdokumentrolle(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    rolle = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SagDokumentRolle'


class Sagskategori(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    kategori = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sagskategori'


class Sagsstatus(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sagsstatus'


class Sagstrin(models.Model):
    dato = models.TextField(blank=True, null=True)
    folketingstidende = models.TextField(blank=True, null=True)
    folketingstidendesidenummer = models.TextField(blank=True, null=True)
    folketingstidendeurl = models.TextField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    sagid = models.BigIntegerField(blank=True, null=True)
    statusid = models.BigIntegerField(blank=True, null=True)
    titel = models.TextField(blank=True, null=True)
    typeid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sagstrin'


class Sagstrinaktr(models.Model):
    aktørid = models.BigIntegerField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    rolleid = models.BigIntegerField(blank=True, null=True)
    sagstrinid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SagstrinAktør'


class Sagstrinaktrrolle(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    rolle = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SagstrinAktørRolle'


class Sagstrindokument(models.Model):

    class Meta:
        managed = False
        db_table = 'SagstrinDokument'


class Sagstrinsagstrin(models.Model):
    andetsagstrinid = models.BigIntegerField(blank=True, null=True)
    førstesagstrinid = models.BigIntegerField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SagstrinSagstrin'


class Sagstrintale(models.Model):

    class Meta:
        managed = False
        db_table = 'SagstrinTale'


class Sagstrinsstatus(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sagstrinsstatus'


class Sagstrinstype(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sagstrinstype'


class Sagstype(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sagstype'


class Stemme(models.Model):
    afstemningid = models.BigIntegerField(blank=True, null=True)
    aktørid = models.BigIntegerField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    typeid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Stemme'


class Tabelbeskrivelse(models.Model):
    beskrivelse = models.TextField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    tabelnavn = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TabelBeskrivelse'
