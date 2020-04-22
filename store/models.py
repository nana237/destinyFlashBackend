from django.db import models
from django import forms
from django.utils import timezone
from datetime import date

#class Student(models.Model):
#    FRESHMAN = 'FR'
#    SOPHOMORE = 'SO'
#    JUNIOR = 'JR'
#    SENIOR = 'SR'
#    GRADUATE = 'GR'
#    YEAR_IN_SCHOOL_CHOICES = [
#        (FRESHMAN, 'Freshman'),
#        (SOPHOMORE, 'Sophomore'),
#        (JUNIOR, 'Junior'),
#        (SENIOR, 'Senior'),
#        (GRADUATE, 'Graduate'),
#    ]
#    year_in_school = models.CharField(
#        max_length=2,
#        choices=YEAR_IN_SCHOOL_CHOICES,
#        default=FRESHMAN,
#    )
#
#    def is_upperclass(self):
#        return self.year_in_school in {self.JUNIOR, self.SENIOR}

# class Manufacturer(models.Model):
#     # ...
#     pass
# 
# class Car(models.Model):
#     manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
#     # ...



# class Person(models.Model):
#     name = models.CharField(max_length=128)
# 
#     def __str__(self):
#         return self.name
# 
# class Group(models.Model):
#     name = models.CharField(max_length=128)
#     members = models.ManyToManyField(Person, through='Membership')
# 
#     def __str__(self):
#         return self.name
# 
# class Membership(models.Model):
#     person = models.ForeignKey(Person, on_delete=models.CASCADE)
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
#     date_joined = models.DateField()
#     invite_reason = models.CharField(max_length=64)

# - de .today()

"""
from django.conf import settings
from django.db import models

class MySpecialUser(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    supervisor = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='supervisor_of',
    )
"""

class FACTURE(models.Model):
    #idF = models.IntegerField()
    dateF = models.DateField(default=date.today)
    montantF = models.IntegerField()
    commande = models.OneToOneField('COMMANDE',on_delete=models.CASCADE)

class VERSEMENT(models.Model):

    EN_ATTENTE = 'E'
    EN_COUR = 'EC'
    EFFECTUER = 'EF'
    TERMINER = "T"
    STATUS_VERSEMENT_CHOICES = [
        (EN_ATTENTE,'En Attente'),
        (EN_COUR,'En Cour'),
        (EFFECTUER,'Effectué'),
        (TERMINER,'Terminé')
    ]
    
    BANCAIRE = 'B'
    MOBILE_MONEY = 'M'
    ESPECE = 'E'
    TYPE_VERSEMENT_CHOICES = [
        (BANCAIRE,'Bancaire'),
        (MOBILE_MONEY,'Mobile Money'),
        (ESPECE,'Espece')
    ]

    #idVers = models.IntegerField()
    dateVers = models.DateField()
    typeVers = models.CharField(max_length=1, choices=TYPE_VERSEMENT_CHOICES, default=ESPECE)
    MontantVers = models.IntegerField()
    statutVers = models.CharField(max_length=2, choices=STATUS_VERSEMENT_CHOICES, default=EN_ATTENTE)
    commande = models.ForeignKey('COMMANDE', on_delete = models.CASCADE)
    client = models.ForeignKey('CLIENT', on_delete = models.CASCADE)

class LIVRAISON(models.Model):

    MAISON = 'M'
    POINT_RETRAIT = 'P'
    TYPE_LIVRAISON_CHOICES = [
        (MAISON,'Maison'),
        (POINT_RETRAIT,'Point de Retrait')
    ]

    #numL = models.IntegerField()
    libeleL = models.CharField(max_length=100, blank= True, null=True)
    dateL = models.DateField() 
    descriptionL = models.CharField(max_length=100)
    montantL = models.IntegerField()
    typeL = models.CharField(max_length=1, choices = TYPE_LIVRAISON_CHOICES, default = POINT_RETRAIT)
    client = models.ForeignKey('CLIENT',on_delete=models.CASCADE)
    point_de_retrait = models.ForeignKey('POINT_DE_RETRAIT', on_delete= models.CASCADE, blank= True, null=True)
    livreur = models.ForeignKey('LIVREUR', on_delete = models.CASCADE)
    commande = models.ForeignKey('COMMANDE',on_delete = models.CASCADE)

