from pyexpat import model
from django.db import models
from datetime import date, datetime
from django.contrib.auth.models import User

# Create your models here.


class Terminale(models.Model):
    TYPE = (
        ('PC', ('PC - Run windows ')),
        ('tablette', ('MAc - Run MacOS ')),
        ('portable ', ('portable - android ')),
        
    ) 
    SECTEUR = (
        ('administration'),
        ('developpement'),
        ('Conception '),
        
    ) 
    id = models.AutoField(primary_key =True, editable = False )
    nom = models.CharField(max_length =200)
    sort= models.CharField(max_length=32, choices=TYPE, default ='PC')
    interface=models.CharField(max_length =20)
    addresse=models.CharField(max_length =16)
    mask=models.CharField(max_length =16)
    addresse_pass=models.CharField(max_length =16)
    secteur=models.CharField(max_length=32, choices= SECTEUR,)
    
    maj=models.CharField(max_length =16)
    maintenance_date = models.DateField( default = datetime.now())
    personnel=models.ManyToManyField(
        User,
        through="Personnel",
    )
class Commutateur(models.Model):
    INTERFACE = (
        ('Fa0/1'),
        ('Fa0/2'),
        ('Fa0/3'),
        ('Fa0/4'),
        ('Fa0/5'),
        ('Fa0/6'),
        ('Fa0/7'),
        ('Fa0/8'),
        ('Fa0/9'),
        ('Fa0/10'),
        ('Fa0/11'),
        ('Fa0/12'),
    ) 
    SECTEUR = (
        ('administration'),
        ('developpement'),
        ('Conception '),
        
    ) 
    nom = models.CharField(primary_key =True, max_length =200)

    id = models.AutoField(editable = False )
    
    interface=models.CharField(max_length =20, choices= INTERFACE,)
    addresse=models.CharField(max_length =16)
    mask=models.CharField(max_length =16)
    addresse_pass=models.CharField(max_length =16)
    secteur=models.CharField(max_length=32, choices= SECTEUR,)
    vlan=models.ManyToManyField(
        nom,
        through="Vlan",
        )
    maj=models.CharField(max_length =16)
    maintenance_date = models.DateField( default = datetime.now())
    personnel=models.ManyToManyField(
        User,
        through="Personnel",
    )
class Routeur(models.Model):
    INTERFACE = (
        ('Fa0/1'),
        ('Fa0/2'),
        ('s0/0/0'),
        ('s0/0/1'),
        
    ) 
    SECTEUR = (
        ('administration'),
        ('developpement'),
        ('Conception '),
        
    ) 
    id = models.AutoField(primary_key =True, editable = False )
    nom = models.CharField(max_length =200)
    interface=models.CharField(max_length =20, choices= INTERFACE,)
    addresse=models.CharField(max_length =16)
    mask=models.CharField(max_length =16)
    addresse_pass=models.CharField(max_length =16)
    secteur=models.CharField(max_length=32, choices= SECTEUR,)
    protocole_routage=models.CharField(max_length =200)
    maj=models.CharField(max_length =16)
    maintenance_date = models.DateField( default = datetime.now())
    personnel=models.ManyToManyField(
        User,
        through="Personnel",
    )



class Personnel(models.Model):
    terminale= models.ForeignKey(Terminale)
    personnel= models.ForeignKey(User)
    commutateur=models.ForeignKey(Commutateur)
    routeur=models.ForeignKey(Routeur)
    tel=models.CharField(max_length =12)

class Vlan(models.Model):
    nom = models.CharField(primary_key =True, max_length =7)
    commutateur=models.ForeignKey(Commutateur)

    

