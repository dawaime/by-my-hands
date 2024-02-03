from django.db import models

# Create your models here.
class Visitors(models.Model):
    db_table = "visitors"
    name = models.CharField(max_length=256, null=True)
    global_click_counter_register = models.PositiveIntegerField(null=True)
    global_click_counter_result = models.PositiveIntegerField(null=True)
