from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name='home'),	
    path('entradadados/', views.entradadados, name='entradadados'),
    path('altera/', views.altera, name='altera'),
    path('consulta/', views.consulta, name='consulta'),
    path('exclusao/', views.exclusao, name='exclusao'),       

]   