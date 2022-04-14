from django.db import models
from django.conf import settings

# Create your models here.
class UserType(models.Model):
    Type = [("D", "Doctor"), ("P", "Patient")]
    userID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    username = models.CharField(max_length = 4, primary_key = True)
    userType = models.CharField(max_length = 1, choices = Type, null = False)

    def __str__(self):
        return f"{self.username} of Django userID {self.userID}, {self.userType}"

class Doctors(models.Model):
    DoctorID = models.ForeignKey(UserType, on_delete = models.CASCADE, primary_key = True)
    Name = models.CharField(max_length = 100, null = False, blank = False)
    ContactNum = models.CharField(max_length = 12, null = False, blank = False) #do num validation in front end, add on_delete
    Hospital = models.CharField(max_length = 100, null = False, blank = False)
    EmailID = models.CharField(max_length=100, default="", null = False, blank = False)

    def __str__(self):
        return f"{self.DoctorID.username}, {self.Name}"

class Patients(models.Model):
    GenderChoices = [("F", "Female"), ("M", "Male")]
    PatientID = models.ForeignKey(UserType, on_delete = models.CASCADE, primary_key = True)
    DoctorID = models.ForeignKey(Doctors, on_delete = models.CASCADE, null = False, blank = False)
    Name = models.CharField(max_length=100, null=False, blank=False)
    DOB = models.DateField(null=False, blank=False)
    Gender = models.CharField(max_length = 1, choices = GenderChoices)
    Age = models.IntegerField(null=False, blank=False, default=1)
    BloodType = models.CharField(max_length=3, null=False, blank=False, default="A+")
    Address = models.CharField(max_length = 150, null=False, blank=False)
    ContactNum = models.CharField(max_length = 12, null = False, blank = False)
    EmergencyContact = models.CharField(max_length = 12, null = False, blank = False)
    Insurance = models.CharField(max_length = 50)
    EmailID = models.CharField(max_length = 100, null = False, blank = False)
    Pedigree = models.FloatField(null=False, default=0.5, blank=False)

    def __str__(self):
        return f"{self.PatientID.username}, {self.Name}"


class DailyData(models.Model):
    PatientID = models.ForeignKey(Patients, on_delete = models.CASCADE)
    Date = models.DateField(null=False, blank=False)
    LastAvgTemp = models.FloatField(null=True, blank=True)    #fill when person enters sugar lvl, by run procedure ig
    LastAvgHeartRate = models.FloatField(null=True, blank=True)   #fill when person enters sugar lvl, by run procedure ig of previous day
    LastAvgOxygen = models.FloatField(null=False, blank=False, default=0)
    BloodSugar = models.FloatField(null=True, blank=True)
    BloodPressure = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.PatientID}, {self.Date}"
#gotta run procedure for auto delete ig
class SecondlyData(models.Model):
    PatientID = models.ForeignKey(Patients, on_delete = models.CASCADE)
    Date = models.DateField(null=False, blank=False)
    Time = models.TimeField(null=False, blank=False)
    Pulse = models.FloatField(null=False, blank=False)
    Temp = models.FloatField(null=False, blank=False)
    Oxygen = models.FloatField(null=False, blank=False, default=0)

    def __str__(self):
        return f"{self.PatientID}, {self.Date}"

class WeeklyData(models.Model): # or monthly idk
    PatientID = models.ForeignKey(Patients, on_delete=models.CASCADE)
    Date = models.DateField(null=False, blank=False)
    Weight = models.FloatField(null=True, blank=True)
    Height = models.FloatField(null=True, blank=True)
    BMI = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.PatientID}, {self.Date}"

class testingAPI(models.Model):
    data = models.FloatField()
    string = models.CharField(max_length=200, default="")

    def __str__(self):
        return f"{self.data}, {self.string}"

class PatientImage(models.Model):
    username = models.CharField(max_length = 4, primary_key = True)
    img = models.ImageField(upload_to="media")

    def __str__(self):
        return f"{self.username}"

class FirebaseData(models.Model):
    username = models.CharField(max_length = 4, primary_key = True)
    Temp = models.FloatField()
    IR = models.IntegerField()

    def __str__(self):
        return f"{self.IR} {self.Temp}"

class Alert(models.Model):
    username = models.CharField(max_length = 4)

# use a models to see what the last - value of ir was and save time with it
class IRCheck(models.Model):
    PositivePrev = models.BooleanField()
    username = models.CharField(max_length=4, primary_key = True)
    TimeStamp = models.FloatField()

    def __str__(self):
        return f"{self.username}, {self.TimeStamp}"

class Conditions(models.Model):
    DiabetesChance = models.BooleanField(default=False)
    Hypoxia = models.BooleanField(default=False)
    HighPulse = models.BooleanField(default=False)
    Hypothermia = models.BooleanField(default=False)
    Fever = models.BooleanField(default=False)
    username = models.CharField(max_length = 4, primary_key = True)
    Alert = models.BooleanField(default=False, null=False, blank=False)

    def __str__(self):
        return f"{self.username} conditions"