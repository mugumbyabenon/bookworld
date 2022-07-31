from  django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('register/',views.register,name='register'),
    path('student_register/', views.student_register.as_view(), name = 'student_register'),
    path('login/', views.login_view, name='login'),
    path('librarain/', views.librarain, name='librarain'),
    path('student/', views.student, name='student'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('activate/<uid64>/<token>', views.activate, name="activate"),
    path('resend/', views.resend)
]