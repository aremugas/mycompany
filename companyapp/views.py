from django.utils import timezone

from django.shortcuts import redirect, render, get_object_or_404

from .models import About, Contactform, Faq, Generalsetting, Service, Slider, Portfolio, Team
# Create your views here.

def homefunction(request):
    sliders = Slider.objects.all()
    about = About.objects.filter(id=1).first()
    service = Service.objects.all()
    portfolios = Portfolio.objects.all()
    teams = Team.objects.all() 
    faqs = Faq.objects.all()
    generalsetting = Generalsetting.objects.filter(id=1).first()
     
    context = {
        'sliders': sliders,
        'about': about, 
        'services': service,
        'portfolios': portfolios,
        'teams': teams, 
        'faqs': faqs,
        'generalsetting': generalsetting,
    }
    return render(request, 'companyapp/index.html', context)  # Renders the index.html template 

def portfolio_detail(request, pk):
    portfolio_detail = get_object_or_404(Portfolio,pk=pk)
    generalsetting = Generalsetting.objects.filter(id=1).first()
    context = {
        'portfolio_detail': portfolio_detail,
        'generalsetting': generalsetting,
    }
    return render(request, 'companyapp/portfolio_detail.html', context)

def contact_f(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        Contactform.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message,
            date_message = timezone.now()
        )
        
    return redirect('home')    
        
    
