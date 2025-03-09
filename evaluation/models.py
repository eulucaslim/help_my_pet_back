from django.db import models
from register.models import User, Veterinary

class Evaluation(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    veterinary = models.ForeignKey(Veterinary, on_delete=models.PROTECT)
    rating = models.PositiveSmallIntegerField()
    description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'veterinary')
