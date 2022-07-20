Тестовое задание
=====================
**Описание**

Приложение должно разворачиватся командами: docker-compose build, docker-compose up.
  
Приложение Accounts.

Создайте модель пользователя, основным индефикатором пользователя должна быть почта а не username.
Авторизация в приложении должна быть по полям - email, password. 

Приложение Catalog.

 - class Product
    - name (str)
   
 - class Filial
    - name (str)
    - region (int)
   
 - class Characterictic
     - self (ForeignKey -> Characterictic) 
     - name (str)
   - product_id (ManyToManyField <- Product)
   
 - class FilialPrice
    - product_id (ForeignKey -> Product)
    - filial_id (ForeignKey -> Filial)
    - price (int)

Реализуйте роуты и предоставления для них, желательно с помощью rest_framework.decorators.action в одном классе.

- catalog/?filial=id список объектов Product + стоимость
- catalog/<product_id>/?filial=id данные объекта Product + стоимость
- catalog/<product_id>/price/ данные объекта FilialPrice
- catalog/<product_id>/price/?filial=id данные объекта FilialPrice фильтруемые по филиалу
- catalog/<product_id>/characteristic/  все связанные с этим товаром характеристики
- catalog/?filial=id&characteristic=id
Возвращать товары с стоимостью в этом филиале, фильтровать список по характеристике

Все модели должны иметь сериализаторы.
Сериализаторы должны поддерживать создание и обновление объектов.
______
**Пометка**

- Я уточнил какого вида должны отдаваться объекты и на языке моделей это {"id": Product.id, "name": Product.name "price":FilialPrice.price}.
- Обычный роут /catalog/, не определились точно мне в ответе что должен возвращать и поэтому я возвращаю по умолчанию queryset.
- Я уточнил про @action методы, если ждут от меня все запросы через экшен. Здесь ответа не было поэтому я сделал два action метода так как посчитал что ?filial=<> и ?characteristic=<> это квери параметры в урле для фильтрации ежели прямо другой путь.
- Убрал из названия полей product_id, filial_id этот _id так как не комильфо. В ORM из-за этого product_id_id.
- Вместо папки settings  у меня папка project/settings/, где разные файлы для настроек.
______
Для того, чтобы запустить проект локально, выполните следующие команды:
```
git clone https://github.com/defenitionofreal/test_by_valta.git
cd test_by_valta
docker-compose build
docker-compose up
```

Новая БД пустая. Запустите следующие команды, чтобы запонить БД:
```
docker exec -it web bash
./manage.py loaddata fixtures/db.json
```

Если статика не подтянулось:
```
docker exec -it web bash
./manage.py collectstatic --noinput
```
______
superuser info:

email: admin@admin.ru
pass: admin
______
swagger 127.0.0.1:8000/swagger/
