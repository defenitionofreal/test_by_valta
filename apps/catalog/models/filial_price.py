from django.db import models


class FilialPrice(models.Model):
    """
    Извиняюсь, но здесь я убрал _id из названий product и filial
    так как это не совсем правильно и если обращаться к данным полям через ORM,
    то может получиться что-то вроде product_id_id и filial_id_id :(
    """
    product = models.ForeignKey("catalog.Product",
                                on_delete=models.CASCADE,
                                related_name="filial_prices")
    filial = models.ForeignKey("catalog.Filial",
                               on_delete=models.CASCADE,
                               related_name="filial_prices")
    price = models.DecimalField(decimal_places=2,
                                max_digits=10)

    class Meta:
        unique_together = ('product', 'filial',)
