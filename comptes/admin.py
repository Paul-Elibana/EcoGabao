from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import Profil


class ProfilInline(admin.StackedInline):
    model = Profil
    can_delete = False
    verbose_name_plural = _('Profil')


@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'ville', 'actif', 'date_creation')
    list_filter = ('role', 'actif')
    search_fields = ('user__username', 'user__email', 'telephone', 'ville')
    readonly_fields = ('date_creation', 'date_modification')


class UserAdmin(BaseUserAdmin):
    inlines = (ProfilInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
