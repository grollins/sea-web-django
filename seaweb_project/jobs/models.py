from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token
from model_utils.models import StatusModel
from model_utils import Choices


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    ''' Creates a token whenever a User is created '''
    if created:
        Token.objects.create(user=instance)


class Job(StatusModel):
    STATUS = Choices('submitted', 'queued', 'done', 'error')
    title = models.CharField(max_length=100, blank=True, default='')
    structure = models.FileField(upload_to='tmp/%Y/%m/%d')
    topology = models.FileField(upload_to='tmp/%Y/%m/%d')
    iterations = models.IntegerField(default=10)
    CALC_TYPE = Choices('dipole', 'quadrupole')
    calculation_type = models.CharField(
                        choices=CALC_TYPE, default=CALC_TYPE.dipole,
                        max_length=20)
    surface_detail = models.IntegerField(default=8)
    owner = models.ForeignKey('auth.User', related_name='jobs')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_on',)
        unique_together = ('owner', 'title')


class Result(models.Model):
    job = models.ForeignKey('Job', related_name='result')
    gb = models.FloatField(default=0.0)
    non_polar = models.FloatField(default=0.0)
    reaction_field = models.FloatField(default=0.0)
    solvent_intershell = models.FloatField(default=0.0)
    solvent_intrashell = models.FloatField(default=0.0)
    solvent_solute = models.FloatField(default=0.0)
    total = models.FloatField(default=0.0)
    sasa = models.FloatField(default=0.0)
    shell_zero_waters = models.FloatField(default=0.0)
