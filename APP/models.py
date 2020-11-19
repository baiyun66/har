from django.db import models

# Create your models here.

# Create your models here. 类似于MVC架构中的Model

class Article(models.Model):
    title = models.CharField(max_length=60,default='title')
    content = models.TextField(null=True)


'''
1 WALKING
2 WALKING_UPSTAIRS
3 WALKING_DOWNSTAIRS
4 SITTING
5 STANDING
6 LAYING
'''


class PosturalData(models.Model):
    posturaltype = models.PositiveSmallIntegerField(choices=[(0, 'wrong'),
                                                             (1, 'WALKING'),
                                                             (2, 'WALKING_UPSTAIRS'),
                                                             (3, 'WALKING_DOWNSTAIRS'),
                                                             (4, 'SITTING'),
                                                             (5, 'STANDING'),
                                                             (6, 'LAYING'),
                                                             ],default=1)