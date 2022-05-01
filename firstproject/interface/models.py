from django.db import models

# Create your models here.
class Interface(models.Model):
    pub_date = models.DateTimeField('date published')
    question_text = models.CharField(default="teste",max_length=200)
    
    def __str__(self):
       return self.question_text
    
    

class File(models.Model):
    pub_date = models.DateTimeField('date published')
    question_text = models.CharField(default="teste",max_length=200)
    
    def __str__(self):
        return self.question_text
        