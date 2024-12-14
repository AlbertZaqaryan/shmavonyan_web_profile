from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Article, ContactMessage, Profile
from .forms import ContactForm

def home(request):
    profile = Profile.objects.first()
    return render(request, 'home.html', context={
        'profile':profile
    })

def about(request):
    return render(request, 'about.html')

def articles(request):
    articles = Article.objects.all()
    return render(request, 'articles.html', {'articles': articles})

def download_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    response = HttpResponse(article.pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{article.pdf_file.name}"'
    return response
    

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')