def upload_caracteristique(instance, filname):
    return '/'.join(['photoCaract',str(instance.article),filname])

class CARACTERISTIQUE(models.Model):
    #refCaract = models.IntegerField()
    couleurCaract = models.CharField(max_length=100)
    photoCaract = models.ImageField(max_length=256, blank= True, null=True,upload_to=upload_caracteristique)
    tailleCaract = models.IntegerField()
    autreDetailCaract = models.CharField(max_length=256,blank= True, null=True)
    prixCaract=models.IntegerField()
    qteCaract = models.IntegerField()
    nbAchatCaract = models.IntegerField()
    article = models.ForeignKey('ARTICLE', on_delete= models.CASCADE)

    # def __str__(self):
    #   return self.refCaract

    class Meta:
        ordering = ['article']


def upload_path(instance, filname):
    return '/'.join(['photoAr',str(instance.designationAr),filname])


class ARTICLE(models.Model):
    #idAr = models.IntegerField()
    designationAr = models.CharField(max_length=100)
    photoAr = models.ImageField(blank=True, null=True, upload_to=upload_path)
    prixAr = models.IntegerField()
    qteAr=models.IntegerField()
    StockSecuriteAr = models.IntegerField()
    VideoPubAr = models.CharField(max_length=256, blank=True, null=True)
    nbAchatAr=models.IntegerField()
    sous_categorie= models.ForeignKey('SOUS_CATEGORIE', on_delete = models.CASCADE)
    marque = models.ForeignKey( 'MARQUE', on_delete = models.CASCADE)

    def __str__(self):
        return self.designationAr

    class Meta:
        ordering = ['designationAr']

class COMMANDE(models.Model):

    EN_ATTENTE = 'EA'
    LIVRER = 'L'
    A_RETIRER = 'AR'
    EN_COUR_DE_LIVRAISON = 'EL'
    RECU = 'R'
    STATUS_RETOUR_CHOICES = [
        (EN_ATTENTE,'En Attente'),
        (LIVRER,'Livré'),
        (A_RETIRER,'A Rétirer'),
        (EN_COUR_DE_LIVRAISON,'En cour de livraison'),
        (RECU,'reçu')
    ]

    #idCmd = models.IntegerField()
    libCmd = models.CharField(max_length=100)
    dateCmd = models.DateField()
    statusCmd = models.CharField(max_length=2, choices=STATUS_RETOUR_CHOICES, default=EN_ATTENTE)
    descriptionCmd = models.CharField(max_length=256)
    montantLivraisonCmd = models.IntegerField()
    client = models.ForeignKey('CLIENT', on_delete=models.CASCADE)
    articles = models.ManyToManyField('ARTICLE')
    caracteristiques = models.ManyToManyField(CARACTERISTIQUE, through = 'DETAIL_COMMANDE', through_fields=('commande','caracteristique'), blank= True, null = True)

    def __str__(self):
        return self.libCmd

    class Meta:
        ordering = ['libCmd']



"""
class Person(models.Model):
    name = models.CharField(max_length=50)

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(
        Person,
        through='Membership',
        through_fields=('group', 'person'),
    )

class Membership(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    inviter = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="membership_invites",
    )
    invite_reason = models.CharField(max_length=64)
"""


class DETAIL_COMMANDE(models.Model):
    commande = models.ForeignKey(COMMANDE, on_delete = models.CASCADE)
    caracteristique = models.ForeignKey(CARACTERISTIQUE, on_delete = models.CASCADE)
    qte_Commander = models.IntegerField()

