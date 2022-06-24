from django.db import models


JOB_TYPE = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time')
)
# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100)
    #locationvacancy = mo
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=500)
    publish_at = models.DateTimeField(auto_now_add=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)


    def __str__(self):
        return [self.title, self.description, self.experience]




