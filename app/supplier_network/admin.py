from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from django.utils.translation import gettext_lazy as _
from mptt.admin import MPTTModelAdmin
from django.urls import reverse
from django.utils.http import urlencode

from .models import Counterparty, Contacts, Products


class TounListFilter(admin.SimpleListFilter):
    title = _('city')
    parameter_name = 'city'

    def queryset(self, request, queryset):
        a = 0
        return queryset


class ProductsInstanceInline(admin.TabularInline):
    model = Products


class ContactsInstanceInline(admin.TabularInline):
    model = Contacts


class CounterpartyInstanceInline(admin.TabularInline):
    model = Counterparty
    fields = ('title', 'debt')
    # filter_horizontal = ('city',)


@admin.register(Counterparty)
class CounterpartyAdmin(MPTTModelAdmin):
    fields = ('level', 'type_counterparty', 'title', 'parent', 'debt', 'created', ('email','country','city','street','house_number'))
    list_display = ('type_counterparty', 'title', 'debt', 'created', 'parent','view_odj_link')
    list_display_links = ('title',)
    # # search_fields = ['username', 'user']
    readonly_fields = ('created',)
    inlines = [CounterpartyInstanceInline, ContactsInstanceInline, ProductsInstanceInline]
    list_filter = ('city',)
    actions = ['make_published']

    def view_odj_link(self, obj):
        if obj.parent:

            return u'<a href="{0}">{1}</a>'.format(reverse('admin:supplier_network_counterparty_change',
                                                           args=(obj.parent.pk,)),
                                                           obj.parent)
        else:
            return obj.parent

    view_odj_link.allow_tags = True
    view_odj_link.admin_parent_field = 'parent'
    view_odj_link.short_description = "Поставщик"

    @admin.action(description='Удаляем задолжность перед поставщиками')
    def make_published(self, request, queryset):
        queryset.update(debt=0)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    ...


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    ...
