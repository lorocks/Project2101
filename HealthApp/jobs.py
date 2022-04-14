from schedule import Scheduler
import threading
import time
import datetime
import random

from .models import *
from .ML import Predict
from django.core.mail import send_mail

def get_firebase_to_web():
    patient_check = "P001"
    patients = Patients.objects.all()
    for thing in patients:
        if thing.PatientID.username == patient_check:
            guy = thing
    secondly = SecondlyData(PatientID=guy,Date=datetime.datetime.now().date(),Time=datetime.datetime.now().time(),Pulse=60 + random.randint(0,40) + random.random(),Temp=random.random() + 36,Oxygen=99)
    secondly.save()

def alert_from_conditions():
    conditions = Conditions.objects.all()
    patients = Patients.objects.all()
    for condition in conditions:
        for patient in patients:
            if patient.PatientID.username == condition.username:
                message = ""
                if condition.Hypoxia:
                    message = message + "Patient has Hypoxia\n"
                if condition.HighPulse:
                    message= message + "Patient has High Pulse\n"
                if condition.Hypothermia:
                    message = message + "Patient has Hypothermia\n"
                if len(message) > 1:
                    send_mail('Urgent', f'There has been an Emergency for {patient.Name} with username: {patient.PatientID.username}\n{message}', 'll753@live.mdx.ac.uk', [patient.DoctorID.EmailID], fail_silently=False)

def diabetes():
    patients = Patients.objects.all()
    for patient in patients:
        daily = DailyData.objects.filter(PatientID=patient)
        daily = daily[len(daily)-1]
        weekly = WeeklyData.object.filter(PatientID=patient)
        weekly = weekly[len(weekly)-1]
        p = Predict(daily.BloodSugar,daily.BloodPressure,weekly.BMI,patient.Pedigree,patient.Age)
        p = p[0]
        if p:
            conditions = Conditions.objects.filter(username=patient.PatientID.username)
            condition = conditions[0]
            conditions.delete()
            newcondition = Conditions(DiabetesChance=True, Hypoxia=condition.Hypoxia,
                                      HighPulse=condition.HighPulse, Fever=condition.Fever,
                                      Hypothermia=condition.Hypothermia,
                                      username=patient.PatientID.username, Alert=condition.Alert)
            newcondition.save()
        else:
            conditions = Conditions.objects.filter(username=patient.PatientID.username)
            condition = conditions[0]
            conditions.delete()
            newcondition = Conditions(DiabetesChance=False, Hypoxia=condition.Hypoxia,
                                      HighPulse=condition.HighPulse, Fever=condition.Fever,
                                      Hypothermia=condition.Hypothermia,
                                      username=patient.PatientID.username, Alert=condition.Alert)
            newcondition.save()

def delete_old_records():
    secondly = SecondlyData.objects.all()
    for thing in secondly:
        if thing.Date < datetime.datetime.now().date() - datetime.timedelta(days=1):
            thing.delete()
    daily = DailyData.objects.all()
    for thing in daily:
        if thing.Date < datetime.datetime.now().date() - datetime.timedelta(days=14):
            thing.delete()
    weekly = WeeklyData.objects.all()
    for thing in weekly:
        if thing.Date < datetime.datetime.now().date() - datetime.timedelta(days=14):
            thing.delete()

def run_continously(self, interval=2):
    cease_continous_run = threading.Event()

    class ScheduleThread(threading.Thread):

        @classmethod
        def run(cls):
            while not cease_continous_run.is_set():
                self.run_pending()
                time.sleep(interval)

    continous_thread = ScheduleThread()
    continous_thread.setDaemon(True)
    continous_thread.start()
    return cease_continous_run

Scheduler.run_continously = run_continously

def start_scheduler():
    scheduler = Scheduler()
    # scheduler.every().second.do(alert_from_conditions) #make into alert from conditions
    scheduler.every().day.at("22:00").do(delete_old_records)
    scheduler.every().day.at("22:30").do(diabetes)
    scheduler.run_continously()