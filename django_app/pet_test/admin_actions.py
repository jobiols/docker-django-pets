# -*- coding: utf-8 -*-
from django.contrib import admin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from xlsxwriter import Workbook
import datetime
import io
import logging
logger = logging.getLogger('')

class ExportAsXls(admin.ModelAdmin):

    actions = ['export_as_xls']

    def export_as_xls(self, request, queryset):
        """
        Generic xls export admin action.
        """
        if not request.user.is_staff:
            raise PermissionDenied
        opts = self.model._meta
        output = io.BytesIO()
        wb = Workbook(output, {'in_memory': True})
        ws0 = wb.add_worksheet()
        col = 0
        field_names = []
        # write header row
        for field in opts.fields:
            ws0.write(0, col, field.name)
            field_names.append(field.name)
            col = col + 1
        row = 1
        # Write data rows
        for obj in queryset:
            col = 0
            for field in field_names:
#               val = unicode(getattr(obj, field)).strip()
                val = getattr(obj, field)
                if type(val) == type(datetime.datetime.now()):
                    val = val.date().strftime('%d/%m/%Y') # replace(tzinfo=None)
                ws0.write(row, col, val)
                col = col + 1
            row = row + 1

        wb.close()
        output.seek(0)
        response = HttpResponse(
            output.read(),
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response['Content-Disposition'] = "attachment; filename=test.xlsx"
        return response

    export_as_xls.short_description = "Exportar como planilla excel (xlsx)"
