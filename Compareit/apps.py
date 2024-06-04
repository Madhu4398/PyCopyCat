from django.apps import AppConfig
import os

class PlagiarismConfig(AppConfig):
    """django.core.exceptions.ImproperlyConfigured: Cannot import 'apps.plagiarism'.
     Check that 'Compareit.apps.PlagiarismConfig.name' is correct."""
    AppConfig.default = False
    name = 'plagiarism'


