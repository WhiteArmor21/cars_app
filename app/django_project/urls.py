from django.contrib import admin
from django.urls import path
from mailing.views import car_request_view
from products.views import CarsListView


urlpatterns = [
    path('mailing/', car_request_view),
    path('products/', CarsListView.as_view()),
    path('admin/', admin.site.urls),
]
