from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic import DetailView
from django.views.generic import ListView
from .models import Material, AWS, Azure, Google
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import F
from django.utils import timezone
#from .forms import PostVote, NewPost, NewEntity, Speakers, AddUser
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt

#@xframe_options_exempt
def index(request):
    Intro = Material.objects.get(title='intro')
    Description = Material.objects.get(title='description')
    Advantage = Material.objects.get(title='advantage')
    Publicdis = Material.objects.get(title='publicdis')
    Privatedis = Material.objects.get(title='privatedis')
    Publicorprivate = Material.objects.get(title='publicorprivate')
    Author = Material.objects.get(title='author')
    Module = "index"
    context = {
        'Module': Module,
	'Intro': Intro,
        'Description': Description,
        'Advantage': Advantage,
        'Publicdis': Publicdis,
        'Privatedis': Privatedis,
	'Publicorprivate': Publicorprivate,
        'Author': Author,
    }
    return render(request, 'CloudasaService/index.html', context)

def virtualisation(request):
    Intro = Material.objects.get(title='history')
    Support = Material.objects.get(title='support')
    Storage = Material.objects.get(title='storage')
    context = {
        'Intro': Intro,
        'Support': Support,
        'Storage': Storage,
    }
    return render(request, 'CloudasaService/virtualisation.html', context)

def detail(request):
    Amazon = AWS.objects.order_by('title_date')[:11]
    MSA = Azure.objects.order_by('title_date')[:10]
    Google = Google.objects.order_by('title_date')[:10]
    Publicorprivate = Material.objects.get(title='publicorprivate')
    Services = Material.objects.get(title='services')
    Costs = Material.objects.get(title='costs')
    Module = "detail"
    context = {
        'Module': Module,
        'Publicorprivate': Publicorprivate,
        'Services': Services,
        'Costs': Costs,
	'Amazon': Amazon,
	'MSA': MSA,
	'Google': Google,
    }
    return render(request, 'CloudasaService/detail.html', context)

def virtual(request):
    Network = Material.objects.get(title='network')
    History = Material.objects.get(title='history')
    Storage = Material.objects.get(title='storage')
    Scalability = Material.objects.get(title='scalability')
    Provisioning = Material.objects.get(title='provisioning')
    Module = "virtual"
    context = {
        'Module': Module,
        'Network': Network,
        'History': History,
        'Storage': Storage,
        'Scalability': Scalability,
        'Provisioning': Provisioning,
    }
    return render(request, 'CloudasaService/virtual.html', context)

def description(request):
    Intro = Material.objects.get(title='description')
    context = {
        'Intro': Intro,
    }
    return render(request, 'CloudasaService/description.html', context)

def difference(request):
    Intro = Material.objects.get(title='whobenefits')
    context = {
        'Intro': Intro,
    }
    return render(request, 'CloudasaService/difference.html', context)

def author(request):
    Intro = Material.objects.get(title='author')
    context = {
        'Intro': Intro,
    }
    return render(request, 'CloudasaService/author.html', context)


def advantage(request):
    Intro = Material.objects.get(title='advantage')
    Manageability = Material.objects.get(title='manageability')
    Scalability = Material.objects.get(title='scalability')
    context = {
        'Intro': Intro,
        'Manageability': Manageability,
        'Scalability': Scalability,
    }
    return render(request, 'CloudasaService/advantage.html', context)

def businesscontinuity(request):
    Intro = Material.objects.get(title='publicorprivate')
    context = {
        'Intro': Intro,
    }
    return render(request, 'CloudasaService/businesscontinuity.html', context)

##@xframe_options_exempt
#def index(request):
#    if not request.user.is_authenticated():
#        userauth = 'no'
#    else:
#        userauth = 'yes'
#    latest_category_list = SiteCategories.objects.order_by('-category_date').exclude(category_name = 'New Entity')
#    good_category_trend = post.objects.filter(post_rating='Good').order_by('-post_update')[:15]
#    bad_category_trend = post.objects.filter(post_rating__contains='Bad').order_by('-post_update')[:15]
#    entities_list = Entities.objects.order_by('-good_vote_count')[:15]
#   recent_posts = post.objects.order_by('-post_create_date')[:15]
#   speakers_corner = SpeakersCorner.objects.latest('post_date')
#   who_are_we = SiteSpecific.objects.get(tag='About us...')
#   topics = Topical.objects.order_by('-post_date')[:4]
#   template = loader.get_template('GnB/index.html')
#   context = {
#       'userauth': userauth,
#	'good_category_trend': good_category_trend,
#	'bad_category_trend': bad_category_trend,
#        'latest_category_list': latest_category_list,
#	'entities_list': entities_list,
#        'recent_posts': recent_posts,
#        'speakers_corner': speakers_corner,
#	'topics': topics,
#        'who_are_we': who_are_we,
#    }
#    return render(request, 'GnB/index.html', context)

def advantage(request):
    Intro = Material.objects.get(title='advantage')
    Manageability = Material.objects.get(title='manageability')
    Scalability = Material.objects.get(title='scalability')
    context = {
        'Intro': Intro,
        'Manageability': Manageability,
        'Scalability': Scalability,
    }
    return render(request, 'CloudasaService/advantage.html', context)

def businesscontinuity(request):
    Intro = Material.objects.get(title='businesscontinuity')
    context = {
        'Intro': Intro,
    }
    return render(request, 'CloudasaService/businesscontinuity.html', context)

##@xframe_options_exempt
#def index(request):
#    if not request.user.is_authenticated():
#        userauth = 'no'
#    else:
#        userauth = 'yes'
#    latest_category_list = SiteCategories.objects.order_by('-category_date').exclude(category_name = 'New Entity')
#    good_category_trend = post.objects.filter(post_rating='Good').order_by('-post_update')[:15]
#    bad_category_trend = post.objects.filter(post_rating__contains='Bad').order_by('-post_update')[:15]
#    entities_list = Entities.objects.order_by('-good_vote_count')[:15]
#   recent_posts = post.objects.order_by('-post_create_date')[:15]
#   speakers_corner = SpeakersCorner.objects.latest('post_date')
#   who_are_we = SiteSpecific.objects.get(tag='About us...')
#   topics = Topical.objects.order_by('-post_date')[:4]
#   template = loader.get_template('GnB/index.html')
#   context = {
#       'userauth': userauth,
#	'good_category_trend': good_category_trend,
#	'bad_category_trend': bad_category_trend,
#        'latest_category_list': latest_category_list,
#	'entities_list': entities_list,
#        'recent_posts': recent_posts,
#        'speakers_corner': speakers_corner,
#	'topics': topics,
#        'who_are_we': who_are_we,
#    }
#    return render(request, 'GnB/index.html', context)
