# from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
#from tutorial.quickstart.serializers import UserSerializer, GroupSerializer
#from store.serializers import UserSerializer
from store.serializers import MovieSerializer,MovieMiniSerializer,PersonSerializer,ReporterSerializer,POINT_DE_RETRAITSerializer
from store.serializers import AGENT_DESTINYSerializer,CLIENTSerializer,LIVREURSerializer,PRESTATAIRESerializer,MARQUESerializer,CATEGORIESerializer
from .models import Movie,Person,Reporter,POINT_DE_RETRAIT,AGENT_DESTINY,CLIENT,LIVREUR,PRESTATAIRE,MARQUE,CATEGORIE
from store.serializers import SOUS_CATEGORIESerializer,PANIERSerializer,EVENEMENTSerializer,RETOURSerializer,COMMANDESerializer,ARTICLESerializer
from store.serializers import CARACTERISTIQUESerializer,DETAIL_COMMANDESerializer,LIVRAISONSerializer,NOTIFICATIONSerializer,VERSEMENTSerializer,FACTURESerializer,DETAIL_P_ASerializer,DET_COMSerializer
from .models import SOUS_CATEGORIE,PANIER,EVENEMENT,RETOUR,COMMANDE,ARTICLE,CARACTERISTIQUE,DETAIL_COMMANDE,LIVRAISON,NOTIFICATION,VERSEMENT,FACTURE,DETAIL_P_A,DET_COM
from rest_framework.response import Response

class FACTUREViewSet (viewsets.ModelViewSet):
    queryset = FACTURE.objects.all()
    serializer_class = FACTURESerializer

    def list(self, request, *args, **kwargs):
        factures = FACTURE.objects.all()
        serializer = FACTURESerializer(factures, many=True)
        return Response(serializer.data)

class VERSEMENTViewSet (viewsets.ModelViewSet):
    queryset = VERSEMENT.objects.all()
    serializer_class = VERSEMENTSerializer

    def list(self, request, *args, **kwargs):
        versements = VERSEMENT.objects.all()
        serializer = VERSEMENTSerializer(versements, many=True)
        return Response(serializer.data)

class NOTIFICATIONViewSet (viewsets.ModelViewSet):
    queryset = NOTIFICATION.objects.all()
    serializer_class = NOTIFICATIONSerializer

    def list(self, request, *args, **kwargs):
        notifications = NOTIFICATION.objects.all()
        serializer = NOTIFICATIONSerializer(notifications, many=True)
        return Response(serializer.data)

class LIVRAISONViewSet (viewsets.ModelViewSet):
    queryset = LIVRAISON.objects.all()
    serializer_class = LIVRAISONSerializer

    def list(self, request, *args, **kwargs):
        livraisons = LIVRAISON.objects.all()
        serializer = LIVRAISONSerializer(livraisons, many=True)
        return Response(serializer.data)

class DETAIL_COMMANDEViewSet (viewsets.ModelViewSet):
    queryset = DETAIL_COMMANDE.objects.all()
    serializer_class = DETAIL_COMMANDESerializer

    def list(self, request, *args, **kwargs):
        details_commandes = DETAIL_COMMANDE.objects.all()
        serializer = DETAIL_COMMANDESerializer(details_commandes, many=True)
        return Response(serializer.data)

