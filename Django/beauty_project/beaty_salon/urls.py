from django.urls import path
from .views import beaty_view, master_view, contacts_view, price_view, master_update_view, reports_view,\
    master_detail, booking_view

urlpatterns = [
    path("", beaty_view, name="beaty"),
    path("booking/", booking_view, name="booking"),
    path("master/", master_view, name="master"),
    path("master_detail/<int:id>/", master_detail, name="master_detail"),
    path("contacts/", contacts_view, name='contacts'),
    path("price/", price_view, name="price"),
    path("master_update/<int:id>/", master_update_view, name="master_update"),
    path("reports/", reports_view, name="reports"),
]
