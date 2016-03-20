from django.db import models


class Mødestatus(models.Model):
    id = models.BigIntegerField(primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Mødestatus'


class Mødetype(models.Model):
    id = models.BigIntegerField(primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Mødetype'


class Møde(models.Model):
    id = models.BigIntegerField(primary_key=True)
    dagsordenurl = models.TextField(blank=True, null=True)
    dato = models.TextField(blank=True, null=True)
    lokale = models.TextField(blank=True, null=True)
    mødestatusid = models.ForeignKey(Mødestatus)
    mødetypeid = models.ForeignKey(Mødetype)
    nummer = models.TextField(blank=True, null=True)
    offentlighedskode = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    periodeid = models.ForeignKey(Periode)
    starttidsbemærkning = models.TextField(blank=True, null=True)
    titel = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Møde'


class Afstemningstype(models.Model):
    id = models.BigIntegerField(primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Afstemningstype'


class Afstemning(models.Model):
    id = models.BigIntegerField(primary_key=True)
    kommentar = models.TextField(blank=True, null=True)
    konklusion = models.TextField(blank=True, null=True)
    mødeid = models.ForeignKey(Møde)
    nummer = models.BigIntegerField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    sagstrinid = models.ForeignKey(Sagstrin)
    typeid = models.ForeignKey(Afstemningstype)
    vedtaget = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'Afstemning'


class Aktør(models.Model):
    id = models.BigIntegerField(primary_key=True)
    biografi = models.TextField(blank=True, null=True)
    efternavn = models.TextField(blank=True, null=True)
    fornavn = models.TextField(blank=True, null=True)
    gruppenavnkort = models.TextField(blank=True, null=True)
    navn = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    periodeid = models.ForeignKey(Periode)
    slutdato = models.TextField(blank=True, null=True)
    startdato = models.TextField(blank=True, null=True)
    typeid = models.ForeignKey(Aktørtype)

    class Meta:
        managed = False
        db_table = 'Aktør'


class AktørAktør(models.Model):
    id = models.BigIntegerField(primary_key=True)
    fraaktørid = models.ForeignKey(Aktør)
    opdateringsdato = models.TextField(blank=True, null=True)
    rolleid = models.ForeignKey(AktørAktørRolle)
    slutdato = models.TextField(blank=True, null=True)
    startdato = models.TextField(blank=True, null=True)
    tilaktørid = models.ForeignKey(Aktør)

    class Meta:
        managed = False
        db_table = 'AktørAktør'


class AktørAktørRolle(models.Model):
    id = models.BigIntegerField(primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    rolle = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AktørAktørRolle'


class Aktørtype(models.Model):
    id = models.BigIntegerField(primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Aktørtype'


class Dagsordenspunkt(models.Model):
    id = models.BigIntegerField(primary_key=True)
    forhandling = models.TextField(blank=True, null=True)
    forhandlingskode = models.TextField(blank=True, null=True)
    kommentar = models.TextField(blank=True, null=True)
    kørebemærkning = models.TextField(blank=True, null=True)
    mødeid = models.ForeignKey(Møde)
    nummer = models.TextField(blank=True, null=True)
    offentlighedskode = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    sagstrinid = models.ForeignKey(Sagstrin)
    superid = models.ForeignKey(Super)
    titel = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dagsordenspunkt'


class Dagsordenspunktdokument(models.Model):
    dagsordenspunktid = models.ForeignKey(Dagsordenspunkt)
    dokumentid = models.ForeignKey(Dokument)
    id = models.BigIntegerField(primary_key=True)
    note = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DagsordenspunktDokument'


class Dagsordenspunktsag(models.Model):
    dagsordenspunktid = models.ForeignKey(Dagsordenspunkt)
    id = models.BigIntegerField(primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    sagid = models.ForeignKey(Sag)

    class Meta:
        managed = False
        db_table = 'DagsordenspunktSag'


class Dokument(models.Model):
    id = models.BigIntegerField(primary_key=True)
    dagsordenudgavenummer = models.TextField(blank=True, null=True)
    dato = models.TextField(blank=True, null=True)
    frigivelsesdato = models.TextField(blank=True, null=True)
    grundnotatstatus = models.TextField(blank=True, null=True)
    kategoriid = models.ForeignKey(Kategori)
    modtagelsesdato = models.TextField(blank=True, null=True)
    offentlighedskode = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    paragraf = models.TextField(blank=True, null=True)
    paragrafnummer = models.TextField(blank=True, null=True)
    procedurenummer = models.TextField(blank=True, null=True)
    spørgsmålsid = models.ForeignKey(Spørgsmåls)
    spørgsmålsordlyd = models.TextField(blank=True, null=True)
    spørgsmålstitel = models.TextField(blank=True, null=True)
    statusid = models.ForeignKey(Dokumentstatus)
    titel = models.TextField(blank=True, null=True)
    typeid = models.ForeignKey(Dokumenttype)

    class Meta:
        managed = False
        db_table = 'Dokument'


class DokumentAktør(models.Model):
    id = models.BigIntegerField(primary_key=True)
    aktørid = models.ForeignKey(Aktør)
    dokumentid = models.ForeignKey(Dokument)
    opdateringsdato = models.TextField(blank=True, null=True)
    rolleid = models.ForeignKey(DokumentAktørRolle)

    class Meta:
        managed = False
        db_table = 'DokumentAktør'


class DokumentAktørRolle(models.Model):
    id = models.BigIntegerField(primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    rolle = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DokumentAktørRolle'


class Dokumentkategori(models.Model):
    id = models.BigIntegerField(primary_key=True)
    kategori = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dokumentkategori'


class Dokumentstatus(models.Model):
    id = models.BigIntegerField(primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dokumentstatus'


class Dokumenttype(models.Model):
    id = models.BigIntegerField(primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dokumenttype'


class Emneord(models.Model):
    id = models.BigIntegerField(primary_key=True)
    emneord = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    typeid = models.ForeignKey(Emneordtype)

    class Meta:
        managed = False
        db_table = 'Emneord'


class Emneordsag(models.Model):
    id = models.BigIntegerField(primary_key=True)
    emneordid = models.ForeignKey(Emneord)
    opdateringsdato = models.TextField(blank=True, null=True)
    sagid = models.ForeignKey(Sag)

    class Meta:
        managed = False
        db_table = 'EmneordSag'


class Emneordstype(models.Model):
    id = models.BigIntegerField(primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Emneordstype'


class Fil(models.Model):
    id = models.BigIntegerField(primary_key=True)
    dokumentid = models.ForeignKey(Dokument)
    dokumentoffentlighedskode = models.TextField(blank=True, null=True)
    dokumentstatus = models.TextField(blank=True, null=True)
    filurl = models.TextField(blank=True, null=True)
    format = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    titel = models.TextField(blank=True, null=True)
    variantkode = models.TextField(blank=True, null=True)
    versionsdato = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Fil'


class Kollonebeskrivelse(models.Model):
    id = models.BigIntegerField(primary_key=True)
    beskrivelse = models.TextField(blank=True, null=True)
    feltnavn = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    tabelnavn = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'KolloneBeskrivelse'




class MødeAktør(models.Model):
    id = models.BigIntegerField(primary_key=True)
    aktørid = models.ForeignKey(Aktør)
    mødeid = models.ForeignKey(Møde)
    opdateringsdato = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MødeAktør'




class Omtryk(models.Model):
    id = models.BigIntegerField(primary_key=True)
    begrundelse = models.TextField(blank=True, null=True)
    dato = models.TextField(blank=True, null=True)
    dokumentid = models.ForeignKey(Dokument)
    opdateringsdato = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Omtryk'


class Periode(models.Model):
    id = models.BigIntegerField(primary_key=True)
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
    id = models.BigIntegerField(primary_key=True)
    afgørelse = models.TextField(blank=True, null=True)
    afgørelsesdato = models.TextField(blank=True, null=True)
    afgørelsesresultatkode = models.TextField(blank=True, null=True)
    afstemningskonklusion = models.TextField(blank=True, null=True)
    baggrundsmateriale = models.TextField(blank=True, null=True)
    begrundelse = models.TextField(blank=True, null=True)
    deltundersagid = models.ForeignKey(Deltundersag)
    fremsatundersagid = models.ForeignKey(Fremsatundersag)
    kategoriid = models.ForeignKey(Kategori)
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
    periodeid = models.ForeignKey(Periode)
    resume = models.TextField(blank=True, null=True)
    retsinformationsurl = models.TextField(blank=True, null=True)
    rådsmødedato = models.TextField(blank=True, null=True)
    statsbudgetsag = models.NullBooleanField()
    statusid = models.ForeignKey(Sagstatus)
    titel = models.TextField(blank=True, null=True)
    titelkort = models.TextField(blank=True, null=True)
    typeid = models.ForeignKey(Sagtype)

    class Meta:
        managed = False
        db_table = 'Sag'


class SagAktør(models.Model):
    id = models.BigIntegerField(primary_key=True)
    aktørid = models.ForeignKey(Aktør)
    opdateringsdato = models.TextField(blank=True, null=True)
    rolleid = models.ForeignKey(SagAktørRolle)
    sagid = models.ForeignKey(Sag)

    class Meta:
        managed = False
        db_table = 'SagAktør'


class SagAktørRolle(models.Model):
    id = models.BigIntegerField(primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    rolle = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SagAktørRolle'


class SagDokument(models.Model):
    id = models.BigIntegerField(primary_key=True)
    bilagsnummer = models.TextField(blank=True, null=True)
    dokumentid = models.ForeignKey(Dokument)
    frigivelsesdato = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    rolleid = models.ForeignKey(SagDokumentRolle)
    sagid = models.ForeignKey(Sag)

    class Meta:
        managed = False
        db_table = 'SagDokument'


class SagDokumentRolle(models.Model):
    id = models.BigIntegerField(primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    rolle = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SagDokumentRolle'


class Sagskategori(models.Model):
    id = models.BigIntegerField(primary_key=True)
    kategori = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sagskategori'


class Sagsstatus(models.Model):
    id = models.BigIntegerField(primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sagsstatus'


class Sagstrin(models.Model):
    id = models.BigIntegerField(primary_key=True)
    dato = models.TextField(blank=True, null=True)
    folketingstidende = models.TextField(blank=True, null=True)
    folketingstidendesidenummer = models.TextField(blank=True, null=True)
    folketingstidendeurl = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    sagid = models.ForeignKey(Sag)
    statusid = models.ForeignKey(Sagstrintatus)
    titel = models.TextField(blank=True, null=True)
    typeid = models.ForeignKey(Sagstrintype)

    class Meta:
        managed = False
        db_table = 'Sagstrin'


class SagstrinAktør(models.Model):
    id = models.BigIntegerField(primary_key=True)
    aktørid = models.ForeignKey(Aktør)
    opdateringsdato = models.TextField(blank=True, null=True)
    rolleid = models.ForeignKey(SagstrinAktørRolle)
    sagstrinid = models.ForeignKey(Sagstrin)

    class Meta:
        managed = False
        db_table = 'SagstrinAktør'


class SagstrinAktørRolle(models.Model):
    id = models.BigIntegerField(primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    rolle = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SagstrinAktørRolle'


class Sagstrinsagstrin(models.Model):
    id = models.BigIntegerField(primary_key=True)
    andetsagstrinid = models.ForeignKey(Andetsagstrin)
    førstesagstrinid = models.ForeignKey(Førstesagstrin)
    opdateringsdato = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SagstrinSagstrin'


class Sagstrinsstatus(models.Model):
    id = models.BigIntegerField(primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sagstrinsstatus'


class Sagstrinstype(models.Model):
    id = models.BigIntegerField(primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sagstrinstype'


class Sagstype(models.Model):
    id = models.BigIntegerField(primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sagstype'


class Stemme(models.Model):
    id = models.BigIntegerField(primary_key=True)
    afstemningid = models.ForeignKey(Afstemning)
    aktørid = models.ForeignKey(Aktør)
    opdateringsdato = models.TextField(blank=True, null=True)
    typeid = models.ForeignKey(Stemmetype)

    class Meta:
        managed = False
        db_table = 'Stemme'


class Tabelbeskrivelse(models.Model):
    id = models.BigIntegerField(primary_key=True)
    beskrivelse = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    tabelnavn = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TabelBeskrivelse'
