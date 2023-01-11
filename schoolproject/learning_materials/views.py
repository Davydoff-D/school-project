from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Group, Material, Question, AnswerModel
from .forms import QuestionForm


def index(request):
    return render(request, 'learning_materials/index.html')


def materials(request):
    materials = Material.objects.all()
    group = get_object_or_404(Group,)
    context = {
        "materials": materials,
        "group": group
    }
    return render(request, 'learning_materials/materials.html', context)


def materials_detail(request, material_id):
    material = get_object_or_404(Material, pk=material_id)
    # question = Question.objects.get(material__id=material_id, pk=question_id)
    print(material_id)
    if material_id == 1:
        first = True
        context = {
            "material": material,
            "first": first,
        }
        return render(request, 'learning_materials/material_detail.html', context)
    elif material_id == 2:
        second = True
        context = {
            "material": material,
            "second": second,
        }
        return render(request, 'learning_materials/material_detail.html', context)
    else:
        context = {
            "material": material,
        }
        return render(request, 'learning_materials/material_detail.html', context)


def tasks(request, material_id):
    material = get_object_or_404(Material, pk=material_id)
    questions = Question.objects.all()
    form = QuestionForm(request.POST or None)
    if form == Question.correct_answer:
        OK = True
        context = {
                    "material": material,
                    "form": form,
                    "questions": questions,
                    "OK": OK,
                }
        return render(request, 'learning_materials/tasks.html', context)
    context = {
                    "material": material,
                    "form": form,
                    "questions": questions,
                }
    return render(request, 'learning_materials/tasks.html', context)


# def tasks_detail(request, material_id, question_id):
#     material = get_object_or_404(Material, pk=material_id)
#     question = get_object_or_404(Question, pk=question_id)
#     print(question_id)
#     context = {
#                     "material": material,
#                     "question": question,
#                 }
#     return render(request, 'learning_materials/tasks_detail.html', context)

def tasks_detail(request, material_id, question_id):
    material = get_object_or_404(Material, pk=material_id)
    # question = Question.objects.get(material__id=material_id, id=question_id)
    question = get_object_or_404(Question, pk=question_id) # get_object_filter(material=material)
    if request.method == 'POST':
        form = QuestionForm(request.POST or None)
        if form.is_valid():
            answer = form.cleaned_data['text']
            correct_answer = Question.objects.get(id=question_id).correct_answer
            if answer == correct_answer:
                current_question_id = question_id
                next_question_id = int(current_question_id) + 1
                ok_answer = True
                ok_answer_tasks = True

                if (next_question_id - 1) % 5 == 0:
                    home = True
                    if question_id == 5 or question_id == 10:
                        fifth = True
                        context = {
                            "material": material,
                            "form": form,
                            "question": question,
                            "ok_answer": ok_answer,
                            "next_question_id": next_question_id,
                            "home": home,
                            "fifth": fifth,
                        }
                        return render(request, 'learning_materials/tasks_detail.html', context)
                    else:
                        context = {
                            "material": material,
                            "form": form,
                            "question": question,
                            "ok_answer": ok_answer,
                            "next_question_id": next_question_id,
                            "home": home,
                        }
                        return render(request, 'learning_materials/tasks_detail.html', context)
                elif question_id == 1 or question_id == 6 or question_id == 7 or question_id == 8 or question_id == 9:
                    first = True
                    context = {
                        "material": material,
                        "form": form,
                        "question": question,
                        "ok_answer": ok_answer,
                        "next_question_id": next_question_id,
                        "ok_answer_tasks": ok_answer_tasks,
                        "first": first,
                    }
                    return render(request, 'learning_materials/tasks_detail.html', context)
                elif question_id == 2:
                    second = True
                    context = {
                        "material": material,
                        "form": form,
                        "question": question,
                        "ok_answer": ok_answer,
                        "next_question_id": next_question_id,
                        "ok_answer_tasks": ok_answer_tasks,
                        "second": second,
                    }
                    return render(request, 'learning_materials/tasks_detail.html', context)
                elif question_id == 3:
                    third = True
                    context = {
                        "material": material,
                        "form": form,
                        "question": question,
                        "ok_answer": ok_answer,
                        "next_question_id": next_question_id,
                        "ok_answer_tasks": ok_answer_tasks,
                        "third": third,
                    }
                    return render(request, 'learning_materials/tasks_detail.html', context)
                elif question_id == 4:
                    fourth = True
                    context = {
                        "material": material,
                        "form": form,
                        "question": question,
                        "ok_answer": ok_answer,
                        "next_question_id": next_question_id,
                        "ok_answer_tasks": ok_answer_tasks,
                        "fourth": fourth,
                    }
                    return render(request, 'learning_materials/tasks_detail.html', context)

            else:
                messages.error(request, 'Ответ неправильный. Попробуйте ещё.')
                context = {
                        "material": material,
                        "form": form,
                        "question": question,
                    }
                return render(request, 'learning_materials/tasks_detail.html', context)

    else:
        form = QuestionForm(request.POST or None)
    context = {
                    "material": material,
                    "form": form,
                    "question": question,
                }
    return render(request, 'learning_materials/tasks_detail.html', context)


def answers(request, material_id, question_id, answermodel_id):
    material = get_object_or_404(Material, pk=material_id)
    # question = get_object_or_404(Question, pk=question_id)
    question = Question.objects.get(material__id=material_id, id=question_id)
    answermodel = AnswerModel.objects.get(question__id=question_id, id=answermodel_id)
    # answermodel = get_object_or_404(AnswerModel, id=question_id, id=answermodel_id)
    print(answermodel_id)
    form = QuestionForm(request.POST or None)
    context = {
                    "material": material,
                    "form": form,
                    "question": question,
                    "answermodel": answermodel,
                }
    return render(request, 'learning_materials/answers.html', context)


# def quiz(request, material_id):
#     if request.method == 'POST':
#         form = QuestionForm(request.POST)
#         if form.is_valid():
#             # Check if the user's answer is correct
#             user_answer = form.cleaned_data['user_answer']
#             correct_answer = form.cleaned_data['correct_answer']
#             if user_answer.lower() == correct_answer.lower():
#                 # The user's answer is correct
#                 # Get the next question from the database
#                 next_question = Question.objects.filter(id__gt=form.instance.id).first()
#                 if next_question:
#                     # If there is a next question, display it
#                     form = QuestionForm(instance=next_question)
#                 else:
#                     # If there are no more questions, display a message indicating that the quiz is complete
#                     form = None
#                     message = "Quiz complete!"
#             else:
#                 # The user's answer is incorrect
#                 message = "Incorrect answer. Please try again."
#     else:
#         form = QuestionForm()
#         message = ""
#     return render(request, 'learning_materials/tasks.html', {'form': form, 'message': message})
