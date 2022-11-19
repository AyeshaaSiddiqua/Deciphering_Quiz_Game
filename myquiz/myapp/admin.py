from django.contrib import admin
from .models import Easy
from .models import Medium
from .models import Difficult
from .models import Team_A
from .models import Team_B

# Register your models here.

admin.site.register(Easy)
admin.site.register(Medium)
admin.site.register(Difficult)
admin.site.register(Team_A)
admin.site.register(Team_B)
