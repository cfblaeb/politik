from django.db import models


class Sagskategori(models.Model):
    id = models.BigIntegerField(primary_key=True)
    kategori = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sagskategori'


class Dokumentkategori(models.Model):
    id = models.BigIntegerField(primary_key=True)
    kategori = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dokumentkategori'


class Sagsstatus(models.Model):
    id = models.BigIntegerField(primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sagsstatus'


class Dokumentstatus(models.Model):
    id = models.BigIntegerField(primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dokumentstatus'


class Mødestatus(models.Model):
    id = models.BigIntegerField(primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Mødestatus'


class Sagstrinsstatus(models.Model):
    id = models.BigIntegerField(primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sagstrinsstatus'


class AktørAktørRolle(models.Model):
    id = models.BigIntegerField(primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    rolle = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AktørAktørRolle'


class DokumentAktørRolle(models.Model):
    id = models.BigIntegerField(primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    rolle = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DokumentAktørRolle'


class SagAktørRolle(models.Model):
    id = models.BigIntegerField(primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    rolle = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SagAktørRolle'


class SagDokumentRolle(models.Model):
    id = models.BigIntegerField(primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    rolle = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SagDokumentRolle'


class SagstrinAktørRolle(models.Model):
    id = models.BigIntegerField(primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    rolle = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SagstrinAktørRolle'


class Afstemningstype(models.Model):
    id = models.BigIntegerField(primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Afstemningstype'


class Mødetype(models.Model):
    id = models.BigIntegerField(primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Mødetype'


class Aktørtype(models.Model):
    id = models.BigIntegerField(primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Aktørtype'


class Dokumenttype(models.Model):
    id = models.BigIntegerField(primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dokumenttype'


class Stemmetype(models.Model):
    id = models.BigIntegerField(primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Stemmetype'


class Emneordstype(models.Model):
    id = models.BigIntegerField(primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Emneordstype'


class Sagstype(models.Model):
    id = models.BigIntegerField(primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sagstype'


class Sagstrinstype(models.Model):
    id = models.BigIntegerField(primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sagstrinstype'


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


class Møde(models.Model):
    id = models.BigIntegerField(primary_key=True)
    dagsordenurl = models.TextField(blank=True, null=True)
    dato = models.TextField(blank=True, null=True)
    lokale = models.TextField(blank=True, null=True)
    mødestatusid = models.ForeignKey(Mødestatus, db_column='mødestatusid')
    mødetypeid = models.ForeignKey(Mødetype, db_column='mødetypeid')
    nummer = models.TextField(blank=True, null=True)
    offentlighedskode = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    periodeid = models.ForeignKey(Periode, db_column='periodeid')
    starttidsbemærkning = models.TextField(blank=True, null=True)
    titel = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Møde'


class Sag(models.Model):
    id = models.BigIntegerField(primary_key=True)
    afgørelse = models.TextField(blank=True, null=True)
    afgørelsesdato = models.TextField(blank=True, null=True)
    afgørelsesresultatkode = models.TextField(blank=True, null=True)
    afstemningskonklusion = models.TextField(blank=True, null=True)
    baggrundsmateriale = models.TextField(blank=True, null=True)
    begrundelse = models.TextField(blank=True, null=True)
    deltundersagid = models.ForeignKey('self', related_name='deltundersag', db_column='deltundersagid')
    fremsatundersagid = models.ForeignKey('self', related_name='fremsatundersag', db_column='fremsatundersagid')
    kategoriid = models.ForeignKey(Sagskategori, db_column='kategoriid')
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
    periodeid = models.ForeignKey(Periode, db_column='periodeid')
    resume = models.TextField(blank=True, null=True)
    retsinformationsurl = models.TextField(blank=True, null=True)
    rådsmødedato = models.TextField(blank=True, null=True)
    statsbudgetsag = models.NullBooleanField()
    statusid = models.ForeignKey(Sagsstatus, db_column='statusid')
    titel = models.TextField(blank=True, null=True)
    titelkort = models.TextField(blank=True, null=True)
    typeid = models.ForeignKey(Sagstype, db_column='typeid')

    class Meta:
        managed = False
        db_table = 'Sag'


class Sagstrin(models.Model):
    id = models.BigIntegerField(primary_key=True)
    dato = models.TextField(blank=True, null=True)
    folketingstidende = models.TextField(blank=True, null=True)
    folketingstidendesidenummer = models.TextField(blank=True, null=True)
    folketingstidendeurl = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    sagid = models.ForeignKey(Sag, db_column='sagid')
    statusid = models.ForeignKey(Sagstrinsstatus, db_column='statusid')
    titel = models.TextField(blank=True, null=True)
    typeid = models.ForeignKey(Sagstrinstype, db_column='typeid')

    class Meta:
        managed = False
        db_table = 'Sagstrin'


class Afstemning(models.Model):
    id = models.BigIntegerField(primary_key=True)
    kommentar = models.TextField(blank=True, null=True)
    konklusion = models.TextField(blank=True, null=True)
    mødeid = models.ForeignKey(Møde, db_column='mødeid')
    nummer = models.BigIntegerField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    sagstrinid = models.ForeignKey(Sagstrin, db_column='sagstrinid')
    typeid = models.ForeignKey(Afstemningstype, db_column='typeid')
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
    periodeid = models.ForeignKey(Periode, db_column='periodeid')
    slutdato = models.TextField(blank=True, null=True)
    startdato = models.TextField(blank=True, null=True)
    typeid = models.ForeignKey(Aktørtype, db_column='typeid')

    class Meta:
        managed = False
        db_table = 'Aktør'


class AktørAktør(models.Model):
    id = models.BigIntegerField(primary_key=True)
    fraaktørid = models.ForeignKey(Aktør, related_name='fraaktør', db_column='fraaktørid')
    opdateringsdato = models.TextField(blank=True, null=True)
    rolleid = models.ForeignKey(AktørAktørRolle, db_column='rolleid')
    slutdato = models.TextField(blank=True, null=True)
    startdato = models.TextField(blank=True, null=True)
    tilaktørid = models.ForeignKey(Aktør, related_name='tilaktør', db_column='tilaktørid')

    class Meta:
        managed = False
        db_table = 'AktørAktør'


class Dokument(models.Model):
    id = models.BigIntegerField(primary_key=True)
    dagsordenudgavenummer = models.TextField(blank=True, null=True)
    dato = models.TextField(blank=True, null=True)
    frigivelsesdato = models.TextField(blank=True, null=True)
    grundnotatstatus = models.TextField(blank=True, null=True)
    kategoriid = models.ForeignKey(Dokumentkategori, db_column='kategoriid')
    modtagelsesdato = models.TextField(blank=True, null=True)
    offentlighedskode = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    paragraf = models.TextField(blank=True, null=True)
    paragrafnummer = models.TextField(blank=True, null=True)
    procedurenummer = models.TextField(blank=True, null=True)
    spørgsmålsid = models.ForeignKey('self')
    spørgsmålsordlyd = models.TextField(blank=True, null=True)
    spørgsmålstitel = models.TextField(blank=True, null=True)
    statusid = models.ForeignKey(Dokumentstatus, db_column='statusid')
    titel = models.TextField(blank=True, null=True)
    typeid = models.ForeignKey(Dokumenttype, db_column='typeid')

    class Meta:
        managed = False
        db_table = 'Dokument'


class Dagsordenspunkt(models.Model):
    id = models.BigIntegerField(primary_key=True)
    forhandling = models.TextField(blank=True, null=True)
    forhandlingskode = models.TextField(blank=True, null=True)
    kommentar = models.TextField(blank=True, null=True)
    kørebemærkning = models.TextField(blank=True, null=True)
    mødeid = models.ForeignKey(Møde, db_column='mødeid')
    nummer = models.TextField(blank=True, null=True)
    offentlighedskode = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    sagstrinid = models.ForeignKey(Sagstrin, db_column='sagstrinid')
    superid = models.IntegerField()
    titel = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dagsordenspunkt'


class Dagsordenspunktdokument(models.Model):
    dagsordenspunktid = models.ForeignKey(Dagsordenspunkt, db_column='dagsordenspunktid')
    dokumentid = models.ForeignKey(Dokument, db_column='dokumentid')
    id = models.BigIntegerField(primary_key=True)
    note = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DagsordenspunktDokument'


class Dagsordenspunktsag(models.Model):
    dagsordenspunktid = models.ForeignKey(Dagsordenspunkt, db_column='dagsordenspunktid')
    id = models.BigIntegerField(primary_key=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    sagid = models.ForeignKey(Sag, db_column='sagid')

    class Meta:
        managed = False
        db_table = 'DagsordenspunktSag'


class DokumentAktør(models.Model):
    id = models.BigIntegerField(primary_key=True)
    aktørid = models.ForeignKey(Aktør, db_column='aktørid')
    dokumentid = models.ForeignKey(Dokument, db_column='dokumentid')
    opdateringsdato = models.TextField(blank=True, null=True)
    rolleid = models.ForeignKey(DokumentAktørRolle, db_column='rolleid')

    class Meta:
        managed = False
        db_table = 'DokumentAktør'


class Emneord(models.Model):
    id = models.BigIntegerField(primary_key=True)
    emneord = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    typeid = models.ForeignKey(Emneordstype, db_column='typeid')

    class Meta:
        managed = False
        db_table = 'Emneord'


class Emneordsag(models.Model):
    id = models.BigIntegerField(primary_key=True)
    emneordid = models.ForeignKey(Emneord, db_column='emneordid')
    opdateringsdato = models.TextField(blank=True, null=True)
    sagid = models.ForeignKey(Sag, db_column='sagid')

    class Meta:
        managed = False
        db_table = 'EmneordSag'


class Fil(models.Model):
    id = models.BigIntegerField(primary_key=True)
    dokumentid = models.ForeignKey(Dokument, db_column='dokumentid')
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
    aktørid = models.ForeignKey(Aktør, db_column='aktørid')
    mødeid = models.ForeignKey(Møde, db_column='mødeid')
    opdateringsdato = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MødeAktør'


class Omtryk(models.Model):
    id = models.BigIntegerField(primary_key=True)
    begrundelse = models.TextField(blank=True, null=True)
    dato = models.TextField(blank=True, null=True)
    dokumentid = models.ForeignKey(Dokument, db_column='dokumentid')
    opdateringsdato = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Omtryk'


class SagAktør(models.Model):
    id = models.BigIntegerField(primary_key=True)
    aktørid = models.ForeignKey(Aktør, db_column='aktørid')
    opdateringsdato = models.TextField(blank=True, null=True)
    rolleid = models.ForeignKey(SagAktørRolle, db_column='rolleid')
    sagid = models.ForeignKey(Sag, db_column='sagid')

    class Meta:
        managed = False
        db_table = 'SagAktør'


class SagDokument(models.Model):
    id = models.BigIntegerField(primary_key=True)
    bilagsnummer = models.TextField(blank=True, null=True)
    dokumentid = models.ForeignKey(Dokument, db_column='dokumentid')
    frigivelsesdato = models.TextField(blank=True, null=True)
    opdateringsdato = models.TextField(blank=True, null=True)
    rolleid = models.ForeignKey(SagDokumentRolle, db_column='rolleid')
    sagid = models.ForeignKey(Sag, db_column='sagid')

    class Meta:
        managed = False
        db_table = 'SagDokument'


class SagstrinAktør(models.Model):
    id = models.BigIntegerField(primary_key=True)
    aktørid = models.ForeignKey(Aktør, db_column='aktørid')
    opdateringsdato = models.TextField(blank=True, null=True)
    rolleid = models.ForeignKey(SagstrinAktørRolle, db_column='rolleid')
    sagstrinid = models.ForeignKey(Sagstrin, db_column='sagstrinid')

    class Meta:
        managed = False
        db_table = 'SagstrinAktør'


class SagstrinSagstrin(models.Model):
    id = models.BigIntegerField(primary_key=True)
    andetsagstrinid = models.ForeignKey(Sagstrin, related_name='andetsagstrin', db_column='andetsagstrinid')
    førstesagstrinid = models.ForeignKey(Sagstrin, related_name='førstesagstrin', db_column='førstesagstrinid')
    opdateringsdato = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SagstrinSagstrin'


class Stemme(models.Model):
    id = models.BigIntegerField(primary_key=True)
    afstemningid = models.ForeignKey(Afstemning, db_column='afstemningid')
    aktørid = models.ForeignKey(Aktør, db_column='aktørid')
    opdateringsdato = models.TextField(blank=True, null=True)
    typeid = models.ForeignKey(Stemmetype, db_column='typeid')

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