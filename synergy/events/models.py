from django.db import models

# Create your models here.


class CommonCriteria(models.Model):

    event_choices = (
        ('s', 'single'),
        ('d', 'double'),
    )

    course_choice = (
        ('it', 'Mtech'),
        ('ic','MCA'),
        ('ib', 'Bcom(hons)'),
        ('mb', 'MBA')
    )
    event_type = models.CharField(max_length=1, choices=event_choices)
    player_name = models.CharField(max_length=100)
    second_player_name = models.CharField(max_length=100, null=True, blank=True)
    course = models.CharField(max_length=2, choices=course_choice)
    email = models.EmailField()
    contact = models.IntegerField()


    class Meta:
        abstract = True


class TableTennis(CommonCriteria):

    def __unicode__(self):

        return self.player_name

class Badminton(CommonCriteria):

    def __unicode__(self):

        return self.player_name

class Volleyball(models.Model):

    course_choice = (
        ('it', 'Mtech'),
        ('ic','MCA'),
        ('ib', 'Bcom(hons)'),
        ('mb', 'MBA')
    )

    course = models.CharField(max_length=2, choices=course_choice)
    captain = models.CharField(max_length=100)
    player1 = models.CharField(max_length=100)
    player2 = models.CharField(max_length=100)
    player3 = models.CharField(max_length=100)
    player4 = models.CharField(max_length=100)
    player5 = models.CharField(max_length=100)
    extra1 = models.CharField(max_length=100)
    extra2 = models.CharField(max_length=100)
    contact = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)


    def __unicode__(self):
        return self.captain

class Chess(models.Model):

    course_choice = (
        ('it', 'Mtech'),
        ('ic','MCA'),
        ('ib', 'Bcom(hons)'),
        ('mb', 'MBA')
    )

    course = models.CharField(max_length=2, choices=course_choice)
    player_name = models.CharField(max_length=100)
    contact = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)

    def __unicode__(self):
        return self.player_name