class RETOUR(models.Model):

    EN_ATTENTE = 'EA'
    APPROUVER = 'A'
    REFUSER = 'R'
    EN_COUR_D_EXECUTION = 'EX'
    VALIDE = 'V'
    STATUS_RETOUR_CHOICES = [
        (EN_ATTENTE,'En Attente'),
        (APPROUVER,'Approuvé'),
        (REFUSER,'Refusé'),
        (EN_COUR_D_EXECUTION,'En cour d\'éxécution'),
        (VALIDE,'Validé')
    ]

    #idRetour = models.IntegerField()
    motifRetour = models.CharField(max_length=100)
    dateRetour = models.DateField()
    statutRetour = models.CharField(max_length=2,choices=STATUS_RETOUR_CHOICES, default=EN_ATTENTE)
    client = models.ForeignKey('CLIENT', on_delete=models.CASCADE)

    def __str__(self):
        return self.motifRetour

    class Meta:
        ordering = ['motifRetour']

class EVENEMENT(models.Model):
    #idEven = models.IntegerField()
    libEven = models.CharField(max_length=100)
    dateEven = models.DateTimeField(default=timezone.now)
    descriptionEven = models.CharField(max_length=256)
    agent_destiny = models.ForeignKey('AGENT_DESTINY', on_delete=models.CASCADE)

    def __str__(self):
        return self.libEven

    class Meta:
        ordering = ['libEven']

class PANIER(models.Model):
    #idPanier = models.IntegerField()
    libPanier = models.CharField(max_length=100)
    client = models.OneToOneField('CLIENT', on_delete=models.CASCADE)
    articles = models.ManyToManyField('ARTICLE', blank=True, null=True)
    
    def __str__(self):
        return self.libPanier

    class Meta:
        ordering = ['libPanier']

class SOUS_CATEGORIE(models.Model):
    #idSCat = models.IntegerField()
    libSCat = models.CharField(max_length=50)
    photoSCat = models.CharField(max_length=256,null=True,blank=True)
    categorie = models.ForeignKey('CATEGORIE', on_delete=models.CASCADE)

    def __str__(self):
        return self.libSCat

    class Meta:
        ordering = ['libSCat']

class CATEGORIE(models.Model):
    #idCat = models.IntegerField()
    libCat = models.CharField(max_length=50)
    photoCat = models.CharField(max_length=256,null=True,blank=True)

    def __str__(self):
        return self.libCat

    class Meta:
        ordering = ['libCat']

class MARQUE(models.Model):
    #idMArq = models.IntegerField()
    libMarq = models.CharField(max_length=50)
    photoMarq = models.CharField(max_length=256,null=True,blank=True)

    def __str__(self):
        return self.libMarq

    class Meta:
        ordering = ['libMarq']

class PRESTATAIRE(models.Model):

    MASCULIN = 'M'
    FEMININ = 'F'
    SEXE_CHOICES = [
        (MASCULIN,'Masculin'),
        (FEMININ,'Feminin')
    ]


    #idP = models.IntegerField()
    nomP = models.CharField(max_length=100)
    prenomP = models.CharField(max_length=100)
    dateNaissP = models.DateField()
    emailP = models.EmailField(null=True,blank=True)
    sexeP = models.CharField(max_length=1, choices = SEXE_CHOICES, default = MASCULIN)
    adresseP = models.CharField(max_length=100,null=True,blank=True)
    villeP = models.CharField(max_length=100)
    quartierP = models.CharField(max_length=100)
    numCNI_P = models.CharField(max_length=25, unique = True)
    telP = models.IntegerField()
    loginP = models.CharField(max_length=100)
    motDePassP = models.CharField(max_length=50)
    
    def __str__(self):
        return "%s %s" % (self.nomP, self.prenomP)

    class Meta:
        ordering = ['nomP']


class LIVREUR(models.Model):

    MASCULIN = 'M'
    FEMININ = 'F'
    SEXE_CHOICES = [
        (MASCULIN,'Masculin'),
        (FEMININ,'Feminin')
    ]


    #idL = models.IntegerField()
    nomL = models.CharField(max_length=100)
    prenomL = models.CharField(max_length=100)
    dateNaissL = models.DateField()
    emailL = models.EmailField(null=True,blank=True)
    sexeL = models.CharField(max_length=1, choices=SEXE_CHOICES, default=MASCULIN  )
    adresseL = models.CharField(max_length=100,null=True,blank=True)
    villeL = models.CharField(max_length=100)
    quartierL = models.CharField(max_length=100)
    numCNI_L = models.CharField(max_length=100, unique=True)
    telL = models.IntegerField()
    loginL = models.CharField(max_length=100)
    motDePassL = models.CharField(max_length=50)

    def __str__(self):
        return "%s %s" % (self.nomL, self.prenomL)

    class Meta:
        ordering = ['nomL']

