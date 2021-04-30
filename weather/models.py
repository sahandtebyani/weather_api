from django.db import models


DESCRIPTION = (
    (0, "Sunny"),
    (1, "Rain"),
    (2, "Cloudy"),
    (3, "Snow"),
)


class Weather(models.Model):
    weather_description = models.IntegerField(choices=DESCRIPTION, default=0)
    temperature = models.FloatField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return str(self.created_on)