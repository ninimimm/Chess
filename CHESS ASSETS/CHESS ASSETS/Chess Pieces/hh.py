from PIL import Image

# Открываем изображение
image = Image.open("Pieces.png")  # Замените "your_image.jpg" на путь к вашему изображению

# Получаем размеры изображения
width, height = image.size

# Размер квадрата
square_size = 100

# Создаем папку для сохранения квадратов
import os
os.makedirs("output", exist_ok=True)  # Папка "output" будет создана в текущей директории

# Разрезаем изображение на квадраты
for x in range(0, width, square_size):
    for y in range(0, height, square_size):
        box = (x, y, x + square_size, y + square_size)
        square = image.crop(box)
        square.save(f"output/square_{x}_{y}.png")  # Сохраняем каждый квадрат с уникальным именем

# Закрываем изображение
image.close()
