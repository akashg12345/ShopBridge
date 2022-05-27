"""ShopBridge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from inventory.apiviews import ItemsCreate,ItemsList,ItemsUpdate,ItemsRetrieve,ItemsDestroy,student_api_view


urlpatterns = [
## -----------------------------  urls for concrete apiview -------------------------------------
    
    path('admin/', admin.site.urls),
    # for function based url
    path("retrieve_view/<int:pk>/",student_api_view),
    path("retrieve_view/",student_api_view),
    # for class based url
    path('item-list/',ItemsList.as_view()),
    path('item-create/',ItemsCreate.as_view()),
    path('item-retrieve/<int:pk>/',ItemsRetrieve.as_view()),
    path('item-update/<int:pk>/',ItemsUpdate.as_view()),
    path('item-delete/<int:pk>/',ItemsDestroy.as_view()),
]



