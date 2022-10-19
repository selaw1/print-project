import uuid
from django.utils.translation import gettext_lazy as _


def make_uuid():
    """
    Returns a UUID V4 for postgres based models

    Example:
    class User(models.Model):
        id = models.UUIDField(primary_key=True, default=make_uuid)
    """
    return uuid.uuid4()


    """
common multi choices
"""

from django.db import models
from django.utils.translation import gettext_lazy as _


class GenderChoices(models.TextChoices):
    """
    Enumeration for the type of genders
    """

    MALE = "male", _("MALE")
    FEMALE = "female", _("FEMALE")
