from django.contrib import admin
from .models import Sotrudniki, Podrazdeleniya, Doljnosti, Zadachi, Doljnost_sotrudnik, Sotrudnik_zadachi

admin.site.register(Sotrudniki)
admin.site.register(Podrazdeleniya)
admin.site.register(Doljnosti)
admin.site.register(Zadachi)
admin.site.register(Doljnost_sotrudnik)
admin.site.register(Sotrudnik_zadachi)
