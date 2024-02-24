from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Movie,Person,Reporter,POINT_DE_RETRAIT,AGENT_DESTINY,CLIENT,LIVREUR,PRESTATAIRE,MARQUE,CATEGORIE
from .models import SOUS_CATEGORIE,PANIER,EVENEMENT,RETOUR,COMMANDE,ARTICLE,CARACTERISTIQUE,DETAIL_COMMANDE,LIVRAISON
from .models import NOTIFICATION,VERSEMENT,FACTURE,DETAIL_P_A,DET_COM

#class UserSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = User
#        fields = ['url', 'username', 'email', 'groups']

class FACTURESerializer(serializers.ModelSerializer):
    class Meta:
        model = FACTURE
        fields = ['id', 'dateF', 'montantF','commande']


class VERSEMENTSerializer(serializers.ModelSerializer):
    class Meta:
        model = VERSEMENT
        fields = ['id', 'dateVers', 'typeVers','MontantVers','statutVers','commande','client']


class NOTIFICATIONSerializer(serializers.ModelSerializer):
    class Meta:
        model = NOTIFICATION
        fields = ['agent_destiny', 'prestataire', 'raisonNot','dateNot']


class LIVRAISONSerializer(serializers.ModelSerializer):
    class Meta:
        model = LIVRAISON
        fields = ['id', 'libeleL', 'dateL', 'descriptionL','montantL','typeL','client','point_de_retrait','livreur','commande']



class DETAIL_COMMANDESerializer(serializers.ModelSerializer):
    class Meta:
        model = DETAIL_COMMANDE
        fields = ['commande', 'caracteristique', 'qte_Commander']



class CARACTERISTIQUESerializer(serializers.ModelSerializer):
    class Meta:
        model = CARACTERISTIQUE
        fields = ['id', 'couleurCaract', 'photoCaract','tailleCaract','autreDetailCaract','prixCaract','qteCaract','nbAchatCaract','article']


class ARTICLESerializer(serializers.ModelSerializer):
    class Meta:
        model = ARTICLE
        fields = ['id', 'designationAr', 'photoAr','prixAr','qteAr','StockSecuriteAr','VideoPubAr','nbAchatAr','sous_categorie','marque']


class COMMANDESerializer(serializers.ModelSerializer):
    class Meta:
        model = COMMANDE
        fields = ['id', 'libCmd', 'dateCmd','statusCmd','descriptionCmd','montantLivraisonCmd','client','articles','caracteristiques']

class DET_COMSerializer(serializers.ModelSerializer):
    class Meta:
        model = DET_COM
        fields = ['id','commande', 'article', 'qteCom','couleurCom','tailleCom','prixCom','autreDetailCom']




class RETOURSerializer(serializers.ModelSerializer):
    class Meta:
        model = RETOUR
        fields = ['id', 'motifRetour', 'dateRetour','statutRetour','client']


class EVENEMENTSerializer(serializers.ModelSerializer):
    class Meta:
        model = EVENEMENT
        fields = ['id', 'libEven', 'dateEven','descriptionEve','agent_destiny']
   

class PANIERSerializer(serializers.ModelSerializer):
    class Meta:
        model = PANIER
        fields = ['id', 'libPanier', 'client','articles']


class DETAIL_P_ASerializer(serializers.ModelSerializer):
    class Meta:
        model = DETAIL_P_A
        fields = ['id', 'panier', 'article','qte','couleur','taille','prix','autreDetail']


class SOUS_CATEGORIESerializer(serializers.ModelSerializer):
    class Meta:
        model = SOUS_CATEGORIE
        fields = ['id', 'libSCat', 'photoSCat','categorie']


class CATEGORIESerializer(serializers.ModelSerializer):
    class Meta:
        model = CATEGORIE
        fields = ['id', 'libCat', 'photoCat']


class MARQUESerializer(serializers.ModelSerializer):
    class Meta:
        model = MARQUE
        fields = ['id', 'libMarq', 'photoMarq']


class PRESTATAIRESerializer(serializers.ModelSerializer):
    class Meta:
        model = PRESTATAIRE
        fields = ['id','nomP','prenomP','dateNaissP','emailP','sexeP','adresseP','villeP','quartierP','numCNI_P','telP','loginP','motDePassP']


class LIVREURSerializer(serializers.ModelSerializer):
    class Meta:
        model = LIVREUR
        fields = ['id','nomL','prenomL','dateNaissL','emailL','sexeL','adresseL','villeL','quartierL','numCNI_L','telL','loginL','motDePassL']


class CLIENTSerializer(serializers.ModelSerializer):
    class Meta:
        model = CLIENT
        fields = ['id','nomC','prenomC','dateNaissC','emailC','sexeC','adresseC','villeC','quartierC','numCNI_C','telC','loginC','motDePassC']



class AGENT_DESTINYSerializer(serializers.ModelSerializer):
    class Meta:
        model = AGENT_DESTINY
        fields = ['id','nomA','prenomA','dateNaissA','emailA','sexeA','adresseA','villeA','quartierA','numCNI_A','telA','loginA','motDePassA']



class POINT_DE_RETRAITSerializer(serializers.ModelSerializer):
    class Meta:
        model = POINT_DE_RETRAIT
        fields = ['id','libPoint','villePoint','quartierPoint','descriptionPoint','telPoint','mailPoint']


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'desc', 'year','autor']

class MovieMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title']

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields=['id','first_name','last_name','email']

class ReporterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporter
        fields=['id','first_name','pub_date','reporter']

# class ArticleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields=['id','headline','last_name','email']



#class GroupSerializer(serializers.HyperlinkedModelSerializer):
 #   class Meta:
  #      model = Group
   #     fields = ['url', 'name']