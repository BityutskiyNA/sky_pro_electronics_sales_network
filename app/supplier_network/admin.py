from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from mptt.admin import MPTTModelAdmin
from django.urls import reverse

from .models import Counterparty, Contacts, Products


class TounListFilter(admin.SimpleListFilter):
    title = _('city')
    parameter_name = 'city'

    def lookups(self, request, model_admin):
        return tuple((x.contact, _(x.contact, )) for x in Contacts.objects.filter(type_contacts=3))

    def queryset(self, request, queryset):
        if 'city' in self.used_parameters.keys():
            queryset = Counterparty.objects.prefetch_related('contacts').filter(
                contacts__type_contacts=3, contacts__contact=self.used_parameters['city']
            )
        return queryset


class ProductsInstanceInline(admin.TabularInline):
    model = Products


class ContactsInstanceInline(admin.TabularInline):
    model = Contacts


class CounterpartyInstanceInline(admin.TabularInline):
    model = Counterparty
    fields = ('title', 'debt')


@admin.register(Counterparty)
class CounterpartyAdmin(MPTTModelAdmin):
    fields = ('level', 'type_counterparty', 'title', 'parent', 'debt', 'created')
    list_display = ('type_counterparty', 'title', 'debt', 'created', 'parent', 'view_odj_link')
    list_display_links = ('title',)
    readonly_fields = ('created', 'level')
    inlines = [CounterpartyInstanceInline, ContactsInstanceInline, ProductsInstanceInline]
    list_filter = (TounListFilter,)
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
