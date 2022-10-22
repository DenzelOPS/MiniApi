from django.db import models


class Sotrudniki(models.Model):
    id_sotrudnik = models.AutoField(primary_key=True)
    Code = models.IntegerField()
    Stavka = models.FloatField(default=None, null=True, blank=True)
    FIO = models.TextField()
    
class Podrazdeleniya(models.Model):
    id_podrazdel = models.AutoField(primary_key=True)
    id_nachal = models.ForeignKey(Sotrudniki, db_column='id_sotrudnik' , on_delete=models.DO_NOTHING, default=None, null=True, blank=True)
    name_podrazdel = models.TextField()
    
class Doljnosti(models.Model):
    id_doljnost = models.AutoField(primary_key=True)
    name = models.TextField()
    prioritet = models.IntegerField()
    
class Zadachi(models.Model):
    id_zadacha = models.AutoField(primary_key=True)
    text_zadacha = models.TextField()
    
class Doljnost_sotrudnik(models.Model):
    id_sotrud = models.ForeignKey(Sotrudniki, db_column='id_sotrudnik' , on_delete=models.DO_NOTHING)
    id_doljnost = models.ForeignKey(Doljnosti, db_column='id_doljnost' , on_delete=models.DO_NOTHING)
    
class Sotrudnik_zadachi(models.Model):
    id_sotrudnik = models.ForeignKey(Sotrudniki, db_column='id_sotrudnik' , on_delete=models.DO_NOTHING)
    id_zadacha = models.ForeignKey(Zadachi, db_column='id_zadacha' , on_delete=models.DO_NOTHING)
    Date = models.TextField(default=None, null=True, blank=True)
