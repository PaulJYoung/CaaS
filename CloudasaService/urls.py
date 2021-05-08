from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib.sitemaps.views import sitemap

from . import views

app_name = 'CloudasaService'
urlpatterns = [
#   url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^$', views.index, name='index'),
    url(r'^cloud-as-a-service-providers/$', views.detail, name='detail'),
    url(r'^cloud-as-a-service-cloud-specifics/$', views.virtual, name='virtual'),
    url(r'^advantage/$', views.advantage, name='advantage'),
    url(r'^virtualisation/$', views.virtualisation, name='virtualisation'),
    url(r'^description/$', views.description, name='description'),
    url(r'^difference/$', views.difference, name='difference'),
    url(r'^the-author-paul-young/$', views.author, name='author'),
    url(r'^CaaS/author/$', views.author, name='author'),
    url(r'^contact-cloud-as-a-service/$', views.contactview, name='contactview'),
    url(r'^businesscontinuity/$', views.businesscontinuity, name='businesscontinuity'),
#    url(r'^(?P<postid>[0-9]+)/$', views.postview, name='postview'),
#    url(r'^createpost/$', views.newpost, name='newpost'),
#    url(r'^speak/(?P<postid>[0-9]+)/$', views.speakerscorner, name='speakerscorner'),
#    url(r'^speak/$', views.speakerscorner, name='speakerscorner'),
#    url(r'^(?P<postid>[0-9]+)/thanks/$', views.thankyoupage, name='thanks'),
#    url(r'^(?P<postid>[0-9]+)/thankspeak/$', views.thankyouspeak, name='thanks'),
#    url(r'^(?P<postid>[0-9]+)/postthanks/$', views.postthanks, name='postthanks'),
#    url(r'^(?P<postid>[0-9]+)/newentity/$', views.newentity, name='newentity'),
#    url(r'^(?P<postid>[0-9]+)/site/$', views.pageview, name='pageview'),
#    url(r'^topic/(?P<postid>[0-9]+)/$', views.topicview, name='topicview'),
#    url(r'^entity/(?P<postid>[0-9]+)/$', views.entityview, name='entityview'),
#    url(r'^entitycat/(?P<entid>[0-9]+)/$', views.entityviewcat, name='entityviewcat'),
#    url(r'^topentity/(?P<entid>[0-9]+)/$', views.topentityview, name='topentityview'),
#    url(r'^category/(?P<catid>[0-9]+)/$', views.categoryview, name='categoryview'),
#    url(r'^thanks/$', views.thankyoupage, name='thanks'),
#    url(r'^adduser/$', views.adduser, name='adduser'),
#    url(r'^login/$', auth_views.login, {'template_name': 'GnB/login.html', 'redirect_field_name': '/GnB/'}),
#    url(r'^logout/$', auth_views.logout, {'template_name': 'GnB/logout.html', 'redirect_field_name': '/GnB/'}),
#    url('^', include('django.contrib.auth.urls')),
#    url(r'^add/$', views.ListEntities, name='addentity'),
]
