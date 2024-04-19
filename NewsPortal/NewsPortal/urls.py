"""NewsPortal URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path


from newsapp.views import (
    # index,  show_category, show_post, addpage,
    about, archive,  contact, pageNotFound,
    PostsHome, PostCategory, ShowPost, AddPage,
    SignUpUser, LoginUser, logout_user
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostsHome.as_view(), name='home'),
    path('category/<slug:postCategory_slug>/',
         PostCategory.as_view(), name='category'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('addpage/', AddPage.as_view(), name='add_page'),

    # --------------------------------------------------------------------------------
    path('about/', about, name='about'),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive, name='archive'),
    path('contact/', contact, name='contact'),
    path('signup/', SignUpUser.as_view(), name='signup'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    # --------------------------------------------------------------------------------
    # Маршруты для представлений в виде функций
    # path('', index, name='home'),
    # path('post/<slug:post_slug>/', show_post, name='post'),
    # path('category/<slug:cat_slug>/', show_category, name='category'),
    # path('category/<int:cat_id>/', show_category, name='category'),
    # path('addpage/', addpage, name='add_page'),

]


handler404 = pageNotFound

# --------------------------------------------------------------------------------
# Этот код только на время отладки работы с медиа-файлами (пока DEBUG=True)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
