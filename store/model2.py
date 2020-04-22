#---------------------------------------------------- deja fais
class ARTICLE(models.Model):
    #idA = models.IntegerField()
    designationA = models.CharField(max_length=100)
    photoA = models.CharField(max_length=256)
    prixA = models.IntegerField()
    qteA=models.IntegerField()
    StockSecuriteA = models.IntegerField()
    VideoPubA = models.CharField(max_length=256)
    nbAchatA=models.IntegerField()
    #idPanier
    #idSC
    #idMarq
#---------------------------------------------------

#--------------------------------------------------- deja fais
class DETAIL_COMMANDE(models.Model):
    #refCaract
    #idCmd
    qte_Commander = models.IntegerField()
#---------------------------------------------------

# (, , )
# (, , , #)
# (, , )

#--------------------------------------------------- deja fais
class CATEGORIE(models.Model):
    #idCat = models.IntegerField()
    libCat = models.CharField(max_length=50)
    photoCat = models.CharField(max_length=256)
#---------------------------------------------------

#--------------------------------------------------- deja fais
class SOUS_CATEGORIE(models.Model):
    #idSCat = models.IntegerField()
    libSCat = models.CharField(max_length=50)
    photoSCat = models.CharField(max_length=256)
    #idCat
#----------------------------------------------------

#---------------------------------------------------- deja fais
class MARQUE(models.Model):
    #idMArq = models.IntegerField()
    libMarq = models.CharField(max_length=50)
    photoMarq = models.CharField(max_length=256)
#----------------------------------------------------

# (, , , , , , , , )
# (, , , )

#---------------------------------------------------- deja fais
class CARACTERISTIQUE(models.Model):
    #refCaract = models.IntegerField()
    couleurCaract = models.CharField(max_length=100)
    photoCaract = models.CharField(max_length=256)
    tailleCaract = models.IntegerField()
    autreDetailCaract = models.CharField(max_length=256)
    prixCaract=models.IntegerField()
    qteCaract = models.IntegerField()
    nbAchatCaract = models.IntegerField()
    #idA
#----------------------------------------------------

#---------------------------------------------------- deja fais
class FACTURE(models.Model):
    #idF = models.IntegerField()
    # -- comment mettre le type date ? dateF = models.CharField(max_length=100)
    montantF = models.IntegerField()
    #idCmd
#----------------------------------------------------

# (, , , , , , , , , , , )

#---------------------------------------------------------------- deja fais
class PRESTATAIRE(models.Model):
    #idP = models.IntegerField()
    nomP = models.CharField(max_length=100)
    prenomP = models.CharField(max_length=100)
    # -- comment mettre le type date ? dateNaissP = models.CharField(max_length=100)
    # -- comment mettre le type email ? emailP = models.CharField(max_length=100)
    # -- comment mettre le type enumeration ? sexeP = models.IntegerField()
    adresseP = models.CharField(max_length=100)
    villeP = models.CharField(max_length=100)
    quartierP = models.CharField(max_length=100)
    #comment dire qu'un attribut est a valeur unique ? numCNI_P = models.CharField(max_length=100)
    telP = models.IntegerField()
    loginP = models.CharField(max_length=100)
    #comment mettre le type password ? motDePassP = models.CharField(max_length=100)
#----------------------------------------------------------------

# (, , )
# (, , , , , , )
# (, , , , , )

#-------------------------------------------------------- deja fais
class PANIER(models.Model):
    #idPanier = models.IntegerField()
    libPanier = models.CharField(max_length=100)
    #idC
#--------------------------------------------------------

#-------------------------------------------------------------- deja fais
class VERSEMENT(models.Model):
    #idVers = models.IntegerField()
    # -- comment mettre le type date ? dateVers = models.CharField(max_length=100)
    typeVers = models.CharField(max_length=100)
    MontantVers = models.IntegerField()
    # -- comment mettre le type enumeration ? statutVers = CharField(max_length=100)
    #idCmd
    #idC
#--------------------------------------------------------------

#-------------------------------------------------------------- deja fais
class COMMANDE(models.Model):
    #idCmd = models.IntegerField()
    libCmd = models.CharField(max_length=100)
    # -- comment mettre le type date ? dateCmd = models.CharField(max_length=100)
    # -- comment mettre le type enumeration ? statusCmd = CharField(max_length=100)
    descriptionCmd = models.CharField(max_length=100)
    montantLivraisonCmd = models.IntegerField()
    #idC
#--------------------------------------------------------------

# (, , , , , , , , , , , )


class PERSONNE(models.Model):
    #idPers = models.IntegerField()
    nomPers = models.CharField(max_length=100)
    prenomPers = models.CharField(max_length=100)
    # -- comment mettre le type date ? dateNaissPers = models.CharField(max_length=100)
    # -- comment mettre le type enumeration ? sexePers = models.IntegerField()
    # -- comment mettre le type email ? emailPers = models.CharField(max_length=100)
    adressePers = models.CharField(max_length=100)
    villePers = models.CharField(max_length=100)
    quartierPers = models.CharField(max_length=100)
    #comment dire qu'un attribut est a valeur unique ? numCNI_Pers = models.CharField(max_length=100)
    telPers = models.IntegerField()
    loginPers = models.CharField(max_length=100)
    #comment mettre le type password ? motDePassPers = models.CharField(max_length=100)


