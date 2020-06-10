from django.db import models
from django.utils import timezone
from author.models import Author


class Book(models.Model):
    Published = 'PB'
    Withdrawn = 'WD'
    Draft = 'DF'

    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name="author_book")
    title = models.CharField(max_length=50)
    desc = models.TextField(default='')
    img = models.FileField(upload_to='images',default='/images/default.png')
    state_choices = [
        (Published,'Published'),
        (Withdrawn,'Withdrawn'),
        (Draft,'Draft')
    ]
    state = models.CharField(max_length=2,choices=state_choices,default=Published)
    created_date = models.DateTimeField(default=timezone.now)


    def is_upperclass(self):
        return self.state in {self.Published, self.Draft, self.Withdrawn}
    
    def __str__(self):
        return self.title

    
