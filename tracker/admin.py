from django.contrib import admin
from .models import Worker, Unit, Visit


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number')
    search_fields = ('name',)


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'worker')
    search_fields = ('name',)


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_time', 'unit', 'latitude', 'longitude')
    search_fields = ('unit__name', 'unit__worker__name')

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False



