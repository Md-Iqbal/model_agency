from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,reverse
from .models import *
# Create your views here.

def IndexView(request):
    random_model = ModelInfo.objects.order_by('?')[:6]
    news = News.objects.order_by('-created')[:2]
    context = {
        'random_model': random_model,
        'news': news,
    }
    return render(request, 'Home.html', context)

def NewsView(request):
    try:
        news = News.objects.all()
        context = {
            'news': news
        }
        return render(request, 'Blog.html', context)
    except:
        print('News not found')
        return render(request, 'Blog.html')
        
def NewsDetailView(request, pk):
    print(pk)
    news = News.objects.get(pk=pk)
    reviews = Review.objects.filter(news=news)
    print(news)
    print("Reviews ===> ",reviews)
    context = {
        'news': news, 
        'reviews': reviews
    }
    return render(request, 'Single_Blog.html', context)


def ReviewCreateView(request, pk):
    if request.method == 'POST':
        print("request is printing =====> ",request.POST)
        news = News.objects.get(pk=pk)
        print(news)
        user = request.user
        userprofile = UserProfile.objects.get(user=user)
        #create new review for the news
        review = Review.objects.create(
            news=news,
            title=request.POST['title'],
            content=request.POST['review_message'],
            author=userprofile,
            image=request.FILES['image']
        )
        print("new review____>>>>> ",review)
        messages.success(request, 'Your review has been sent successfully. Check given email for further details.')
        return HttpResponseRedirect(reverse('NewsDetailView', args=(pk,)))

def ContactView(request, *args, **kwargs):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('review_message')
        print(name, email, message)
        contact = Contact.objects.create(
            name=name,
            email=email,
            message=message
        )
        print("new contact____>>>>> ",contact)
        messages.success(request, 'Your message has been sent successfully. Check given email for further details.')
        return HttpResponseRedirect(reverse('ContactView'))
    else:
        return render(request, 'Contact.html')

def ModelView(request):
    model = ModelInfo.objects.all()
    context = {
        'model': model
    }
    return render(request, 'Models.html', context)


def ModelDetailView(request, pk):
    model = ModelInfo.objects.get(pk=pk)
    ## random model 4 object
    model_random = ModelInfo.objects.order_by('?')[:4]
    context = {
        'model': model,
        'model_random': model_random
    }
    return render(request, 'Model_Profile.html', context)

def AboutView(request):
    return render(request, 'About.html')


def FAQView(request):
    return render(request, 'FAQ.html')