class CARACTERISTIQUEViewSet (viewsets.ModelViewSet):
    queryset = CARACTERISTIQUE.objects.all()
    serializer_class = CARACTERISTIQUESerializer

    def list(self, request, *args, **kwargs):
        caracteristiques = CARACTERISTIQUE.objects.all()
        serializer = CARACTERISTIQUESerializer(caracteristiques, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        article = request.data['article']
        nbAchatCaract = request.data['nbAchatCaract']
        qteCaract = request.data['qteCaract']
        prixCaract = request.data['prixCaract']
        autreDetailCaract = request.data['autreDetailCaract']
        tailleCaract = request.data['tailleCaract']
        photoCaract = request.data['photoCaract']
        couleurCaract = request.data['couleurCaract']
        CARACTERISTIQUE.objects.create(couleurCaract=couleurCaract,photoCaract=photoCaract,tailleCaract=tailleCaract,autreDetailCaract=autreDetailCaract,
         prixCaract=prixCaract,qteCaract=qteCaract,nbAchatCaract=nbAchatCaract,article=article)

        return HttpResponse({'message': 'article created'}, status=200)



class ARTICLEViewSet (viewsets.ModelViewSet):
    queryset = ARTICLE.objects.all()
    serializer_class = ARTICLESerializer

    def list(self, request, *args, **kwargs):
        articles = ARTICLE.objects.all()
        serializer = ARTICLESerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        marque = request.data['marque']
        sous_categorie = request.data['sous_categorie']
        nbAchatAr = request.data['nbAchatAr']
        VideoPubAr = request.data['VideoPubAr']
        StockSecuriteAr = request.data['StockSecuriteAr']
        qteAr = request.data['qteAr']
        prixAr = request.data['prixAr']
        photoAr = request.data['photoAr']
        designationAr = request.data['designationAr']
        ARTICLE.objects.create(designationAr=designationAr,photoAr=photoAr,prixAr=prixAr,qteAr=qteAr, StockSecuriteAr=StockSecuriteAr,VideoPubA=VideoPubArr,nbAchatAr=nbAchatAr,sous_categorie=sous_categorie,marque=marque)

        return HttpResponse({'message': 'article created'}, status=200)


class COMMANDEViewSet (viewsets.ModelViewSet):
    queryset = COMMANDE.objects.all()
    serializer_class = COMMANDESerializer

    def list(self, request, *args, **kwargs):
        commandes = COMMANDE.objects.all()
        serializer = COMMANDESerializer(commandes, many=True)
        return Response(serializer.data)

class DET_COMViewSet (viewsets.ModelViewSet):
    queryset = DET_COM.objects.all()
    serializer_class = DET_COMSerializer

    def list(self, request, *args, **kwargs):
        detcoms = DET_COM.objects.all()
        serializer = DET_COMSerializer(detcoms, many=True)
        return Response(serializer.data)

class RETOURViewSet (viewsets.ModelViewSet):
    queryset = RETOUR.objects.all()
    serializer_class = RETOURSerializer

    def list(self, request, *args, **kwargs):
        retours = RETOUR.objects.all()
        serializer = RETOURSerializer(retours, many=True)
        return Response(serializer.data)

class EVENEMENTViewSet (viewsets.ModelViewSet):
    queryset = EVENEMENT.objects.all()
    serializer_class = EVENEMENTSerializer

    def list(self, request, *args, **kwargs):
        evenements = EVENEMENT.objects.all()
        serializer = EVENEMENTSerializer(evenements, many=True)
        return Response(serializer.data)

class PANIERViewSet (viewsets.ModelViewSet):
    queryset = PANIER.objects.all()
    serializer_class = PANIERSerializer

    def list(self, request, *args, **kwargs):
        paniers = PANIER.objects.all()
        serializer = PANIERSerializer(paniers, many=True)
        return Response(serializer.data)

class DETAIL_P_AViewSet (viewsets.ModelViewSet):
    queryset = DETAIL_P_A.objects.all()
    serializer_class = DETAIL_P_ASerializer

    def list(self, request, *args, **kwargs):
        detail_p_as = DETAIL_P_A.objects.all()
        serializer = DETAIL_P_ASerializer(detail_p_as, many=True)
        return Response(serializer.data)

class SOUS_CATEGORIEViewSet (viewsets.ModelViewSet):
    queryset = SOUS_CATEGORIE.objects.all()
    serializer_class = SOUS_CATEGORIESerializer

    def list(self, request, *args, **kwargs):
        sous_categories = SOUS_CATEGORIE.objects.all()
        serializer = SOUS_CATEGORIESerializer(sous_categories, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        libSCat = request.data['libSCat']
        photoSCat = request.data['photoSCat']
        categorie = request.data['categorie']
        
        CATEGORIE.objects.create(libSCat=libSCat,photoSCat=photoSCat,categorie=categorie)

        return HttpResponse({'message': 'sous_categorie created'}, status=200)


class CATEGORIEViewSet (viewsets.ModelViewSet):
    queryset = CATEGORIE.objects.all()
    serializer_class = CATEGORIESerializer

    def list(self, request, *args, **kwargs):
        categories = CATEGORIE.objects.all()
        serializer = CATEGORIESerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        libCat = request.data['libCat']
        photoCat = request.data['photoCat']
        
        CATEGORIE.objects.create(libCat=libCat,photoCat=photoCat)

        return HttpResponse({'message': 'categorie created'}, status=200)


class MARQUEViewSet (viewsets.ModelViewSet):
    queryset = MARQUE.objects.all()
    serializer_class = MARQUESerializer

    def list(self, request, *args, **kwargs):
        marques = MARQUE.objects.all()
        serializer = MARQUESerializer(marques, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        libMarq = request.data['libMarq']
        photoMarq = request.data['photoMarq']
        
        CATEGORIE.objects.create(libMarq=libMarq,photoMarq=photoMarq)

        return HttpResponse({'message': 'marque created'}, status=200)

class PRESTATAIREViewSet (viewsets.ModelViewSet):
    queryset = PRESTATAIRE.objects.all()
    serializer_class = PRESTATAIRESerializer

    def list(self, request, *args, **kwargs):
        prestataires = PRESTATAIRE.objects.all()
        serializer = PRESTATAIRESerializer(prestataires, many=True)
        return Response(serializer.data)

class LIVREURViewSet (viewsets.ModelViewSet):
    queryset = LIVREUR.objects.all()
    serializer_class = LIVREURSerializer

    def list(self, request, *args, **kwargs):
        livreurs = LIVREUR.objects.all()
        serializer = LIVREURSerializer(livreurs, many=True)
        return Response(serializer.data)

class CLIENTViewSet (viewsets.ModelViewSet):
    queryset = CLIENT.objects.all()
    serializer_class = CLIENTSerializer

    def list(self, request, *args, **kwargs):
        clients = CLIENT.objects.all()
        serializer = CLIENTSerializer(clients, many=True)
        return Response(serializer.data)

class AGENT_DESTINYViewSet (viewsets.ModelViewSet):
    queryset = AGENT_DESTINY.objects.all()
    serializer_class = AGENT_DESTINYSerializer

    def list(self, request, *args, **kwargs):
        agent_destinys = AGENT_DESTINY.objects.all()
        serializer = AGENT_DESTINYSerializer(agent_destinys, many=True)
        return Response(serializer.data)

class POINT_DE_RETRAITViewSet (viewsets.ModelViewSet):
    queryset = POINT_DE_RETRAIT.objects.all()
    serializer_class = POINT_DE_RETRAITSerializer

    def list(self, request, *args, **kwargs):
        point_de_retraits = POINT_DE_RETRAIT.objects.all()
        serializer = POINT_DE_RETRAITSerializer(point_de_retraits, many=True)
        return Response(serializer.data)

class MovieViewSet (viewsets.ModelViewSet):
    queryset=Movie.objects.all()
    serializer_class = MovieSerializer

    def list(self, request, *args, **kwargs):
        movies = Movie.objects.all()
        serializer = MovieMiniSerializer(movies, many=True)
        return Response(serializer.data)

class PersonViewSet (viewsets.ModelViewSet):
    queryset=Person.objects.all()
    serializer_class = PersonSerializer
    
    def list(self, request, *args, **kwargs):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

#class ArticleViewSet (viewsets.ModelViewSet):
#    queryset=Article.objects.all()
#    serializer_class = ArticleSerializer
#    
#    def list(self, request, *args, **kwargs):
#        articles = Article.objects.all()
#        serializer = ArticleSerializer(articles, many=True)
#        return Response(serializer.data)

class ReporterViewSet (viewsets.ModelViewSet):
    queryset=Reporter.objects.all()
    serializer_class = ReporterSerializer
    
    def list(self, request, *args, **kwargs):
        reporters = Reporter.objects.all()
        serializer = ReporterSerializer(reporters, many=True)
        return Response(serializer.data)
    


#class UserViewSet(viewsets.ModelViewSet):
#    """
#    API endpoint that allows users to be viewed or edited.
#    """
#    queryset = User.objects.all().order_by('-date_joined')
#    serializer_class = UserSerializer
#    permission_classes = [permissions.IsAuthenticated]




#class GroupViewSet(viewsets.ModelViewSet):
#    """
#    API endpoint that allows groups to be viewed or edited.
#    """
#    queryset = Group.objects.all()
#    serializer_class = GroupSerializer
#    permission_classes = [permissions.IsAuthenticated]

    