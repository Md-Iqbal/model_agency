from django.urls import path
from . import views
urlpatterns = [
    path('', views.IndexView, name='IndexView'),
    path('news/', views.NewsView, name='NewsView'),
    path('news/<int:pk>/', views.NewsDetailView, name='NewsDetailView'),
    path('review/<int:pk>', views.ReviewCreateView, name='ReviewCreateView'),
    path('contact/', views.ContactView, name='ContactView'),
    path('models/', views.ModelView, name='ModelView'),
    path('models/<int:pk>', views.ModelDetailView, name='ModelDetailView'),
    path('about-us/', views.AboutView, name='AboutView'),
    path('faq/', views.FAQView, name='FaqView'),
]
