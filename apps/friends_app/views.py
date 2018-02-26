from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from ..login.models import User
from .models import Friendship

# Create your views here.
def friends(request):
    if 'user_id' not in request.session:
        print "The user is not in session"
        return redirect('/lr_app')
    else:
        user = User.objects.get(id=request.session['user_id'])
        context = {
            'user': user,
            # all users except user in session
            'my_friends':  user.friendships.all().exclude(from_people=user.id),
            'all_users': User.objects.all().exclude(from_people=user.id).exclude(friendships=user.id),
        }
    return render(request, "dashboard.html", context)

def add_friend(request, id):
    print "************"
    print request.POST

    this_person = User.objects.get(id=id) # person you clicked on add friend in html
    curr_user = User.objects.get(id=request.session['user_id']) # User in session
    print "************"
    print this_person
    print curr_user

    # add the person to current user's friendships
    curr_user.friendships.add(this_person)
    
    Friendship.objects.create(from_person_id=curr_user.id, to_person=User.objects.get(id=this_person.id))
    print "************"
    print "Friendship instance created"
    

    # save changes
    this_person.save()
    curr_user.save()

    print "************"
    print "friend added to user in session"
    return redirect('/friends')

def remove_friend(request, id):
    curr_user = User.objects.get(id=request.session['user_id']) 
    this_person = User.objects.get(id=id) # person you clicked on remove friend in html

    print "************"
    print curr_user
    print this_person
    
    # remove friend(this_person) from the user's list of friends
    curr_user.friendships.remove(this_person)
    
    #  delete friendship instance
    Friendship.objects.filter(
        to_person=User.objects.get(
            id=this_person.id
        )
    ).delete()
    print "************"
    print "friend was removed from user in session"
    print "************"
    return redirect('/friends')
        

def profile(request, id):
    this_person = User.objects.get(id=id)
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'alias': this_person.alias,
        'name': this_person.name,
        'email': this_person.email,
    }
    return render(request, 'profile.html', context)
