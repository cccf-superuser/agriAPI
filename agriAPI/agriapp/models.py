from django.db import models

class WeatherData(models.Model):
    humidity = models.FloatField()
    temperature = models.FloatField()
    nitrogen = models.FloatField()
    phosphorus = models.FloatField()
    potassium = models.FloatField()
    water_level = models.FloatField()
    pH = models.FloatField()

    def __str__(self):
        return f"WeatherData {self.id}"
