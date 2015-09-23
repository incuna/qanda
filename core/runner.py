from colour_runner.django_runner import ColourRunnerMixin
from django.test.runner import DiscoverRunner


class TestRunner(ColourRunnerMixin, DiscoverRunner):
    pass
