from django.db import models


class Profile(models.Model):
    image = models.ImageField(upload_to='profile/')
    name = models.CharField(max_length=100)
    prof = models.TextField()

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pdf_file = models.FileField(upload_to='articles/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

class About(models.Model):

    text = models.TextField()

    def __str__(self):
        return "About me"
    
class Education(models.Model):

    info = models.TextField()

    def __str__(self):
        return self.info
    

class Experience(models.Model):

    date = models.CharField(max_length=100)
    info = models.TextField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.info
    

    
class Awards(models.Model):

    text = models.TextField()

    def __str__(self):
        return self.text
    
class Science_visit(models.Model):

    date = models.CharField(max_length=60)
    locations = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.date} -> {self.locations}'