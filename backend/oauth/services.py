import os

from django.core.exceptions import ValidationError


def validate_size_image(file_obj):
    """ Cheking size of image
    """
    megabyte_limit = 2  # Const size
    if file_obj.size > megabyte_limit * 1024 * 1024:
        raise ValidationError(f"Максимальный размер файла {megabyte_limit}MB")


def get_path_upload_avatar(instance, file):
    return f'avatar/user_{instance.id}/{file}'
