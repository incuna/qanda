from django.test import TestCase
from incuna_test_utils.utils import field_names

from ..models import Answer, AnswerVote, Question, QuestionVote


class TestAnswer(TestCase):
    def test_fields(self):
        expected = {
            'id',
            'body',
            'question',
            'created_date',

            # incoming relationship
            'questions',
            'user',
            'votes',
        }
        fields = field_names(Answer)
        self.assertEqual(fields, expected)


class TestAnswerVote(TestCase):
    def test_fields(self):
        expected = {'id', 'user', 'vote', 'answer'}
        fields = field_names(AnswerVote)
        self.assertEqual(fields, expected)


class TestQuestion(TestCase):
    def test_fields(self):
        expected = {
            'id',
            'name',
            'body',
            'created_date',
            'accepted_answer',

            # incoming relationships
            'answers',
            'user',
            'votes',
        }
        fields = field_names(Question)
        self.assertEqual(fields, expected)


class TestQuestionVote(TestCase):
    def test_fields(self):
        expected = {'id', 'user', 'vote', 'question'}
        fields = field_names(QuestionVote)
        self.assertEqual(fields, expected)
