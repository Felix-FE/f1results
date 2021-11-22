from django.db import models


class timeEntry(models.Model):
  driver = models.CharField(max_length=200)
  fastest_time = models.CharField(max_length=200)
  position = models.CharField(max_length=200)
  laps = models.CharField(max_length=200)
  team = models.CharField(max_length=200)
  gp = models.CharField(max_length=200)
  session = models.CharField(max_length=200)
  year = models.CharField(max_length=200)
  published = models.DateField(auto_now = True)
  
  def __str__(self):
    return '%s %s %s %s %s %s %s' % (
    self.driver, 
    self.fastest_time, 
    self.position, 
    self.laps, 
    self.team, 
    self.gp, 
    self.session,
    self.year) 
