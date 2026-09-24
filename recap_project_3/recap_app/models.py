from django.db import models

# Create your models here.
class StudentModel(models.Model):
    GENDER_TYPES =[
        #list er moddhe tupple prothom ta mechine readable arekta human readable, Dan pasher ta drop down e asebe  

        ('male','Male'),('female','Female'),('third_party','Third Party') #MALE,FEMALE, OTHERS

    ]
    
    address = models.TextField(null=True)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null = True )
    admission_date = models.DateField(null=True)
    gender = models.CharField(choices=GENDER_TYPES, max_length= 100, null=True)
    image = models.ImageField(upload_to='media/student_img',null = True)



    def __str__(self):
        return f'{self.name}'