class CLIENT(models.Model):

    MASCULIN = 'M'
    FEMININ = 'F'
    SEXE_CHOICES = [
        (MASCULIN,'Masculin'),
        (FEMININ,'Feminin')
    ]

    #idC = models.IntegerField()
    nomC = models.CharField(max_length=100)
    prenomC = models.CharField(max_length=100)
    dateNaissC = models.DateField()
    emailC = models.EmailField(null=True,blank=True)
    sexeC = models.CharField(max_length=1, choices=SEXE_CHOICES, default=MASCULIN  )
    adresseC = models.CharField(max_length=100,null=True,blank=True)
    villeC = models.CharField(max_length=100,null=True,blank=True)
    quartierC = models.CharField(max_length=100,null=True,blank=True)
    numCNI_C = models.CharField(max_length=25, unique = True)
    telC = models.IntegerField()
    loginC = models.CharField(max_length=100)
    motDePassC = models.CharField(max_length=50)

    def __str__(self):
        return "%s %s" % (self.nomC, self.prenomC)

    class Meta:
        ordering = ['nomC']

class AGENT_DESTINY(models.Model):

    MASCULIN = 'M'
    FEMININ = 'F'
    SEXE_CHOICES = [
        (MASCULIN,'Masculin'),
        (FEMININ,'Feminin')
    ]


    #idA = models.IntegerField()
    nomA = models.CharField(max_length=100)
    prenomA = models.CharField(max_length=100)
    dateNaissA = models.DateField()
    emailA = models.EmailField(null=True,blank=True)
    sexeA = models.CharField(max_length=1, choices=SEXE_CHOICES, default=MASCULIN  )
    adresseA = models.CharField(max_length=100,null=True,blank=True)
    villeA = models.CharField(max_length=100)
    quartierA = models.CharField(max_length=100)
    numCNI_A = models.CharField(max_length=25, unique = True)
    telA = models.IntegerField()
    loginA = models.CharField(max_length=100)
    motDePassA = models.CharField(max_length=50)
    prestataires = models.ManyToManyField ('PRESTATAIRE', through='NOTIFICATION',through_fields=('agent_destiny','prestataire') )


    def __str__(self):
        return "%s %s" % (self.nomA, self.prenomA)

    class Meta:
        ordering = ['nomA']


class NOTIFICATION(models.Model):
    agent_destiny = models.ForeignKey('AGENT_DESTINY', on_delete= models.CASCADE)
    prestataire = models.ForeignKey('PRESTATAIRE', on_delete= models.CASCADE)
    raisonNot = models.CharField(max_length=100)
    dateNot = models.DateField(max_length=100)



class POINT_DE_RETRAIT(models.Model):
    #idPoint = models.IntegerField()
    libPoint = models.CharField(max_length=100)
    villePoint = models.CharField(max_length=100)
    quartierPoint = models.CharField(max_length=100)
    descriptionPoint = models.CharField(max_length=256,null=True,blank=True)
    telPoint = models.IntegerField()
    mailPoint = models.EmailField(null=True,blank=True)

    def __str__(self):
        return self.libPoint

    class Meta:
        ordering = ['libPoint']


class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

#class Article(models.Model):
#    headline = models.CharField(max_length=100)
#    pub_date = models.DateField()
#    reporter = models.CharField(max_length=100)
#    reporter = models.ForeignKey('Reporter', on_delete=models.CASCADE)
#
#    def __str__(self):
#        return self.headline
#
#    class Meta:
#        ordering = ['headline']



    #def __str__(self):
     #   return "%s %s" % (self.first_name, self.last_name)
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

class Movie(models.Model):
    title = models.CharField(max_length=32)
    desc = models.CharField(max_length=256)
    year = models.IntegerField()
    autor = models.CharField(max_length=32)
    autor = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)

   # def __str__(self):
   #     return self.title

    #class Meta:
     #   ordering = ['title']