# (, , , , , , , , , , , )

#------------------------------------------------------------- deja fais
class LIVREUR(models.Model):
    #idL = models.IntegerField()
    nomL = models.CharField(max_length=100)
    prenomL = models.CharField(max_length=100)
    # -- comment mettre le type date ? dateNaissL = models.CharField(max_length=100)
    # -- comment mettre le type email ? emailL = models.CharField(max_length=100)
    # -- comment mettre le type enumeration ? sexeL = models.IntegerField()
    adresseL = models.CharField(max_length=100)
    villeL = models.CharField(max_length=100)
    quartierL = models.CharField(max_length=100)
    #comment dire qu'un attribut est a valeur unique ? numCNI_L = models.CharField(max_length=100)
    telL = models.IntegerField()
    loginL = models.CharField(max_length=100)
    #comment mettre le type password ? motDePassL = models.CharField(max_length=100)
#--------------------------------------------------------------

# (, , , , , , )
# -------------------------------------------------------------------- deja fais
class POINT_DE_RETRAIT(models.Model):
    #idPoint = models.IntegerField()
    libPoint = models.CharField(max_length=100)
    villePoint = models.CharField(max_length=100)
    quartierPoint = models.CharField(max_length=100)
    descriptionPoint = models.CharField(max_length=256)
    telPoint = models.IntegerField()
    # -- comment mettre le type email ? mailPoint = models.CharField(max_length=100)
# ------------------------------------------------------------------ 

# (, , , , , , , , , , , )
# (, , , )

# ------------------------------------------------------------------ deja fais
class AGENT_DESTINY(models.Model):
    #idA = models.IntegerField()
    nomA = models.CharField(max_length=100)
    prenomA = models.CharField(max_length=100)
    # -- comment mettre le type date ? dateNaissA = models.CharField(max_length=100)
    # -- comment mettre le type email ? emailA = models.CharField(max_length=100)
    # -- comment mettre le type enumeration ? sexeA = models.IntegerField()
    adresseA = models.CharField(max_length=100)
    villeA = models.CharField(max_length=100)
    quartierA = models.CharField(max_length=100)
    #comment dire qu'un attribut est a valeur unique ? numCNI_A = models.CharField(max_length=100)
    telA = models.IntegerField()
    loginA = models.CharField(max_length=100)
    #comment mettre le type password ? motDePassA = models.CharField(max_length=100)
# -----------------------------------------------------------------

#------------------------------------------------------------------ deja fais
class NOTIFICATION(models.Model):
    #idP
    #idA
    raisonNot = models.CharField(max_length=100)
    # -- comment mettre le type date ? dateNot = models.CharField(max_length=100)
#------------------------------------------------------------------
    

# (, , , , , , , , , , , )

#------------------------------------------------------------------ deja fais
class CLIENT(models.Model):
    #idC = models.IntegerField()
    nomC = models.CharField(max_length=100)
    prenomC = models.CharField(max_length=100)
    # -- comment mettre le type date ? dateNaissC = models.CharField(max_length=100)
    # -- comment mettre le type email ? emailC = models.CharField(max_length=100)
    # -- comment mettre le type enumeration ? sexeC = models.IntegerField()
    adresseC = models.CharField(max_length=100)
    villeC = models.CharField(max_length=100)
    quartierC = models.CharField(max_length=100)
    #comment dire qu'un attribut est a valeur unique ? numCNI_C = models.CharField(max_length=100)
    telC = models.IntegerField()
    loginC = models.CharField(max_length=100)
    #comment mettre le type password ? motDePassC = models.CharField(max_length=100)
#----------------------------------------------------------------------

# (, )   // le fait qu’un client passe une commande
# (, , , , , , , , )



class PASSER(models.Model): #anullé
    #idC
    #idCmd

#---------------------------------------------------- deja fais
class LIVRAISON(models.Model):
    #numL = models.IntegerField()
    # -- comment mettre le type date ? dateL = models.CharField(max_length=100)
    descriptionL = models.CharField(max_length=100)
    montantL = models.IntegerField()
    typeL = models.CharField(max_length=100)
    #idC
    #idPoint
    #idL
    #idCmd
#-------------------------------------------------------

# (, , , , )
# (, , , , )

#--------------------------------------------------------- deja fais
class EVENEMENT(models.Model):
    #idEven = models.IntegerField()
    libEven = models.CharField(max_length=100)
    # -- comment mettre le type date ? dateEven = models.CharField(max_length=100)
    descriptionEven = models.CharField(max_length=256)
    #idA
#---------------------------------------------------------


#--------------------------------------------------------- deja fais
class RETOUR(models.Model):
    #idRetour = models.IntegerField()
    motifRetour = models.CharField(max_length=100)
    # -- comment mettre le type date ? dateRetour = models.CharField(max_length=100)
    # -- comment mettre le type enumeration ? statutRetour = models.IntegerField()
    #idC
#---------------------------------------------------------