from django.db import models


class Counterparty(models.Model):
    class TypeCounterparty(models.IntegerChoices):
        factory = 1, "Завод"
        retail_network = 2, "Розничная сеть"
        ind_entrepreneur = 3, "Индивидуальный предприниматель"

    type_counterparty = models.PositiveSmallIntegerField(verbose_name="Роль",
                                                         choices=TypeCounterparty.choices,
                                                         default=TypeCounterparty.factory)
    title = models.CharField(verbose_name="Название", max_length=255)
    provider = models.OneToOneField('Counterparty',
                                    verbose_name="Поставщик",
                                    on_delete=models.PROTECT,
                                    blank=True,
                                    null=True)
    # contacts = models.ForeignKey(Contacts, verbose_name="Контакты", on_delete=models.PROTECT)
    # products = models.ManyToManyField(Products, verbose_name="Продукты")
    debt = models.FloatField(verbose_name="Задолженность", max_length=255)
    created = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Контрагент"
        verbose_name_plural = "Контрагент"

    def __str__(self):
        return self.title

class Contacts(models.Model):
    class ContactType(models.IntegerChoices):
        email = 1, "Email"
        country = 2, "Страна"
        city = 3, "Город"
        street = 4, "Улица"
        house_number = 5, "Номер дома"

    type_contacts = models.PositiveSmallIntegerField(verbose_name="Тип контакта",
                                                     choices=ContactType.choices,
                                                     default=ContactType.house_number)
    contact = models.CharField(verbose_name="Контакт", max_length=255)
    counterparty = models.ForeignKey(Counterparty, verbose_name="Контрагент", on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакт"

    def __str__(self):
        return self.contact


class Products(models.Model):
    title = models.CharField(verbose_name="Название", max_length=255)
    counterparty = models.ForeignKey(Counterparty, verbose_name="Контрагент", on_delete=models.PROTECT)
    model = models.CharField(verbose_name="Модель", max_length=255)
    release_date = models.DateTimeField(verbose_name="Дата выхода продукта на рынок")


    class Meta:
        verbose_name = "Номенклатура"
        verbose_name_plural = "Номенклатура"

    def __str__(self):
        return self.title