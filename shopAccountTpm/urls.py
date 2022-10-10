from django.urls import path
from shopAccountTpm import views

urlpatterns=[
    # url(r'^accounts/$', views.AccountApi),
    # url(r'^labours/$', views.LabourApi)
    path('accounts/',views.AccountApi),
    path('accounts/<int:id>',views.AccountApi),
    path('labours/',views.LabourApi),
    path('labours/<int:id>',views.LabourApi)

]