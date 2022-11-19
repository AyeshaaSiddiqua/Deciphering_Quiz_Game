"""myquiz URL Configuration

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
from myapp import views
from .import settings
from django.conf.urls.static import static 
 
urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('', views.welcome),
    path('easyquiz/', views.quiz_easy),
    path('level/', views.level),
    path('save_ans/', views.save_ans),
    path('save_ans_A/', views.save_ans_A),
    path('save_ans_B/', views.save_ans_B),
    path('result/<int:lid>', views.result, name="result"),
    path('mediumquiz/', views.quiz_medium),
    path('hardquiz/', views.quiz_hard),
    path('quiz/<int:aid>/<int:bid>/', views.quiz_BattleFaceoff),
    path('battleresult/', views.battle_result),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

