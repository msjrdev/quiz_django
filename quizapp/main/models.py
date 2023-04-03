from django.db import models

class QuizCategory(models.Model):
    title=models.CharField(max_length=100)
    detail=models.TextField()
    image=models.ImageField(upload_to='cat_imgs/')
    
    class Meta:
        verbose_name_plural="Categories"

    def __str__(self):
        return self.title

class QuizQuestion(models.Model):
    category=models.ForeignKey(QuizCategory, on_delete=models.CASCADE)
    question=models.TextField()
    image=models.ImageField(upload_to='cat_imgs/', null=True, blank=True)
    opt_1=models.CharField(max_length=250)
    opt_2=models.CharField(max_length=250)
    opt_3=models.CharField(max_length=250)
    opt_4=models.CharField(max_length=250)
    opt_5=models.CharField(max_length=250)
    level=models.CharField(max_length=100)
    time_limit=models.IntegerField()
    right_ope=models.CharField(max_length=100)
    comentary=models.CharField(max_length=250, null=True, blank=True)
    
    class Meta:
        verbose_name_plural="Questions"
        
    def __str__(self):
        return self.question
