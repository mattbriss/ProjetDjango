import imp
from django.contrib import admin

from .models import Personnel
from .models import Commutateur
from .models import Routeur
from .models import Terminale
from .models import Vlan

admin.site.register(Personnel)
admin.site.register(Commutateur)
admin.site.register(Routeur)
admin.site.register(Terminale)
admin.site.register(Vlan)

# Register your models here.
