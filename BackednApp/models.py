from django.db import models

# Create your models here.
class User(models.Model):
    uid = models.CharField(max_length=100, primary_key=True)
    email = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    friends = models.ManyToManyField("self", null=True)
    def __str__(self) -> str:
        return self.username

class League(models.Model):
    rankName = models.CharField(max_length=10)
    minRankPoints = models.IntegerField()
    maxRankPoints = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class WaterConsumption(models.Model):
    waterSourceName = models.CharField(max_length=15)
    waterConsumptionPerHour = models.IntegerField()
    unit = models.CharField(max_length=5)
    hoursOfUsage = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class ElectrictyConsumption(models.Model):
    hoursOfPhoneUsage = models.IntegerField(default=1)
    hoursOfComputerUsage = models.IntegerField(default=1)
    hoursOfTVUsage = models.IntegerField(default=1)
    electricityConsumption = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    @property
    def consumptionCalculations(self):
        totalConsumption = self.hoursOfPhoneUsage*0.0586 + self.hoursOfComputerUsage*0.01 + self.hoursOfTVUsage*0.055 + 5
        return totalConsumption

    def save(self, *args, **kwargs):
          self.electricityConsumption = self.consumptionCalculations
          super(ElectrictyConsumption, self).save(*args, **kwargs)
    
class HeatingConsumption(models.Model):
    temperatureInYourHoushold = models.IntegerField()
    electricityConsumptionPerHour = models.IntegerField()
    unit = models.CharField(max_length=5)
    hoursOfUsage = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Quiz(models.Model):
    learnigPathNumber = models.IntegerField()
    title = models.CharField(max_length=100)
    score = models.IntegerField()
    content = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Quiz_question(models.Model):
    level = models.IntegerField()
    score = models.IntegerField()
    content = models.CharField(max_length=250)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

class Quiz_answer(models.Model):
    correct = models.BooleanField()
    content = models.CharField(max_length=250)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    quiz_question = models.ForeignKey(Quiz_question, on_delete=models.CASCADE)

class Take(models.Model):
    score = models.IntegerField()
    content = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

class Take_answer(models.Model):
    content = models.CharField(max_length=250)
    take = models.ForeignKey(Take, on_delete=models.CASCADE)
    quiz_question = models.ForeignKey(Quiz_question, on_delete=models.CASCADE)
    quiz_answer = models.ForeignKey(Quiz_answer, on_delete=models.CASCADE)