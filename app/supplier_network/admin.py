from django.contrib import admin
from .models import Counterparty, Contacts, Products



class ProductsInstanceInline(admin.TabularInline):
    model = Products

class ContactsInstanceInline(admin.TabularInline):
    model = Contacts

class CounterpartyInstanceInline(admin.TabularInline):
    model = Counterparty

@admin.register(Counterparty)
class CounterpartyAdmin(admin.ModelAdmin):
    fields = ('type_counterparty', 'title','provider','debt','created')
    list_display = ('type_counterparty', 'title','provider','debt','created')
    # search_fields = ['username', 'user']
    readonly_fields = ('created',)
    inlines = [CounterpartyInstanceInline, ContactsInstanceInline,  ProductsInstanceInline]


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    ...


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    ...