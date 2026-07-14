from django.db import models

# Create your models here.
class Slider(models.Model):
    title = models.CharField(max_length=200, default='')
    description = models.TextField(default='')
    image = models.ImageField(upload_to='image_sliders')

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=200, default='')
    image1 = models.ImageField(upload_to='image_about', null=True, blank=True)
    description = models.TextField(default='')
    short_description1 = models.CharField(max_length=300, default='')
    title_headline1 = models.CharField(max_length=100, default='')
    title_headline2 = models.CharField(max_length=100, default='')
    title_headline3 = models.CharField(max_length=100, default='')
    short_description2 = models.TextField(default='')
    image2 = models.ImageField(upload_to='image2_about', null=True, blank=True)
    video = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.title
    
    
class Service(models.Model):
        icon_service = models.CharField(max_length=100, default='', blank=True)
        title = models.CharField(max_length=100, default='', blank=True)
        description = models.TextField(max_length=300, default='', blank=True)
        speed = models.CharField(max_length=100, default='', blank=True)
    
        
        def __str__(self):
            return self.title
    
class Portfolio(models.Model):
    catigory = models.CharField(max_length=200, default='', blank=True)
    title = models.CharField(max_length=200, default='', blank=True)
    short_description = models.TextField(max_length=300, default='', blank=True)
    client = models.CharField(max_length=100, default='', blank=True)
    url = models.CharField(max_length=100, default='', blank=True)   
    description = models.TextField(max_length=1000, default='', blank=True)
    image = models.ImageField(upload_to='image_portfolio', null=True, blank=True)   

    def __str__(self):
        return self.title 
    
class Team(models.Model):
    fullname = models.CharField(max_length=100, default='', blank=True)
    role_company = models.CharField(max_length=100, default='', blank=True)
    image = models.ImageField(upload_to='image_team', null=True, blank=True) 
    urlx = models.CharField(max_length=100, default='', blank=True)
    urlfacebook = models.CharField(max_length=100, default='', blank=True)
    urlinstagram = models.CharField(max_length=100, default='', blank=True)
    urllikedin = models.TextField(max_length=100, default='', blank=True)
    speed = models.TextField(max_length=100, default='', blank=True)
    
    def __str__(self):
        return self.fullname
    
class Faq(models.Model):
    question = models.CharField(max_length=200, default='', blank=True)
    reply = models.TextField(max_length=1000, default='', blank=True)
    speed = models.CharField(max_length=100, default='', blank=True)
    
    def __str__(self):
        return self.question

class Contactform(models.Model):
    name = models.CharField(max_length=100, default='', blank=True)
    email = models.EmailField(max_length=100, default='', blank=True)
    subject = models.CharField(max_length=200, default='', blank=True)
    message = models.TextField()
    date_message = models.DateTimeField(auto_now_add=True, null=True,blank=True )

    def __str__(self):
        return self.email 
    
    
class Generalsetting(models.Model):
    favicon = models.ImageField(upload_to='image_favicon', null=True, blank=True)
    logo = models.ImageField(upload_to='image_logo', null=True, blank=True)
    companyname = models.CharField(max_length=100, default='', blank=True)
    email1 = models.EmailField(default='', blank=True)
    email2 = models.EmailField(default='', blank=True)
    phone = models.CharField(default='', blank=True)  
    address = models.CharField(max_length=200, default='', blank=True)
    urlx = models.CharField(max_length=100, default='', blank=True)
    urlfacebook = models.CharField(max_length=100, default='', blank=True)
    urlinstagram = models.CharField(max_length=100, default='', blank=True)
    urllikedin = models.TextField(max_length=100, default='', blank=True)
    

    def __str__(self):
        return self.companyname
    