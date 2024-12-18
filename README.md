# Pixel Expand

Небольшой скрипт, позволяющий увеличить размер изображения, увеличивая размер его пикселей. Вероятно, далеко не самый оптимизированный, но и лицензия Unlicense.

<p align="center">
    <img alt="Широ ^-^" width="500" src="https://i.ibb.co/gyjPNyr/shiro.gif"/>
</p>

<p align="center">
    <img alt="Python 3.12" src="https://img.shields.io/badge/Python-3.12-yellow?style=flat">
    <img alt="Версия 0.1.0" src="https://img.shields.io/badge/%D0%92%D0%B5%D1%80%D1%81%D0%B8%D1%8F-0.1.0-purple?style=flat">
    <img alt="Лицензия Unlicense" src="https://img.shields.io/badge/%D0%9B%D0%B8%D1%86%D0%B5%D0%BD%D0%B7%D0%B8%D1%8F-Unlicense-aqua?style=flat">
</p>

## Использование

```python
from pixel_expand import expand

# Увеличит изображение в 4 раза
expand(
    image_in="image.png"
    image_out="image_exp.png",
    scale=4
)
```

Смотрите также [примеры использования](https://github.com/Shuwiku/Shuwiku/tree/main/pixel_expand).

## Как это работает

Предположим, что у нас есть изображение 3x3 пикселя. Представим его так:

```python
[1][2][3]
[4][5][6]
[7][8][9]
```

Если данное изображение увеличить в 2 раза, то оно станет следующим:

```python
[1][1][2][2][3][3]
[1][1][2][2][3][3]
[4][4][5][5][6][6]
[4][4][5][5][6][6]
[7][7][8][8][9][9]
[7][7][8][8][9][9]
```

Это всё. Больше скрипт ничего не делает.
