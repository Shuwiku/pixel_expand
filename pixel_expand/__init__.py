# -*- coding: utf-8 -*-
"""Небольшой скрипт, увеличивающий изображение."""

# Это позволит имортировать функцию напрямую из модуля
# Вместо:   from pixel_expand.expand import expand
# Будет:    from pixel_expand import expand
from .expand import expand  # noqa: F401
