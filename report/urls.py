from django.conf.urls import url
import views as qc_views

urlpatterns = [

    url(r'^$', qc_views.index, name='index'),
]