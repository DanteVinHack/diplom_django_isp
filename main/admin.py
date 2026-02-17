from django.contrib import admin
from .models import Position, Passport, Worker

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(Passport)
class PassportAdmin(admin.ModelAdmin):
    list_display = ["serial", "number", "date_of_birth", "date_issue"]
    list_filter = ["date_of_birth", "date_issue"]

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ["login", "password", "fio", "passport_id", "position_id"]
    list_filter = ["login", "fio"]