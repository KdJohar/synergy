from django.contrib import admin
from .models import TableTennis, Badminton, Volleyball, Chess
# Register your models here.

class CommonCriteriaAdmin(admin.ModelAdmin):
    # common for badminton and tabletennis
    list_display = ('player_name', 'event_type', 'course', 'contact', 'email', )
    list_filter = ('event_type', 'course', )
    search_fields = ('player_name', 'second_player_name', 'contact', 'email', )

class VolleyballAdmin(admin.ModelAdmin):
    # common for badminton and tabletennis
    list_display = ('captain', 'course', 'contact', 'email', )
    list_filter = ( 'course', )
    search_fields = ('captain', 'contact', 'email', )

class ChessAdmin(admin.ModelAdmin):
    # common for badminton and tabletennis
    list_display = ('player_name', 'course', 'contact', 'email', )
    list_filter = ( 'course', )
    search_fields = ('player_name', 'contact', 'email', )

admin.site.register(TableTennis, CommonCriteriaAdmin)
admin.site.register(Badminton, CommonCriteriaAdmin)
admin.site.register(Volleyball, VolleyballAdmin)
admin.site.register(Chess, ChessAdmin)