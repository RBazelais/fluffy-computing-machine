from __future__ import unicode_literals
from django.db import models
from ..login.models import User

# Create your models here.
class FriendshipManager(models.Manager):
    def get_friends(self, person):
        user = self.user
        return Friendship.objects.filter(
            from_person=user,
            to_person=person
            )

    def add_friendship(self, person):
        user = user.self
        existingFriend = Friendship.objects.filter(
            from_person=user,
            to_person=person
        )
        if len(existingFriend) > 0:
            existingFriend[0].save()
        else:
            friendship = Friendship.objects.get_or_create(
                from_person=user,
                to_person=person
            )
        return friendship
    
    def remove_friendship(self, person):
        Friendship.objects.filter(
            from_person=self,
            to_person=person
        ).delete()

class Friendship(models.Model):
    from_person = models.ForeignKey(User, related_name='from_people')
    to_person = models.ForeignKey(User, related_name='to_people')
    objects = FriendshipManager()

    def __str__(self):
        return '%s %s %s' % (self.from_person, "befriended", self.to_person)

