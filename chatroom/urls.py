from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('',views.Sweet,name="Sweet"), #type this url----> http://127.0.0.1:8000
    path('room/',views.room), #type this url----> http://127.0.0.1:8000/room/
    path('contact',views.contact,name="form"),
    path('Orders/',views.Orders,name="Orders"),
    path('stock/',views.home,name="stock"),
    path('thanks/',views.thanks,name="thanks")
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)