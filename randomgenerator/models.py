from django.conf import settings
from django.db import models


TITLE_CHOICES = {
    "MR": "Mr.",
    "MRS": "Mrs.",
    "MS": "Ms.",
}


class RanGenModel(models.Model):
    name = models.CharField(max_length=100)
    game_id = models.CharField(max_length=5)
    ran_num_json = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.name
