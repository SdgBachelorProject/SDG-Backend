from django.db import models

# Create your models here.


class League(models.Model):
    rankName = models.CharField(max_length=10)
    minRankPoints = models.IntegerField(default=1)
    maxRankPoints = models.IntegerField(default=1)
    
class User(models.Model):
    uid = models.CharField(max_length=100, primary_key=True)
    email = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    friends = models.ManyToManyField("self", null=True)
    league = models.ForeignKey(League, on_delete=models.CASCADE, null=True)
    def __str__(self) -> str:
        return self.username
    def is_active(self):
        return True


class WaterConsumption(models.Model):
    bathsPerWeek = models.IntegerField(default=1)
    singleShowerDuration = models.IntegerField(default=1)
    numberOfShowerPerWeek = models.IntegerField(default=1)
    hasDishwasher = models.BooleanField(default=True)
    numberOfDishwashesPerWeek = models.IntegerField(default=1)
    numberOfWashingMachineUsage = models.IntegerField(default=1)
    waterConsumption = models.IntegerField(default=1)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    @property
    def consumptionCalculations(self):
        if(self.hasDishwasher == True):
            totalConsumption = self.bathsPerWeek*15 + self.singleShowerDuration*6*self.numberOfShowerPerWeek + self.numberOfDishwashesPerWeek*3 + self.numberOfDishwashesPerWeek*4
            return totalConsumption
        if(self.hasDishwasher == False):
            totalConsumption = self.bathsPerWeek*15 + self.singleShowerDuration*6*self.numberOfShowerPerWeek + self.numberOfDishwashesPerWeek*5 + self.numberOfDishwashesPerWeek*4
            return totalConsumption
        else:
            return 0

    def save(self, *args, **kwargs):
          self.waterConsumption = self.consumptionCalculations
          super(WaterConsumption, self).save(*args, **kwargs)

class ElectrictyConsumption(models.Model):
    hoursOfPhoneUsage = models.IntegerField(default=1)
    hoursOfComputerUsage = models.IntegerField(default=1)
    hoursOfTVUsage = models.IntegerField(default=1)
    electricityConsumption = models.DecimalField(default=1, decimal_places=2,max_digits=10)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)


    @property
    def consumptionCalculations(self):
        totalConsumption = self.hoursOfPhoneUsage*0.0586 + self.hoursOfComputerUsage*0.01 + self.hoursOfTVUsage*0.055 + 5
        return totalConsumption

    def save(self, *args, **kwargs):
          self.electricityConsumption = self.consumptionCalculations
          super(ElectrictyConsumption, self).save(*args, **kwargs)
    
class HeatingConsumption(models.Model):
    temperatureInYourHoushold = models.IntegerField(default=1)
    numberOfRooms = models.IntegerField(default=1)
    buildingType = models.IntegerField(default=1)
    heatingConsumption = models.IntegerField(default=1)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    @property
    def consumptionCalculations(self):
        if(self.buildingType == 1 ):
            totalConsumption = (self.temperatureInYourHoushold*0.0586 + self.numberOfRooms*0.01) * 2 
            return totalConsumption
        if(self.buildingType == 2 ):
            totalConsumption = (self.temperatureInYourHoushold*0.0586 + self.numberOfRooms*0.01) * 3 
            return totalConsumption
        if(self.buildingType == 3 ):
            totalConsumption = (self.temperatureInYourHoushold*0.0586 + self.numberOfRooms*0.01) * 4 
            return totalConsumption
        else:
            return 0

    def save(self, *args, **kwargs):
          self.heatingConsumption = self.consumptionCalculations
          super(HeatingConsumption, self).save(*args, **kwargs)

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