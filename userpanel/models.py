from django.db import models
from base.models import User
from adminpanel.models import DocumentModel, Form, Job, Question, JobQuestion
# Create your models here.

class CustomDocumentUploadModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    File= models.FileField(upload_to ="my_documents",blank=True)
    PagesNo = models.IntegerField()
    Title = models.CharField(max_length=200)
    isVerified = models.BooleanField(default=False)
    upload_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)

class ProfileDocumentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    NAD_Documents= models.ForeignKey(DocumentModel, on_delete=models.CASCADE)
    
class SubmitFileQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.FileField(upload_to ="docs",blank=True)
    
class SubmitPreVerifiedQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null= True, blank= True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    file_id = models.IntegerField(null=True, blank=True)
    
class SubmitTextQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField(null=False, blank=True)
    
class JobSubmitFileQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(JobQuestion, on_delete=models.CASCADE)
    answer = models.FileField(upload_to ="docs",blank=True)
    
class JobSubmitPreVerifiedQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null= True, blank= True)
    question = models.ForeignKey(JobQuestion, on_delete=models.CASCADE)
    file_id = models.IntegerField(null=True, blank=True)
    
class JobSubmitTextQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(JobQuestion, on_delete=models.CASCADE)
    answer = models.TextField(null=False, blank=True)
    

    