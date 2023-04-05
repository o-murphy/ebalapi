from django.contrib import admin


from . import diameter
from . import caliber
from . import bullet
from . import cartridge


# title settings
admin.site.site_title = 'E-Ballistics API'
admin.site.site_header = 'E-Ballistics API'
admin.site.index_title = 'E-Ballistics API'

# Register your models here.
