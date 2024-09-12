from django.contrib.admin import register,ModelAdmin

from .models import *

@register(CoinWarning)
class CoinWarningAdmin(ModelAdmin):
    pass


