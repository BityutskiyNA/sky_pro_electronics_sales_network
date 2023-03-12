from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Counterparty(MPTTModel):
    class TypeCounterparty(models.IntegerChoices):
        factory = 0, "Завод"
        retail_network = 1, "Розничная сеть"
        ind_entrepreneur = 2, "Индивидуальный предприниматель"

    level = models.IntegerField(verbose_name="Уровень", default=0)
    type_counterparty = models.PositiveSmallIntegerField(verbose_name="Роль",
                                                         choices=TypeCounterparty.choices,
                                                         default=TypeCounterparty.factory)
    title = models.CharField(verbose_name="Название", max_length=255)
    parent = TreeForeignKey('Counterparty',
                            verbose_name="Поставщик",
                            on_delete=models.PROTECT,
                            blank=True,
                            null=True,
                            related_name='children')
    email = models.CharField(verbose_name="email", max_length=255, blank=True, null=True)
    debt = models.FloatField(verbose_name="Задолженность", max_length=255)
    created = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        verbose_name = "Контрагент"
        verbose_name_plural = "Контрагент"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        with Counterparty.objects.disable_mptt_updates():
            if self.type_counterparty == 0:
                self.level = 0
            elif self.parent.type_counterparty == 0:
                self.level = 1
            else:
                self.level = self.type_counterparty
            super().save(*args, **kwargs)


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
    counterparty = models.ForeignKey(Counterparty, verbose_name="Контрагент", on_delete=models.PROTECT, related_name="contacts",)

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
