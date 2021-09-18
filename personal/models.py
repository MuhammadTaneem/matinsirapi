from django.db import models


class Education(models.Model):
    institution = models.CharField(max_length=255, null=False, blank=False)
    degree = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.degree + ' ' + self.institution


class Work(models.Model):
    institution = models.CharField(max_length=255, null=False, blank=False)
    position = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.position + ' ' + self.institution


class Research(models.Model):
    description = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.description


class Gallery(models.Model):
    image = models.ImageField(upload_to='images/', default=None)

