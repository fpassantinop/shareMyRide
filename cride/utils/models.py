"""Django models utilities"""

#Django
from django.db import models

class CRideModel(models.Model):
    """Comparte Ride base model.
    acts as an abstract class from which
    every other model in the project will inherit. This class
    provides every table with the following attributes:
        + created (DateTime) : Store the datetime with the object was created
        + modified (DateTime) : Store the datetime with the object was modified
    """
    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text= 'Date time on which the object was created'
    )
    
    modified = models.DateTimeField(
        'modified at',
        auto_now_add=True,
        help_text= 'Date time on which the object was modified'
    )
    
    class Meta:
        """Meta options"""
        abstract = True
        
        get_latest_by = 'created'
        ordering = ['-created', '-modified']
    