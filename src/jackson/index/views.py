from urllib import response
from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.utils.html import strip_tags
from django.utils.translation import activate
from django.contrib.auth import logout

from.models import Hours, Review, EmailList, Promotion, Tag, Article, Photos

from .forms import ContactForm

# from invoice.models import Promotion

# Create your views here.
def test_view(request):
    context = {}

    return render(request, 'test.html', context)

def home_view(request):
    # Email Modal Coupon
    if request.method == 'POST':
        if 'coupon_email' in request.POST:
            coupon_email=request.POST.get('coupon_email').lower()
            EmailList.objects.create_emaillist(coupon_email)
            subject = "Lens Lab Express | 10% Off"
            message_plain = render_to_string('email.txt')
            message_html = render_to_string('email.html')
            sender = "llejh.noreply@gmail.com"
            recipient = coupon_email

            try: 
                send_mail(subject, message_plain, sender, [recipient], html_message=message_html)
            except:
                print("Email Failed To Send")

    hours = Hours.objects.filter(visible=True)[0]
    reviews = Review.objects.filter(visible=True)

    photos = Photos.objects.filter(visible=True)

    context = {"hours": hours,
               "reviews": reviews,
               "photos": photos,
               "view_name": "home_view"}

    return render(request, 'home.html', context) 


def promotions_view(request):
    hours = Hours.objects.filter(visible=True)[0]
    promotions = Promotion.objects.order_by('end_date').filter(visible=True)

    context = { "hours": hours,
                "promotions": promotions,
                "view_name": "promotions_view"
                }
    return render(request, 'promos.html', context)

from django.core.paginator import Paginator

def library_index(request):
    hours = Hours.objects.filter(visible=True)[0]

    # # Get The First 10 Visible Articles, Sorted By Publish Date
    # articles = Article.objects.filter(visible=True).order_by('-publish_date')[:10]

    articles= Article.objects.order_by('-publish_date').all()
    paginator = Paginator(articles, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)


    context = { "hours": hours,
                # "articles": articles
                "page_obj": page_obj
                }
    return render(request, 'library.html', context)

# def library_article(request, article_id):
#     hours = Hours.objects.filter(visible=True)[0]

#     article = Article.objects.get(id=article_id)

#     context = { "hours": hours,
#                 "article": article
#                 }
#     return render(request, 'article.html', context)

def library_article(request, slug):
    hours = Hours.objects.filter(visible=True)[0]

    article = Article.objects.get(slug=slug)

    context = { "hours": hours,
                "article": article
                }
    return render(request, 'article.html', context)

def logout_view(request):
    #Logout and Redirect home
    logout(request)
    return redirect('/')


def about_view(request):
    hours = Hours.objects.filter(visible=True)[0]
   
    if request.method == 'POST':
        print(request.POST)
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            

            
            subject = "New Contact Us Message From " + name
            sender = 'llejh.noreply@gmail.com'
            # recipient = ['llejh.noreply@gmail.com', 'lenslabexpressjacksonheights@gmail.com', 'ctash98@gmail.com']
            recipient = ['llejh.noreply@gmail.com', 'ctash98@gmail.com']
            html_message = render_to_string('contact_email.html', {'name': name, 'email': email, 'phone': phone, 'message': message})
            plain_message = strip_tags(html_message)

            try: 
                send_mail(
                    subject, 
                    plain_message, 
                    sender, 
                    recipient, 
                    html_message=html_message
                    )
                print("Email Sent From " + sender + " To: " + recipient)
            except:
                print("Contact Email Failed To Send")




            return render(request, 'about.html', {'form_sent': True, 'form': form, 'hours': hours, "view_name": "about_view"})
    else:
        print(request.POST)
        form = ContactForm()
    return render(request, 'about.html', {'form_sent': False, 'form': form, 'hours': hours, "view_name": "about_view"})
    
    
    