from django.contrib import admin

from .models import Guests
from admin_actions import ExportAsXls

admin.site.register(Guests,ExportAsXls)

