from django.urls import path
from randomgenerator.views import ticket_update_view, \
    ticket_list_view, ran_gen_view, book_detail_view, update_ticket_price


urlpatterns = [
    path('', ran_gen_view, name='rangenview'),
    path('list/', ticket_list_view, name='list'),
    path('detail/<int:num>', book_detail_view, name='detail'),
    path('update/', ticket_update_view, name='update'),
    path('up/', update_ticket_price, name='update_price'),
]
