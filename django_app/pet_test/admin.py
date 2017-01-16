from django.contrib import admin

from .models import Guests, ImportedData, UploadedFiles
from .admin_actions import GuestsAdmin, UploadedFilesAdmin, ImportedDataAdmin

admin.site.register(Guests, GuestsAdmin)
admin.site.register(ImportedData, ImportedDataAdmin)
admin.site.register(UploadedFiles, UploadedFilesAdmin)
