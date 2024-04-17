import os
from django.core.exceptions import ValidationError 

def validate_presentation_file(value):
    file_ext = os.path.splitext(value.name)[1]

    supported_extensions = [".pdf", "pptx"]
    if not (file_ext.lower() in supported_extensions):
        raise ValidationError("Unsupported file extension.")
    