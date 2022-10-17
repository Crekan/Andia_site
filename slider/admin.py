from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


admin.site.register(SliderModel)
admin.site.register(CardsBenefitsModel)
admin.site.register(LatestWork)
