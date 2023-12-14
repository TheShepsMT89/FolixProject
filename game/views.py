from django.shortcuts import render, redirect
from .models import *
from core.models import Topic
import random

# Create your views here.

def ex1(request):

    e_subtopic = Subtopic.objects.all()
    
    topic_ids = list(Topic.objects.all().values_list("id", "name"))
    
    exercise_values = list(
        Exercise.objects.all().values_list("id", "eng_phrase", "spa_phrase", "topic")
    )

    words_values = list(
        Words.objects.all().values_list("word", "trans", "highlighted", "exercise")
    )

    list_exercise = []
    list_words = []

    
    
    x = random.randint(1, len(topic_ids))

    random.shuffle(exercise_values)


    for ex_value in exercise_values:
        if len(list_exercise) == 3:
            break
        elif ex_value[-1] == int(x):
            list_exercise.append(ex_value)

    for w_value in words_values:
        for le in list_exercise:
            if w_value[-1] == le[0]:
                list_words.append(w_value)

    context = {"exercise": list_exercise, "words": list_words, "e_subtopic": e_subtopic}

    return render(request, "game/ex1.html", context)
