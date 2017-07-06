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

    discussionsList = Discussion.objects.all()
    # comments = {}
    # for i in discussionsList:
    #     comments[i] = DiscussionComment.objects.filter(parent=i)
    #     # comments[i] = comments[i][len(comments[i])-5-1:len(comments[i])-1]
    return render(request, 'discussion.html',
                  {'username': username, 'discussions': discussionsList[::-1]})
def questions(request):
    username = checkLogin(request)
    if username == False:
        return HttpResponseRedirect('/')

    questionsList = Question.objects.all()


    return render(request, 'questions.html', {'username': username, 'questions':questionsList[::-1]})

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

def specificQuestion(request, postTitle):

    try:
        questionData = Question.objects.get(title=postTitle)
        # print("discussionData " ,discussionData)
        # print(DiscussionComment.objects.get())
        comments = QuestionComment.objects.filter(parent=questionData)
        # print(comments)
        ret = render(request, 'specificQuestion.html',
                  {'questionData': questionData, 'comments': comments})
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

def questionPostComment(request, postTitle):
    username = checkLogin(request)
    if username == False:
        return HttpResponseRedirect('/')
    comment = request.POST.get('comment', '')
    if comment.replace(' ','') == '':
        return HttpResponseRedirect('/home/questions/' + postTitle + '/')
    commentObj = QuestionComment(author=User.objects.get(username=username), parent=Question.objects.get(title=postTitle), date=datetime.date.today(), content=comment)
    print(username)

    commentObj.save()
    return HttpResponseRedirect('/home/questions/'+postTitle+'/')

def profile(request):
    username = checkLogin(request)
    if username == False:
        return HttpResponseRedirect('/')

    return render(request, 'profile.html', {'username': username})


def new_discussion(request):
    username = checkLogin(request)
    if username == False:
        return HttpResponseRedirect('/')
    if request.method == "POST":
        title = request.POST.get('title','')
        content = request.POST.get('content', '')
        try:
            Discussion.objects.get(title = title)
            return HttpResponseRedirect('/home/new-discussion/')
        except Discussion.DoesNotExist:
            discussionObject = Discussion(author=User.objects.get(username=username), date=datetime.date.today(), content=content,title=title)
            discussionObject.save();
        return HttpResponseRedirect('/home/discussions/')

    return render(request, 'new-discussion.html')

def new_question(request):
    username = checkLogin(request)
    if username == False:
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        try:
            Question.objects.get(title = title)
            return HttpResponseRedirect('/home/new-question/')
        except Question.DoesNotExist:
            questionObject = Question(author=User.objects.get(username=username), date=datetime.date.today(), content=content,title=title)
            questionObject.save();
        return HttpResponseRedirect('/home/questions/')

    return render(request,  'new-question.html')