from django.db import models


class Category(models.Model):
    nick = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title


class Project(models.Model):
    category = models.ForeignKey(Category)
    pub_date = models.DateTimeField('date published')
    nick = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=200)
    lead = models.TextField()

    def __unicode__(self):
        return self.title


class Artifact(models.Model):
    project = models.ForeignKey(Project)
    description = models.CharField(max_length=200)

    def __unicode__(self):
        return self.description
