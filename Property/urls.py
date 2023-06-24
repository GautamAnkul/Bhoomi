from django.conf import settings
from django.conf.urls.static import static
from Property.views import *
from django.urls import path



# Path

urlpatterns = [
    path("state", GetStateView.as_view(), name="state"),
    path("category", GetCategoryView.as_view(), name="category"),
    path("city/<int:id>", GetCityView.as_view(), name="city"), 
    path('getdata/',GetDataApiview.as_view(),name='getdata'),
    path('getdatabycategory/',GetDataByCategoryView.as_view(),name='getdata'),
    path("contactus/",GetContactUsView.as_view(), name="contactus"),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
