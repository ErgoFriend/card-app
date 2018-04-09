from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Card, Request, ProgrammingLanguage, Tag, Category
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User
# Create your views here.
@login_required
def index(request):
    new_cards = Card.objects.order_by('-card_date')
    new_requests = Request.objects.order_by('-request_date')
    #ranked_cards = Card.objects.order_by('liked')
    if request.method == 'POST':
        if 'create_card_btn' in request.POST:
            card = Card(
                title=request.POST['cardtitle'],
                content=request.POST['cardcontent'],
                #card_tag=request.POST['cardtag'],
                #card_category=request.POST['cardcategory'],
                user = request.user,
                card_date=timezone.now())
            card.save()
        if 'create_request_btn' in request.POST:
            request_a = Request(
                title=request.POST['requesttitle'],
                content=request.POST['requestcontent'],
                #request_tag=request.POST['requesttag'],
                #request_category=request.POST['requestcategory'],
                user = request.user,
                request_date=timezone.now())
            request_a.save()
    context = {
            'cards':new_cards,
            'requests':new_requests,
        }
    return render(request,'iniita/index.html',context)

@login_required
def create(request):
    tags = Tag.objects.all()
    categories = Category.objects.all()
    if request.method == 'POST':
        if 'button' in request.POST:
            card = Card(
                title=request.POST['title'],
                content=request.POST['content'],
                #card_tag=request.POST['tag'],
                #card_category=request.POST['category'],
                user = request.user.id,
                card_date=timezone.now())
            card.save()
        if 'button_1' in request.POST:
            tag = Tag(
                name=request.POST['tagname'])
            tag.save()
        if 'button_2' in request.POST:
            category = Category(
                name=request.POST['categoryname'])
            category.save()
    context = {
        'tags':tags,
        'categories':categories
    }
    return render(request,'iniita/create.html',context)

@login_required
def detail(request,card_id):
    try:
        card = Card.objects.get(pk=card_id)
    except Card.DoesNotExist:
        raise Http404("Card does not exist")
    context = {
        'card': card,
    }
    return render(request,'iniita/detail.html', context)

@login_required
def update(request,card_id):
    try:
        card = Card.objects.get(pk=carde_id)
    except Card.DoesNotExist:
        raise Http404("Card does not exist")
    if request.method == 'POST':
        card.title = request.POST['title']
        card.text= request.POST['content']
        card.save()
        return HttpResponseRedirect(reverse(detail, args=[card_id]))
    context = {
        'card': card
    }
    return render(request, 'iniita/index.html', context)

def delete(request,card_id):
    try:
        card = Card.objects.get(pk=card_id)
        card.delete()
    except Card.DoesNotExist:
        raise Http404("Card does not exist")
    return HttpResponseRedirect(reverse(index))

@login_required
def test(request):
    return render(request,'iniita/test.html')

@login_required
def mypage(request):
    user = request.user
    #cards = Card.objects.get(user=user)
    cards = Card.objects.all()
    context = {
        #'cards' : cardss,
        'cards' : cards,
        'user' : user,
    }
    print("-----------")
    print(user)
    print(User.cards)
    print(cards)
    print("-----------")
    return render(request,'iniita/mypage.html',context)