from core.models import CreatedModel, PubdateModel

from django.db import models


class Material(PubdateModel):
    title = models.CharField(
        max_length=200, verbose_name='Заголовок материала', default='Заголовок'
    )
    text = models.TextField(
        verbose_name='Текст материала',
        help_text='Введите текст материала',
    )
    group = models.ForeignKey(
        'Group',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='materials',
        verbose_name='Группа',
        help_text='Группа, к которой будет относиться материал',
    )

    class Meta:
        ordering = ('pub_date',)
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'

    def __str__(self):
        return self.text


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок группы')
    slug = models.SlugField(unique=True, verbose_name='Ссылка на раздел')

    def __str__(self):
        return self.title


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=200)
    material = models.ForeignKey(
        'Material',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='questions',
        verbose_name='Материал',
        help_text='Материал, к которому будут относиться вопросы',
    )

    def __str__(self):
        return self.question_text


class AnswerModel(models.Model):
    question = models.ForeignKey(
        'Question',
        on_delete=models.CASCADE,
        related_name='answers',
        verbose_name='Ответ к вопросу',
        help_text='Вопрос, на который будет дан ответ',
    )
    text = models.TextField(
        verbose_name='Текст ответа',
        help_text='Текст ответа вводите строго с использованием специальных символов, без пробелов',
    )
