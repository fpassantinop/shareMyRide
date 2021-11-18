"""Profile model"""

#Django
from django.db import models

#utilities
from cride.utils.models import CRideModel

class Profile(CRideModel):
    """Profile model

    a profile save a users public data like picture, stats, etc
    """
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    
    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True, #No requiered
        null=True
    )
    biography = models.TextField(max_length=500,blank=True)
    
    #stats
    rides_taken = models.PositiveIntegerField(default=0)
    rides_offered = models.PositiveIntegerField(default=0)
    reputation = models.FloatField(
        default=5.0,
        help_text="Users reputation based on the ride taken an offered."
    )
    
    def __str__(self):
        return str(self.user)