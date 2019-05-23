# This is an auto-generated Django model module.
# Jeg har sat "primary_key=True" på alle modellers "id" felt
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` linews if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models


class Afstemningstype(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Afstemningstype'


class AktørAktørRolle(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    rolle = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AktørAktørRolle'


class Aktørtype(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Aktørtype'


class DokumentAktørRolle(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    rolle = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DokumentAktørRolle'


class Dokumentkategori(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    kategori = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dokumentkategori'


class Dokumentstatus(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dokumentstatus'


class Dokumenttype(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dokumenttype'


class Emneordstype(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Emneordstype'


class Kollonebeskrivelse(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    beskrivelse = models.TextField(blank=True, null=True)
    entitetnavn = models.TextField(blank=True, null=True)
    kollonenavn = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'KolloneBeskrivelse'


class SagAktørRolle(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    rolle = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SagAktørRolle'


class SagDokumentRolle(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    rolle = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SagDokumentRolle'


class Sagskategori(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    kategori = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sagskategori'


class Sagsstatus(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sagsstatus'


class SagstrinAktørRolle(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    rolle = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SagstrinAktørRolle'


class Sagstype(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sagstype'


class Sagstrinsstatus(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sagstrinsstatus'


class Sagstrinstype(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sagstrinstype'


class Periode(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    kode = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    slutdato = models.TextField(blank=True, null=True)
    startdato = models.TextField(blank=True, null=True)
    titel = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Periode'


class Mødestatus(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Mødestatus'


class Mødetype(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Mødetype'


class Møde(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    dagsordenurl = models.TextField(blank=True, null=True)
    dato = models.TextField(blank=True, null=True)
    lokale = models.TextField(blank=True, null=True)
    nummer = models.TextField(blank=True, null=True)
    offentlighedskode = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    periodeid = models.ForeignKey(Periode, db_column='periodeid', on_delete=models.DO_NOTHING)
    starttidsbemærkning = models.TextField(blank=True, null=True)
    statusid = models.ForeignKey(Mødestatus, db_column='statusid', on_delete=models.DO_NOTHING)
    titel = models.TextField(blank=True, null=True)
    typeid = models.ForeignKey(Mødetype, db_column='typeid', on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Møde'


class Sag(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    afgørelse = models.TextField(blank=True, null=True)
    afgørelsesdato = models.TextField(blank=True, null=True)
    afgørelsesresultatkode = models.TextField(blank=True, null=True)
    afstemningskonklusion = models.TextField(blank=True, null=True)
    baggrundsmateriale = models.TextField(blank=True, null=True)
    begrundelse = models.TextField(blank=True, null=True)
    deltundersagid = models.ForeignKey('self', related_name='deltundersag', db_column='deltundersagid', on_delete=models.DO_NOTHING)
    fremsatundersagid = models.ForeignKey('self', related_name='fremsatundersag', db_column='fremsatundersagid', on_delete=models.DO_NOTHING)
    kategoriid = models.ForeignKey(Sagskategori, db_column='kategoriid', on_delete=models.DO_NOTHING)
    lovnummer = models.TextField(blank=True, null=True)
    lovnummerdato = models.TextField(blank=True, null=True)
    nummer = models.TextField(blank=True, null=True)
    nummernumerisk = models.TextField(blank=True, null=True)
    nummerpostfix = models.TextField(blank=True, null=True)
    nummerprefix = models.TextField(blank=True, null=True)
    offentlighedskode = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    paragraf = models.TextField(blank=True, null=True)
    paragrafnummer = models.TextField(blank=True, null=True)  # This field type is a guess.
    periodeid = models.ForeignKey(Periode, db_column='periodeid', on_delete=models.DO_NOTHING)
    resume = models.TextField(blank=True, null=True)
    retsinformationsurl = models.TextField(blank=True, null=True)
    rådsmødedato = models.TextField(blank=True, null=True)
    statsbudgetsag = models.BooleanField(blank=True, null=True)
    statusid = models.ForeignKey(Sagsstatus, db_column='statusid', on_delete=models.DO_NOTHING)
    titel = models.TextField(blank=True, null=True)
    titelkort = models.TextField(blank=True, null=True)
    typeid = models.ForeignKey(Sagstype, db_column='typeid', on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Sag'


class Sagstrin(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    dato = models.TextField(blank=True, null=True)
    folketingstidende = models.TextField(blank=True, null=True)
    folketingstidendesidenummer = models.TextField(blank=True, null=True)
    folketingstidendeurl = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    sagid = models.ForeignKey(Sag, db_column='sagid', on_delete=models.DO_NOTHING)
    statusid = models.ForeignKey(Sagstrinsstatus, db_column='statusid', on_delete=models.DO_NOTHING)
    titel = models.TextField(blank=True, null=True)
    typeid = models.ForeignKey(Sagstrinstype, db_column='typeid', on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Sagstrin'


class Afstemning(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    kommentar = models.TextField(blank=True, null=True)
    konklusion = models.TextField(blank=True, null=True)
    mødeid = models.ForeignKey(Møde, db_column='mødeid', on_delete=models.DO_NOTHING)
    nummer = models.BigIntegerField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    sagstrinid = models.ForeignKey(Sagstrin, db_column='sagstrinid', on_delete=models.DO_NOTHING)
    typeid = models.ForeignKey(Afstemningstype, db_column='typeid', on_delete=models.DO_NOTHING)
    vedtaget = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Afstemning'


#HMM Aktstykke er vist ikke helt implementeret op oda.ft.dk
class Aktstykke(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    afgørelse = models.TextField(blank=True, null=True)
    afgørelsesdato = models.TextField(blank=True, null=True)
    afgørelsesresultatkode = models.TextField(blank=True, null=True)
    afstemningskonklusion = models.TextField(blank=True, null=True)
    baggrundsmateriale = models.TextField(blank=True, null=True)
    begrundelse = models.TextField(blank=True, null=True)
    deltundersagid = models.TextField(blank=True, null=True)  # This field type is a guess.
    fremsatundersagid = models.TextField(blank=True, null=True)
    kategoriid = models.BigIntegerField(blank=True, null=True)
    lovnummer = models.TextField(blank=True, null=True)
    lovnummerdato = models.TextField(blank=True, null=True)
    nummer = models.TextField(blank=True, null=True)
    nummernumerisk = models.TextField(blank=True, null=True)
    nummerpostfix = models.TextField(blank=True, null=True)
    nummerprefix = models.TextField(blank=True, null=True)
    offentlighedskode = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    paragraf = models.TextField(blank=True, null=True)
    paragrafnummer = models.TextField(blank=True, null=True)
    periodeid = models.BigIntegerField(blank=True, null=True)
    resume = models.TextField(blank=True, null=True)
    retsinformationsurl = models.TextField(blank=True, null=True)
    rådsmødedato = models.TextField(blank=True, null=True)
    statsbudgetsag = models.BooleanField(blank=True, null=True)
    statusid = models.BigIntegerField(blank=True, null=True)
    titel = models.TextField(blank=True, null=True)
    titelkort = models.TextField(blank=True, null=True)
    typeid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Aktstykke'


class Aktør(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    biografi = models.TextField(blank=True, null=True)
    efternavn = models.TextField(blank=True, null=True)
    fornavn = models.TextField(blank=True, null=True)
    gruppenavnkort = models.TextField(blank=True, null=True)
    navn = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    periodeid = models.ForeignKey(Periode, db_column='periodeid', on_delete=models.DO_NOTHING)
    slutdato = models.TextField(blank=True, null=True)
    startdato = models.TextField(blank=True, null=True)
    typeid = models.ForeignKey(Aktørtype, db_column='typeid', on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Aktør'


class AktørAktør(models.Model):
    fraaktørid = models.ForeignKey(Aktør, related_name='fraaktør', db_column='fraaktørid', on_delete=models.DO_NOTHING)
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    rolleid = models.ForeignKey(AktørAktørRolle, db_column='rolleid', on_delete=models.DO_NOTHING)
    slutdato = models.TextField(blank=True, null=True)
    startdato = models.TextField(blank=True, null=True)
    tilaktørid = models.ForeignKey(Aktør, related_name='tilaktør', db_column='tilaktørid', on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'AktørAktør'


## hmm den her er vist heller ikke linket op på oda.ft.dk
class Almdel(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    afgørelse = models.TextField(blank=True, null=True)
    afgørelsesdato = models.TextField(blank=True, null=True)
    afgørelsesresultatkode = models.TextField(blank=True, null=True)
    afstemningskonklusion = models.TextField(blank=True, null=True)
    baggrundsmateriale = models.TextField(blank=True, null=True)
    begrundelse = models.TextField(blank=True, null=True)
    deltundersagid = models.TextField(blank=True, null=True)
    fremsatundersagid = models.TextField(blank=True, null=True)
    kategoriid = models.TextField(blank=True, null=True)
    lovnummer = models.TextField(blank=True, null=True)
    lovnummerdato = models.TextField(blank=True, null=True)
    nummer = models.TextField(blank=True, null=True)
    nummernumerisk = models.TextField(blank=True, null=True)
    nummerpostfix = models.TextField(blank=True, null=True)
    nummerprefix = models.TextField(blank=True, null=True)
    offentlighedskode = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    paragraf = models.TextField(blank=True, null=True)
    paragrafnummer = models.TextField(blank=True, null=True)
    periodeid = models.BigIntegerField(blank=True, null=True)
    resume = models.TextField(blank=True, null=True)
    retsinformationsurl = models.TextField(blank=True, null=True)
    rådsmødedato = models.TextField(blank=True, null=True)
    statsbudgetsag = models.BooleanField(blank=True, null=True)
    statusid = models.BigIntegerField(blank=True, null=True)
    titel = models.TextField(blank=True, null=True)
    titelkort = models.TextField(blank=True, null=True)
    typeid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Almdel'


class Dagsordenspunkt(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    forhandling = models.TextField(blank=True, null=True)
    forhandlingskode = models.TextField(blank=True, null=True)
    kommentar = models.TextField(blank=True, null=True)
    kørebemærkning = models.TextField(blank=True, null=True)
    mødeid = models.ForeignKey(Møde, db_column='mødeid', on_delete=models.DO_NOTHING)
    nummer = models.TextField(blank=True, null=True)
    offentlighedskode = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    sagstrinid = models.ForeignKey(Sagstrin, db_column='sagstrinid', on_delete=models.DO_NOTHING)
    superid = models.TextField(blank=True, null=True)  # This field type is a guess.
    titel = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dagsordenspunkt'


class Dokument(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    dagsordenudgavenummer = models.TextField(blank=True, null=True)
    dato = models.TextField(blank=True, null=True)
    frigivelsesdato = models.TextField(blank=True, null=True)
    grundnotatstatus = models.TextField(blank=True, null=True)
    kategoriid = models.ForeignKey(Dokumentkategori, db_column='kategoriid', on_delete=models.DO_NOTHING)
    modtagelsesdato = models.TextField(blank=True, null=True)
    offentlighedskode = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    paragraf = models.TextField(blank=True, null=True)
    paragrafnummer = models.TextField(blank=True, null=True)
    procedurenummer = models.TextField(blank=True, null=True)
    spørgsmålsid = models.ForeignKey('self', db_column='spørgsmålsid', on_delete=models.DO_NOTHING)
    spørgsmålsordlyd = models.TextField(blank=True, null=True)
    spørgsmålstitel = models.TextField(blank=True, null=True)
    statusid = models.ForeignKey(Dokumentstatus, db_column='statusid', on_delete=models.DO_NOTHING)
    titel = models.TextField(blank=True, null=True)
    typeid = models.ForeignKey(Dokumenttype, db_column='typeid', on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Dokument'


class Dagsordenspunktdokument(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    dagsordenspunktid = models.ForeignKey(Dagsordenspunkt, db_column='dagsordenspunktid', on_delete=models.DO_NOTHING)
    dokumentid = models.ForeignKey(Dokument, db_column='dokumentid', on_delete=models.DO_NOTHING)
    note = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DagsordenspunktDokument'


class Dagsordenspunktsag(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    dagsordenspunktid = models.ForeignKey(Dagsordenspunkt, db_column='dagsordenspunktid', on_delete=models.DO_NOTHING)
    opdateringsdato = models.TextField(blank=True, null=True)
    sagid = models.ForeignKey(Sag, db_column='sagid', on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'DagsordenspunktSag'

### hmm måske er de alle sammen "sag"...men hvorfor så ikke bare gøre dem til sager med en sagstype?
class Debat(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    afgørelse = models.TextField(blank=True, null=True)
    afgørelsesdato = models.TextField(blank=True, null=True)
    afgørelsesresultatkode = models.TextField(blank=True, null=True)
    afstemningskonklusion = models.TextField(blank=True, null=True)
    baggrundsmateriale = models.TextField(blank=True, null=True)
    begrundelse = models.TextField(blank=True, null=True)
    deltundersagid = models.TextField(blank=True, null=True)
    fremsatundersagid = models.TextField(blank=True, null=True)
    kategoriid = models.TextField(blank=True, null=True)  # This field type is a guess.
    lovnummer = models.TextField(blank=True, null=True)
    lovnummerdato = models.TextField(blank=True, null=True)
    nummer = models.TextField(blank=True, null=True)
    nummernumerisk = models.TextField(blank=True, null=True)
    nummerpostfix = models.TextField(blank=True, null=True)
    nummerprefix = models.TextField(blank=True, null=True)
    offentlighedskode = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    paragraf = models.TextField(blank=True, null=True)
    paragrafnummer = models.TextField(blank=True, null=True)
    periodeid = models.BigIntegerField(blank=True, null=True)
    resume = models.TextField(blank=True, null=True)
    retsinformationsurl = models.TextField(blank=True, null=True)
    rådsmødedato = models.TextField(blank=True, null=True)
    statsbudgetsag = models.BooleanField(blank=True, null=True)
    statusid = models.BigIntegerField(blank=True, null=True)
    titel = models.TextField(blank=True, null=True)
    titelkort = models.TextField(blank=True, null=True)
    typeid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Debat'


class Dokumentaktør(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    aktørid = models.ForeignKey(Aktør, db_column='aktørid', on_delete=models.DO_NOTHING)
    dokumentid = models.ForeignKey(Dokument, db_column='dokumentid', on_delete=models.DO_NOTHING)
    opdateringsdato = models.TextField(blank=True, null=True)
    rolleid = models.ForeignKey(DokumentAktørRolle, db_column='rolleid', on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'DokumentAktør'


class Emneord(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    emneord = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    typeid = models.ForeignKey(Emneordstype, db_column='typeid', on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Emneord'


class Emneordsag(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    emneordid = models.ForeignKey(Emneord, db_column='emneordid', on_delete=models.DO_NOTHING)
    opdateringsdato = models.TextField(blank=True, null=True)
    sagid = models.ForeignKey(Sag, db_column='sagid', on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'EmneordSag'


class MødeAktør(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    aktørid = models.ForeignKey(Aktør, db_column='aktørid', on_delete=models.DO_NOTHING)
    mødeid = models.ForeignKey(Møde, db_column='mødeid', on_delete=models.DO_NOTHING)
    opdateringsdato = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MødeAktør'


class Omtryk(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    begrundelse = models.TextField(blank=True, null=True)
    dato = models.TextField(blank=True, null=True)
    dokumentid = models.ForeignKey(Dokument, db_column='dokumentid', on_delete=models.DO_NOTHING)
    opdateringsdato = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Omtryk'


class Sagaktør(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    aktørid = models.ForeignKey(Aktør, db_column='aktørid', on_delete=models.DO_NOTHING)
    opdateringsdato = models.TextField(blank=True, null=True)
    rolleid = models.ForeignKey(SagAktørRolle, db_column='rolleid', on_delete=models.DO_NOTHING)
    sagid = models.ForeignKey(Sag, db_column='sagid', on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'SagAktør'


class SagstrinAktør(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    aktørid = models.ForeignKey(Aktør, db_column='sagid', on_delete=models.DO_NOTHING)
    opdateringsdato = models.TextField(blank=True, null=True)
    rolleid = models.ForeignKey(SagstrinAktørRolle, db_column='sagid', on_delete=models.DO_NOTHING)
    sagstrinid = models.ForeignKey(Sagstrin, db_column='sagid', on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'SagstrinAktør'


class Sagstrindokument(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    dokumentid = models.ForeignKey(Dokument, db_column='dokumentid', on_delete=models.DO_NOTHING)
    opdateringsdato = models.TextField(blank=True, null=True)
    sagstrinid = models.ForeignKey(Sagstrin, db_column='sagstrinid', on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'SagstrinDokument'


class Stemme(models.Model):
    id = models.BigIntegerField(blank=True, null=True, primary_key=True)
    afstemningid = models.ForeignKey(Afstemning, db_column='afstemningid', on_delete=models.DO_NOTHING)
    aktørid = models.ForeignKey(Aktør, db_column='aktørid', on_delete=models.DO_NOTHING)
    opdateringsdato = models.TextField(blank=True, null=True)
    typeid = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Stemme'
