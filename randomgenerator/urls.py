from django.urls import path
from randomgenerator.views import ran_gen_view


urlpatterns = [
    path('', ran_gen_view, name='rangenview')
]
