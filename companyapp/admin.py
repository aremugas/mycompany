from django.contrib import admin

from .models import Contactform, Faq, About, Generalsetting, Service, Slider, Portfolio, Team

# Register your models here.
admin.site.register(Slider)
admin.site.register(About) 
admin.site.register(Service) 
admin.site.register(Portfolio) 
admin.site.register(Team) 
admin.site.register(Faq) 
admin.site.register(Contactform)
admin.site.register(Generalsetting)