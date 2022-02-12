from django.core.exceptions import ValidationError


def validate_title_length(value):
    value_words = value.split()

    if len(value_words) == 1 and len(value_words[0]) < 6:
        raise ValidationError(
            'title must be at least one word or 6 letters'
        )


def validate_caption_length(value):
    value_words = value.split()
    if len(value_words) > 130 or len(value_words) < 10:
        raise ValidationError(
            'title must between 10 or 130 words'
        )
