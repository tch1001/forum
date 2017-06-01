from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from login.models import *
from home.models import *
import datetime
# Create your views here.

def checkLogin(req):
    if not req.session.has_key('username'):
        return False
    return req.session['username']

def home(request):
    username = checkLogin(request)
    if username == False:
        return HttpResponseRedirect('/')

    return render(request, 'home.html', {'username': username})

def discussions(request):
    username = checkLogin(request)
    if username == False:
        return HttpResponseRedirect('/')

    return render(request, 'discussion.html',
                  {'username': username, 'discussions': Discussion.objects.all()})
def questions(request):
    username = checkLogin(request)
    if username == False:
        return HttpResponseRedirect('/')

    return render(request, 'questions.html', {'username': username})

def announcements(request):
    username = checkLogin(request)
    if username == False:
        return HttpResponseRedirect('/')
    return render(request, 'announcements.html',
                  {'username': username})

def specificDiscussion(request, postTitle):

    try:
        discussionData = Discussion.objects.get(title=postTitle)
        # print("discussionData " ,discussionData)
        # print(DiscussionComment.objects.get())
        comments = DiscussionComment.objects.filter(parent=discussionData)
        # print(comments)
        ret = render(request, 'specificDiscussion.html',
                  {'discussionData': discussionData, 'comments': comments})
    except:
        ret = HttpResponse('haha sorry got nothing from the database, try googling "cat" instead!')
    return ret

def discussionPostComment(request, postTitle):
    username = checkLogin(request)
    if username == False:
        return HttpResponseRedirect('/')
    comment = request.POST.get('comment', '')
    if comment.replace(' ','') == '':
        return HttpResponseRedirect('/home/discussions/' + postTitle + '/')
    commentObj = DiscussionComment(author=User.objects.get(username=username), parent=Discussion.objects.get(title=postTitle), date=datetime.date.today(), content=comment)
    print(username)

    commentObj.save()
    return HttpResponseRedirect('/home/discussions/'+postTitle+'/')

def profile(request):
    username = checkLogin(request)
    if username == False:
        return HttpResponseRedirect('/')

    return render(request, 'profile.html', {'username': username})