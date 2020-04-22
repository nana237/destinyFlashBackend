# """djangoDestinyFlash URL Configuration
# 
# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/3.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

#urlpatterns = [
   # path('admin/', admin.site.urls),
#]


from django.urls import include, path
from rest_framework import routers
from store import views

router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
router.register(r'movies', views.MovieViewSet)
router.register(r'persons',views.PersonViewSet)
# router.register(r'articles',views.ArticleViewSet)
router.register(r'reporters',views.ReporterViewSet)
router.register(r'point_de_retraits',views.POINT_DE_RETRAITViewSet)
router.register(r'agent_destinys',views.AGENT_DESTINYViewSet)
router.register(r'clients',views.CLIENTViewSet)
router.register(r'livreurs',views.LIVREURViewSet)
router.register(r'prestataires',views.PRESTATAIREViewSet)
router.register(r'marques',views.MARQUEViewSet)
router.register(r'categories',views.CATEGORIEViewSet)
router.register(r'sous_categories',views.SOUS_CATEGORIEViewSet)
router.register(r'paniers',views.PANIERViewSet)
router.register(r'evenements',views.EVENEMENTViewSet)
router.register(r'retours',views.RETOURViewSet)
router.register(r'commandes',views.COMMANDEViewSet)
router.register(r'articles',views.ARTICLEViewSet)
router.register(r'caracteristiques',views.CARACTERISTIQUEViewSet)
router.register(r'details_commandes',views.DETAIL_COMMANDEViewSet)
router.register(r'livraisons',views.LIVRAISONViewSet)
router.register(r'notifications',views.NOTIFICATIONViewSet)
router.register(r'versements',views.VERSEMENTViewSet)
router.register(r'factures',views.FACTUREViewSet)








# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
     path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)