from django.urls import path
from .views import MainView, PostDetailView, SignUpView, SignInView, FeedBackView, SuccessView,create_post #PostCreate
from django.contrib.auth.views import LogoutView
from django.conf import settings
from . import views

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('signout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='signout',),
    path('contact/', FeedBackView.as_view(), name='contact'),
    path('contact/success/', SuccessView.as_view(), name='success'),
    # path('create/', PostCreate.as_view(), name='post_create'),
    path('create/', views.create_post, name='post_create'),
    path('<slug>/', PostDetailView.as_view(), name='post_detail'),
    # path('<slug>/update/', views.update_post, name='update_post'),
]