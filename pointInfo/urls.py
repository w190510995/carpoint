from django.conf.urls import url
from . import views,views_classic_2

urlpatterns=[


    url(r'^index',views.index),
    url(r'^serch',views.conditionSerch),
    url(r'^pkCar',views.pkCar),
    url(r'^login',views.signin),
    url(r'^$', views.signin),
    url(r'^signin', views.signin),
    url(r'^sup',views.anlysit),
    url(r'^one',views.anlysit2),
    url(r'^many', views.anlysit3),
    url(r'^febakCarPoints', views.febakCarPoints),
    url(r'^carNum', views.carNumber),
    url(r'^febakSuppiles', views.febakSupplies),
    url(r'^pointSup', views.supPointsTest),
    url(r'^xcheckSingn',views.checkSingin),

    url(r'^te',views_classic_2.test1),

    url(r'^prod', views_classic_2.producer),
    url(r'^pointProd',views_classic_2.producerPoint),
    url(r'^febakProds',views_classic_2.febakProds),

    url(r'^samMac', views_classic_2.samMac),
    url(r'^pointSamMac',views_classic_2.samMacPoint),
    url(r'^febakSamMac',views_classic_2.febakSamMac),




]