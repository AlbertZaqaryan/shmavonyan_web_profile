from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Article, ContactMessage, Profile, About, Education, Experience, Science_visit, Awards
from .forms import ContactForm

def home(request):
    profile = Profile.objects.first()
    about_info = About.objects.all()
    education_list = Education.objects.all()
    experience_list = Experience.objects.all()
    Science_visit_list = Science_visit.objects.all()
    awards_list = Awards.objects.all()
    return render(request, 'home.html', context={
        'profile':profile,
        'about_info':about_info,
        'education_list':education_list,
        'experience_list':experience_list,
        'Science_visit_list':Science_visit_list,
        'awards_list':awards_list

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
