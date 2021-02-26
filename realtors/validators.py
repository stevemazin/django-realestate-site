from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions

def image_restriction(image):
    image_width, image_height = get_image_dimensions(image)
    if image_width >= image_height +2 or image_width <= image_height -2:
        raise ValidationError('Avatar image dimensions needs to be a square')