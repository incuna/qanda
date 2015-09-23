from django.db import models
from django.utils import timezone


class Answer(models.Model):
    body = models.TextField()
    question = models.ForeignKey('questions.Question', related_name='answers')
    created_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey('users.User', related_name='answers')


class Question(models.Model):
    name = models.CharField(max_length=255)
    body = models.TextField()
    accepted_answer = models.ForeignKey('questions.Answer', related_name='questions')
    created_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey('users.User', related_name='questions')


class AnswerVote(models.Model):
    vote = models.NullBooleanField()
    answer = models.ForeignKey('questions.Answer', related_name='votes')
    user = models.ForeignKey('users.User', related_name='answer_votes')


class QuestionVote(models.Model):
    vote = models.NullBooleanField()
    question = models.ForeignKey('questions.Question', related_name='votes')
    user = models.ForeignKey('users.User', related_name='question_votes')
