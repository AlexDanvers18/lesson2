"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

list_products = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]





all_summ_prod = 0

for product in list_products:
  product_name = product['product']
  product_sold = product['items_sold']
  summ_prod = 0
  for item in product['items_sold']:
    summ_prod += item
  print(f'Суммарное количество продаж для {product_name} = {summ_prod}')

  avg_summ_prod = int(summ_prod / (len(product['items_sold'])))
  print(f'Cреднее количество продаж для {product_name}: {avg_summ_prod}')
  

  all_summ_prod += sum(product['items_sold']) 
  avg_summ = int(all_summ_prod / len(list_products))

print(f'Суммарное количество продаж всех товаров = {all_summ_prod}')
print(f'Cреднее количество продаж всех товаров: {avg_summ}')




if __name__ == "__main__":
    main()
