"""CreditCardProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cardapp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('addcardtypes/',AddCardTypesView.as_view()),
    path('listallcardrequests/',ListAllCardRequestsView.as_view()),
    path('acceptcardrequest/<int:pk>/',AcceptCardRequestView.as_view()),
    path('rejectcardrequest/<int:pk>/',RejectCardRequestView.as_view()),
    path('listlimitincreaserequests/',ListLimitIncreaseRequestsView.as_view()),
    path('listallblockedcards/',ListAllBlockedCardsView.as_view()),
    path('unblockcard/<int:pk>/',UnBlockCardView.as_view()),
    path('acceptincreasecardlimitrequest/<int:pk>/',AcceptIncreaseCardLimitRequestView.as_view()),
    path('rejectincreasecardlimitrequest/<int:pk>/',RejectIncreaseCardLimitRequestView.as_view()),
    path('customerregistration/',CustomerRegistrationView.as_view()),
    path('applyforcard/',ApplyForCardView.as_view()),
    path('listallcardtypes/',ListCardsAndStatusView.as_view()),
    path('getstatus/<int:pk>/',ListCardsAndStatusView.as_view()),
    path('blockcard/<int:pk>/',BlockCardView.as_view()),
    path('requestforincreselimit/',RequestForIncreaseLimitView.as_view()),
]
