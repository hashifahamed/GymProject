from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=12)
    description=models.TextField()
    
    def __str__(self):
        return self.email
    
class Enrollment(models.Model):
    FullName=models.CharField(max_length=25)
    Email=models.EmailField()
    Gender=models.CharField(max_length=25)
    PhoneNumber=models.CharField(max_length=10)
    DOB=models.CharField(max_length=50)
    SelectMembershipPlane=models.CharField(max_length=200)
    SelectTrainer=models.CharField(max_length=55)
    DueDate=models.DateTimeField(max_length=100, blank=True, null=True )
    PaymentStatus=models.CharField(max_length=10, blank=True, null=True)
    Timestamp=models.TimeField(max_length=50, blank=True, null=True)
    Address=models.TextField()
    
        
    def __str__(self):
        return self.FullName
    
class Trainer(models.Model):
    name=models.CharField(max_length=55)
    gender=models.CharField(max_length=25)
    phone=models.CharField(max_length=10)
    Qualification=models.CharField(max_length=400)
    timeStamp=models.DateTimeField(auto_now_add=True, auto_now=False)
        
    def __str__(self):
        return self.name
        
class MembershipPlan(models.Model):
    plan=models.CharField(max_length=200)
    price=models.CharField(max_length=100)
        
    def __str__(self):
        return self.plan   
    
    
class Attendance(models.Model):
    SelectDate=models.DateTimeField(auto_now_add=True)
    PhoneNumber=models.CharField(max_length=10)
    Login=models.CharField(max_length=200)
    Logout=models.CharField(max_length=200)
    SelectWorkout=models.CharField(max_length=200,null=True)
    TrainedBy=models.CharField(max_length=200)   
    
    def __str__(self):
        return self.SelectWorkout    