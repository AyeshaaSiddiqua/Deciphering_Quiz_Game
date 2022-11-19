from django.shortcuts import render
from django.http import HttpResponse
from .models import Easy
from .models import Medium
from .models import Difficult
from .models import Team_A
from .models import Team_B
from django.core.paginator import Paginator

# Create your views here.

lst = []
answersE = Easy.objects.all()  
answersM = Medium.objects.all()
answersH = Difficult.objects.all()
anslistE = []
anslistM = []
anslistH = []
listA = []
listB = []
answersA = Team_A.objects.all()
answersB = Team_B.objects.all()
anslistA = []
anslistB = []

for i in answersE:
    anslistE.append(i.answer)

for i in answersM:
    anslistM.append(i.answer)

for i in answersH:
    anslistH.append(i.answer)

for i in answersA:
    anslistA.append(i.answer_A)

for i in answersB:
    anslistB.append(i.answer_B)

def welcome(request):
    lst.clear()
    listA.clear()
    listB.clear()
    return render(request, 'myapp/welcome.html')

def level(request):
    return render(request, 'myapp/level.html')

def quiz_easy(request):
    obj = Easy.objects.all()
    count = Easy.objects.all().count()
    paginator = Paginator(obj,1)
    try:
        page = int(request.GET.get('page','1'))  
    except:
        page = 1
    try:
        questions = paginator.page(page)
    except(EmptyPage , InvalidPage):
        questions = paginator.page(paginator.num_pages)
    return render(request, 'myapp/easyquiz.html',{'obj' : obj, 'questions':questions,'count':count})

def quiz_medium(request):
    obj = Medium.objects.all()
    count = Medium.objects.all().count()
    paginator = Paginator(obj,1)
    try:
        page = int(request.GET.get('page','1'))  
    except:
        page = 1
    try:
        questions = paginator.page(page)
    except(EmptyPage , InvalidPage):
        questions = paginator.page(paginator.num_pages)
    return render(request, 'myapp/mediumquiz.html',{'obj' : obj, 'questions':questions,'count':count})

def quiz_hard(request):
    obj = Difficult.objects.all()
    count = Difficult.objects.all().count()
    paginator = Paginator(obj,1)
    try:
        page = int(request.GET.get('page','1'))  
    except:
        page = 1
    try:
        questions = paginator.page(page)
    except(EmptyPage , InvalidPage):
        questions = paginator.page(paginator.num_pages)
    return render(request, 'myapp/hardquiz.html',{'obj' : obj, 'questions':questions,'count':count})

def result(request, lid):
    score = 0
    if lid == 1:
        for i in range(len(lst)):
            print(lst[i])
            print(anslistE[i])
            if lst[i] == anslistE[i]:
                score = score + 1
                print(score)
    elif lid == 2:
        for i in range(len(lst)):
            print(lst[i])
            print(anslistM[i])
            if lst[i] == anslistM[i]:
                score = score + 1
                print(score)
    elif lid == 3:
        for i in range(len(lst)):
            print(lst[i])
            print(anslistH[i])
            if lst[i] == anslistH[i]:
                score = score + 1
                print(score)
    else:
        print(Error)

    return render(request, 'myapp/result.html', {'score':score})

def save_ans(request):
    ans = request.GET['ans']
    lst.append(ans)
    print(lst)
    return ans

def quiz_BattleFaceoff(request,aid,bid):
    obj_A = Team_A.objects.get(id=aid)
    obj_B = Team_B.objects.get(id=bid)
    obj_A_id = int(obj_A.id) 
    next_A_id = int(obj_A.id) + 1
    obj_B_id = int(obj_B.id)
    next_B_id = int(obj_B.id) + 1

    context = {
         'obj_A_question_A': obj_A.question_A,
         'obj_A_option1_A': obj_A.option1_A,
         'obj_A_option2_A':obj_A.option2_A,
         'obj_A_option3_A': obj_A.option3_A,
         'obj_A_option4_A': obj_A.option4_A,
         'obj_A_hint_A': obj_A.hint_A,
         'obj_A_id': obj_A_id,
         'next_A': next_A_id,
         'obj_B_question_B': obj_B.question_B,
         'obj_B_option1_B': obj_B.option1_B,
         'obj_B_option2_B':obj_B.option2_B,
         'obj_B_option3_B': obj_B.option3_B,
         'obj_B_option4_B': obj_B.option4_B,
         'obj_B_hint_B': obj_B.hint_B,
         'obj_B_id': obj_B_id,
         'next_B': next_B_id,

    }
    return render(request, 'myapp/quiz.html',context)

def save_ans_A(request):
    ans_A = request.GET['ans_A']
    listA.append(ans_A)
    print(listA)
    return ans_A

def save_ans_B(request):
    ans_B = request.GET['ans_B']
    listB.append(ans_B)
    print(listB)
    return ans_B


def battle_result(request):
    score_A = 0  
    score_B = 0
    winner = "" 
    for i in range(len(listA)):
        print(listA[i])
        print(anslistA[i])
        if listA[i] == anslistA[i]:
            score_A = score_A + 1
            print(score_A)

    for i in range(len(listB)):
        print(listB[i])
        print(anslistB[i])
        if listB[i] == anslistB[i]:
            score_B = score_B + 1
            print(score_B)
    
    if score_A > score_B:
        winner = 'PLAYER A'
        print("Winner A")
    elif score_A < score_B:
        winner = 'Team B'
        print("PLAYER B")
    else:
        winner = 'DRAW MATCH'
        print('DRAW MATCH')

    context = {
        'score_A': score_A,
        'score_B': score_B,
        'winner': winner
    }
    return render(request, 'myapp/battleresult.html',context)

