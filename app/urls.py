from django.urls import path
from app import views

urlpatterns=[
    path('cus/',views.cusinsert),
    path('pro/',views.proinsert),
    # path('ptab/',views.pinsert.as_view())
    path('cr/<int:pk>/',views.crd.as_view()),
    path('pr/<int:pk>/',views.pr.as_view()),
    path('cup/<int:pk>/',views.cup.as_view()),
    path('pup/<int:pk>/',views.pup.as_view())
]