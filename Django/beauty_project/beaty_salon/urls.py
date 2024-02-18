from django.urls import path
from .views import beaty_view, master_view, contacts_view, price_view, master_update_view, reports_view,\
    master_detail, booking_view, home_section1, master_delete

urlpatterns = [
    path("", beaty_view, name="beaty"),
    path("home_post/<int:id>/", home_section1, name="home_post"),
    path("master/", master_view, name="master"),
    path("master_detail/<int:id>/", master_detail, name="master_detail"),
    path("master_update/<int:id>/", master_update_view, name="master_update"),
    path("master_delete/<int:id>/", master_delete, name="master_delete"),
    path("contacts/", contacts_view, name='contacts'),
    path("price/", price_view, name="price"),
    path("reports/", reports_view, name="reports"),
    path("booking/", booking_view, name="booking"),
]
