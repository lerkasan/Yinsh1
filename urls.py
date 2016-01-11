from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from game import views

#urlpatterns = [
#    url(r'^ajax/onclick', onclick),
#]

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^play/', views.play),
    url(r'^ajax/', views.ajax),
    url(r'^close/', views.close),
    url(r'^$', views.index),
]


#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
