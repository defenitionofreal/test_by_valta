from django.db import models


class Characteristic(models.Model):
    """
    Про поле self, конечно удобней и привычней ссылться на "self",
    а не называться self, но тем не меннее я решил выбрать on_delete=PROTECT,
    но так же бывает SET_NULL. Тут уже как задача стоит, про это ничего не было
    сказано поэтому я выбрал первый вариант.
    Явно линейно удаляем дерево так же как и создаём.
    """
    self = models.ForeignKey("Characteristic",
                             on_delete=models.PROTECT,
                             null=True,
                             blank=True)
    name = models.CharField(max_length=255)
    product_id = models.ManyToManyField("catalog.Product",
                                        related_name='characteristics')

    def __str__(self):
        return self.name
