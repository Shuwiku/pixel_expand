# -*- coding: utf-8 -*-
"""Небольшой скрипт, увеличивающий изображение."""

from typing import Any, Optional

from PIL import Image


exp_image: Image.Image
exp_image_h: int = 0
exp_image_w: int = 0


def _expand_pixel(
    pixel: float | tuple[int, ...],
    scale: int
) -> None:
    """Увеличивает пиксель в scale раз.

    Args:
        pixel (float | tuple[int, ...]): Пиксель изображения.
        scale (int): Масштаб увеличения пикселя.
    """
    global exp_image, exp_image_h, exp_image_w

    # Цикл по высоте
    for _ in range(scale):

        # Цикл по ширине
        for __ in range(scale):

            exp_image.putpixel(
                xy=(exp_image_w, exp_image_h),
                value=pixel
            )
            exp_image_w += 1

        exp_image_w -= scale
        exp_image_h += 1


def expand(
    image_in: Any,
    image_out: Any,
    scale: int
) -> None:
    """Увеличивает изображение в scale раз.

    Внимание! Увеличенное изображение будет формата PNG.

    Args:
        image_in (Any): Любой тип, который сможет открыть PIL.Image.
        image_out (Any): Любой тип, в который сможет сохранить PIL.Image.
        scale (int): Масштаб увеличения изображения.
    """
    global exp_image, exp_image_h, exp_image_w

    with Image.open(fp=image_in) as image:
        image.convert(mode="RGBA")
        width: int = image.size[0]
        height: int = image.size[1]

        exp_image = Image.new(
            mode="RGBA",
            size=(width * scale, height * scale)
        )
        exp_image_h = 0
        exp_image_w = 0

        for image_h in range(height):

            for image_w in range(width):

                pixel: Optional[float | tuple[int, ...]] = image.getpixel(
                    xy=(image_w, image_h)
                )
                if pixel is not None:
                    _expand_pixel(
                        pixel=pixel,
                        scale=scale
                    )
                exp_image_w = image_w * scale + scale
                exp_image_h = image_h * scale

            exp_image_w = 0
            exp_image_h = (image_h + 1) * scale

    exp_image.save(image_out, format="PNG")
    exp_image.close()
    del exp_image
