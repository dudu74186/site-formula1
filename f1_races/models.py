from django.db import models

class car_data(models.Model):
    driver_number = models.IntegerField()
    session_key = models.IntegerField()
    date = models.DateTimeField()
    speed = models.IntegerField()
    throttle = models.IntegerField()
    brake = models.IntegerField()
    n_gear = models.IntegerField()
    meeting_key = models.IntegerField()

    class Meta:
        unique_together = ('driver_number', 'session_key', 'date')

    def __str__(self):
        return f"Driver {self.driver_number} - Session {self.session_key} on {self.date}"
    
class driver(models.Model):
    broadcast_name = models.CharField(max_length=100)
    driver_number = models.IntegerField()
    first_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    meeting_key = models.IntegerField()
    team_colour = models.CharField(max_length=7 , blank=True, null=True)
    team_name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=4)
    headshot_url = models.URLField(max_length=200, blank=True, null=True)
    name_acronym = models.CharField(max_length=3, blank=True, null=True)
    session_key = models.IntegerField()

    def __str__(self):
        return f"{self.full_name} ({self.driver_number}) - {self.team_name}"


class sessions(models.Model):
    circuit_key = models.IntegerField()
    circuit_short_name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=4)
    country_key = models.IntegerField()
    country_name = models.CharField(max_length=100)
    date_end = models.DateTimeField()
    date_start = models.DateTimeField()
    gmt_offset = models.CharField(max_length=10)
    location = models.CharField(max_length=100)
    meeting_key = models.IntegerField()
    session_key = models.IntegerField()
    session_name = models.CharField(max_length=100)
    session_type = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.session_name} - {self.circuit_short_name} ({self.year})"