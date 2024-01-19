from rest_framework import serializers

from main.models import NetworkNode


class FactoryValidator:
    def __init__(self, category, supplier):
        self.category = category
        self.supplier = supplier

    def __call__(self, attrs):
        if attrs[self.category] == 'Завод' and self.supplier in attrs:
            raise serializers.ValidationError(
                "Завод является изначальным звеном сети, у него не может быть поставщиков")


class RetailNetworkValidator:
    def __init__(self, category, supplier):
        self.category = category
        self.supplier = supplier

    def __call__(self, attrs):
        if attrs[self.category] == 'Розничная сеть':
            if self.supplier not in attrs:
                raise serializers.ValidationError("У розничной сети должен быть поставщик")
            else:
                supplier_node = NetworkNode.objects.get(id=attrs[self.supplier].id)
                if supplier_node.category == 'Розничная сеть' or supplier_node.category == 'ИП':
                    raise serializers.ValidationError("Поставщиком розничной сети может быть только завод")


class SoleProprietorValidator:
    def __init__(self, category, supplier):
        self.category = category
        self.supplier = supplier

    def __call__(self, attrs):
        if attrs[self.category] == 'ИП':
            if self.supplier not in attrs:
                raise serializers.ValidationError("У ИП должен быть поставщик")
            else:
                supplier_node = NetworkNode.objects.get(id=attrs[self.supplier].id)
                if supplier_node.category == 'ИП':
                    raise serializers.ValidationError("Поставщиком ИП может быть только завод или розничная сеть")


class DebtValidator:
    def __init__(self, category, debt):
        self.category = category
        self.debt = debt

    def __call__(self, attrs):
        category_to_check = attrs[self.category]
        if category_to_check == "Завод":
            if self.debt in attrs and attrs[self.debt] != 0:
                raise serializers.ValidationError("У завода не может быть задолженности")
        elif category_to_check == "Розничная сеть":
            if self.debt not in attrs:
                raise serializers.ValidationError("У розничной сети должна быть информация о задолженности")
            else:
                if attrs[self.debt] < 0:
                    raise serializers.ValidationError("Долг не может быть отрицательным числом")
        else:
            if self.debt not in attrs:
                raise serializers.ValidationError("У ИП должна быть информация о задолженности")
            else:
                if attrs[self.debt] < 0:
                    raise serializers.ValidationError("Долг не может быть отрицательным числом")


class ProhibitedFieldsValidator:
    def __init__(self, category, supplier, debt):
        self.category = category
        self.supplier = supplier
        self.debt = debt

    def __call__(self, attrs):
        if self.category in attrs:
            raise serializers.ValidationError("Запрещено изменять поле category")
        elif self.supplier in attrs:
            raise serializers.ValidationError("Запрещено изменять поле supplier")
        elif self.debt in attrs:
            raise serializers.ValidationError("Запрещено изменять поле debt")
