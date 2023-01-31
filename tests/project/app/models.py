from django.db import models

from file_validator.constants import ALL, PYTHON_MAGIC
from file_validator.models import ValidatedFileField
from file_validator.models import FileValidator
from tests.fixtures import PNG_OBJECT, MP3_OBJECT, BAD_OBJECT


class TestFileModel(models.Model):
    test_file = ValidatedFileField(
        libraries=["all"],
        acceptable_mimes=[PNG_OBJECT['mime'], MP3_OBJECT['mime']],
        max_upload_file_size=1000000
    )


class TestFileModelWithFileValidator(models.Model):
    test_file = models.FileField(
        validators=[
            FileValidator(
                libraries=[PYTHON_MAGIC],
                acceptable_mimes=[PNG_OBJECT['mime'], MP3_OBJECT['mime']],
                max_upload_file_size=10485760
            )
        ]
    )


class TestFileModelWithFileValidatorSizeIsNone(models.Model):
    test_file = models.FileField(
        validators=[
            FileValidator(
                libraries=[ALL],
                acceptable_mimes=[PNG_OBJECT['mime'], MP3_OBJECT['mime']],
            )
        ]
    )


class TestFileModelWithFileValidatorLibraryIsNone(models.Model):
    test_file = models.FileField(
        validators=[
            FileValidator(
                acceptable_mimes=[PNG_OBJECT['mime'], MP3_OBJECT['mime']],
            )
        ]
    )

