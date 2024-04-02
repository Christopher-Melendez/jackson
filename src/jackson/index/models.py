from django.db import models
from django.utils import timezone
from django.urls import reverse

from ckeditor_uploader.fields import RichTextUploadingField



# Create your models here.

class ReviewManager(models.Manager):
    def create_review(self, author, img, text, link):
        promotion = self.create(author=author, img=img, text=text, link=link)
        return Review

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.CharField(default="Claire", max_length=100)
    img = models.TextField(default="https://lh3.googleusercontent.com/a/ACg8ocJXZofFupD7SwebKyeqFM7evCP_HUPW0Hkfn-YPVUIl=w68-h68-p-rp-mo-br100", blank=False)
    en_text = models.TextField(default="The Best Shop on the block!", blank=False)
    es_text = models.TextField(default="The Best Shop on the block!", blank=False)
    link = models.TextField(default="https://lh3.googleusercontent.com/a/ACg8ocJXZofFupD7SwebKyeqFM7evCP_HUPW0Hkfn-YPVUIl=w68-h68-p-rp-mo-br100", blank=False)
    visible = models.BooleanField(default=True)

    objects = ReviewManager()
    
    def __str__(self):
         return self.author
    
class HoursManager(models.Manager):
    def create_hours(self, monday, tuesday, wednesday, thursday, friday, saturday, sunday, visible):
        hours = self.create(monday=monday, tuesday=tuesday, wednesday=wednesday, thursday=thursday, friday=friday, saturday=saturday, sunday=sunday, visible=visible)
        return Hours
    
class Hours(models.Model):
    id = models.AutoField(primary_key=True)
    monday = models.CharField(default="10:30 am - 6:30 pm", blank=False, max_length=100)
    tuesday = models.CharField(default="10:30 am - 6:30 pm", blank=False, max_length=100)
    wednesday = models.CharField(default="10:30 am - 6:30 pm", blank=False, max_length=100)
    thursday = models.CharField(default="10:30 am - 6:30 pm", blank=False, max_length=100)
    friday = models.CharField(default="10:30 am - 6:30 pm", blank=False, max_length=100)
    saturday = models.CharField(default="10:30 am - 6:30 pm", blank=False, max_length=100)
    sunday = models.CharField(default="Closed", blank=False, max_length=100)
    date_updated = models.DateField(default=timezone.now)
    visible = models.BooleanField(default=True)

    objects = HoursManager()
    
    def __str__(self):
         name = "Hours UPDATED: " + self.date_updated.strftime('%m/%y/%d')
         return name
    
    class Meta:
        verbose_name_plural = "Hours"

class Photos(models.Model):
    en_description = models.TextField(default="A New Promo description", blank=True)
    es_description = models.TextField(default="SPANISH A New Promo description", blank=True)
    en_photo = models.ImageField(upload_to="images/Photos/", default='transplogo.png')
    es_photo = models.ImageField(upload_to="images/Photos/", default='transplogo.png')
    visible = models.BooleanField(default=False)
    
    def __str__(self):
         return self.en_description


class EmailListManager(models.Manager):
    def create_emaillist(self, email):
        hours = self.create(email=email)
        return Hours
        
    
class EmailList(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=254)
    subscribed = models.BooleanField(default=True)

    objects = EmailListManager()
    
    def __str__(self):
         return self.email
    
    def unsubscribe(self):
        self.subscribed = False
        return
    
    class Meta:
        verbose_name_plural = "Email List"



PROMOTION_STATUS_CHOICES = [
        ('AC', 'Active'), 
        ('EX', 'Expired'),
        ('CS', 'Coming Soon'),
        ('OT', 'Other')
]

class PromotionManager(models.Manager):
    def create_promotion(self, name, description, start_date, end_date):
        promotion = self.create(name=name, description=description, start_date=start_date, end_date=end_date)
        return promotion

class Promotion(models.Model):
    id = models.AutoField(primary_key=True)
    en_name = models.CharField(default="New Promo", max_length=100)
    es_name = models.CharField(default="SPANISH New Promo", max_length=100)
    en_description = models.TextField(default="A New Promo description", blank=True)
    es_description = models.TextField(default="SPANISH A New Promo description", blank=True)
    en_photo = models.ImageField(upload_to="images/promos/", default='transplogo.png')
    es_photo = models.ImageField(upload_to="images/promos/", default='transplogo.png')
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    date_updated = models.DateField(default=timezone.now)
    status = models.CharField(default='AC', max_length=2, choices = PROMOTION_STATUS_CHOICES)
    visible = models.BooleanField(default=False)
    unique = models.BooleanField(default=False)

    objects = PromotionManager()
    
    def __str__(self):
         return self.en_name


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    en_name = models.CharField(default="Eyecare", blank=False, max_length=64)
    es_name = models.CharField(default="Eyecare", blank=False, max_length=64)

    def __str__(self):
         return self.en_name

class ArticleManager(models.Manager):
    def create_article(self, title, photo, text, visible, tags):
        article = self.create(title=title, photo=photo, text=text, visible=visible, tags=tags)
        return article
    
class Article(models.Model):
    id = models.AutoField(primary_key=True)
    en_title = models.CharField(default="A New Article", max_length=250)
    es_title = models.CharField(default="A New Article", max_length=250)
    slug = models.SlugField(max_length=250, unique=True, null=True)
    author = models.CharField(default="Eyes of Jamaica", max_length=250, blank=True)
    description = models.TextField(default="A New article", blank=True)
    es_description = models.TextField(default="A New article", blank=True)
    photo = models.ImageField(upload_to="images/library/", default='default_article.jpg')
    text = models.TextField(default="Article Text")
    en_body = RichTextUploadingField(default="DEFAULT TEXT")
    es_body = RichTextUploadingField(default="DEFAULT TEXT")
    publish_date = models.DateField(default=timezone.now)
    date_updated = models.DateField(default=timezone.now)
    visible = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)

    objects = ArticleManager()
    
    def __str__(self):
         return self.en_title
    
    def get_absolute_url(self):
        return reverse("article", args=[str(self.slug)])
    
    