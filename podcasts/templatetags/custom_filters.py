# custom_filters.py
from django import template
import datetime

register = template.Library()

@register.filter(name='convert_duration')
def convert_duration(milliseconds):
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)

    return "{:2} Hours {:2} Minutes".format(int(hours), int(minutes))
