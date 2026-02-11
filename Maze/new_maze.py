from __future__ import annotations

from random import randint
from typing import Callable, Dict, List, Tuple

from mlx import Mlx

# ============================================================
#               ТИПИ (для читабельності)
# ============================================================
Coord = Tuple[int, int]   # координати клітинки (x, y)
RGBA = bytes              # колір у форматі RGBA: bytes([R, G, B, A])


# ============================================================
#               ПАРСИНГ / ПІДГОТОВКА ДАНИХ
# ============================================================
def parse_maze(maze_str: str) -> List[str]:
    """
    Розбиває великий рядок-лабіринт на список рядків.

    Кожен рядок = один ряд у лабіринті.
    Кожен символ у рядку = одна клітинка (hex-цифра 0..F), яка кодує стіни.
    """
    return maze_str.split("\n")


def compute_scale(window_w: int, canvas_h: int, maze_rows: int, maze_cols: int) -> int:
    """
    Підбирає 'scale' (розмір клітинки в пікселях), щоб лабіринт вліз у полотно.

    window_w  - ширина зображення (пікселі)
    canvas_h  - висота зображення (пікселі)
    maze_rows - кількість рядків лабіринту
    maze_cols - кількість колонок лабіринту
    """
    # Скільки пікселів можна виділити на одну клітинку по висоті
    scale_h = canvas_h // maze_rows
    # Скільки пікселів можна виділити на одну клітинку по ширині
    scale_w = window_w // maze_cols
    # Беремо мінімум, щоб точно влізло і по ширині, і по висоті
    return min(scale_h, scale_w)


def build_path(path_str: str, start: Coord) -> List[Coord]:
    """
    Будує список координат шляху з рядка інструкцій (E,S,W,N).

    path_str - рядок типу "EESSWN..."
    start    - стартова координата (x, y)

    Повертає список клітинок, які проходить шлях (включно зі стартом).
    """
    path: List[Coord] = [start]

    for letter in path_str:
        x, y = path[-1]

        # IMPORTANT:
        # Тут можна легко змінити правила руху або додати перевірки меж.
        if letter == "E":
            path.append((x + 1, y))
        elif letter == "S":
            path.append((x, y + 1))
        elif letter == "W":
            path.append((x - 1, y))
        elif letter == "N":
            path.append((x, y - 1))

    return path


def random_rgba() -> RGBA:
    """
    Випадковий колір для стін.
    Альфа завжди 255 (повністю непрозорий).
    """
    return bytes([randint(0, 255), randint(0, 255), randint(0, 255), 255])


# ============================================================
#               БАЗОВЕ МАЛЮВАННЯ (ПІКСЕЛЬНИЙ РІВЕНЬ)
# ============================================================
def clear_image(image_address: bytearray, rgba: RGBA) -> None:
    """
    Заливає все зображення одним кольором.

    image_address - буфер пікселів (RGBA)
    rgba          - колір заливки
    """
    # len(image_address)//4 = кількість пікселів
    image_address[:] = rgba * (len(image_address) // 4)


def put_cell(
    image_address: bytearray,
    scale: int,
    size_line: int,
    x: int,
    y: int,
    color: RGBA,
) -> None:
    """
    Малює "заповнену клітинку" (квадрат scale x scale) у координатах (x,y).

    Важливо:
    - size_line = кількість БАЙТ в одному рядку пікселів (stride).
    - Один піксель = 4 байти (RGBA).
    - Тому offset_x множимо на 4.

    Якщо хочеш змінити товщину/форму клітинки — редагуй тут.
    """
    offset_x = scale * x * 4               # зміщення по X у байтах
    offset_y = scale * size_line * y       # зміщення по Y у байтах

    # Малюємо scale рядків по вертикалі
    for i in range(scale):
        start = offset_x + offset_y + i * size_line
        end = start + scale * 4
        # color * scale = повторити колір scale разів (scale пікселів)
        image_address[start:end] = color * scale


def draw_cell_walls(
    block_hex: str,
    row_idx: int,
    col_idx: int,
    size_line: int,
    scale: int,
    image_address: bytearray,
    color: RGBA,
) -> None:
    """
    Малює стіни клітинки за hex-кодом (0..F).

    Твоя поточна схема (як у твоєму коді):
    - беремо 4 біти з hex цифри
    - bits[0] = WEST
    - bits[1] = SOUTH
    - bits[2] = EAST
    - bits[3] = NORTH

    Тобто порядок бітів: W S E N

    Якщо ти хочеш інший порядок — заміни розкладку тут:
    west, south, east, north = bits[0], bits[1], bits[2], bits[3]
    """
    numer = int(block_hex, 16)
    bits = format(numer, "04b")  # наприклад: '1010'
    west, south, east, north = bits[0], bits[1], bits[2], bits[3]

    # offset для "верхнього-лівого" пікселя клітинки
    offset_x = scale * col_idx * 4
    offset_y = scale * size_line * row_idx

    # ---------- Верхня стіна (NORTH) ----------
    # Малюємо верхній ряд пікселів клітинки, довжина = scale пікселів.
    if north == "1":
        start = offset_x + offset_y
        end = start + scale * 4
        image_address[start:end] = color * scale

    # ---------- Нижня стіна (SOUTH) ----------
    # Малюємо нижній ряд пікселів клітинки.
    if south == "1":
        start = (scale - 1) * size_line + offset_x + offset_y
        end = start + scale * 4
        image_address[start:end] = color * scale

    # ---------- Ліва/права стіна (WEST/EAST) ----------
    # Малюємо по одному пікселю в кожному рядку клітинки:
    # - WEST: перший піксель рядка
    # - EAST: останній піксель рядка
    for i in range(scale):
        row_start = offset_y + i * size_line + offset_x

        if west == "1":
            image_address[row_start: row_start + 4] = color

        if east == "1":
            east_start = row_start + (scale - 1) * 4
            image_address[east_start: east_start + 4] = color


# ============================================================
#               РЕНДЕР СЦЕНИ (весь кадр)
# ============================================================
def draw_scene(
    mlx: Mlx,
    mlx_ptr,
    window,
    image,
    tab_str: List[str],
    size_line: int,
    scale: int,
    image_address: bytearray,
    start: Coord,
    exit: Coord,
    path: List[Coord],
    show_path: bool,
    wall_color: RGBA,
) -> None:
    """
    Малює повний кадр:
    1) фон
    2) шлях (якщо show_path=True)
    3) старт/фініш
    4) опціонально "особливі клітинки" (у тебе було: якщо block == 'F')
    5) стіни лабіринту

    Якщо хочеш змінити порядок шарів (наприклад стіни поверх шляху) — редагуй тут.
    """
    # ---- КОЛЬОРИ ШАРІВ (легко редагувати тут) ----
    BG = bytes([0, 0, 0, 255])          # фон
    COL_PATH = bytes([0, 255, 255, 255])  # шлях (бірюзовий)
    COL_START = bytes([255, 0, 0, 255])   # старт (червоний)
    COL_EXIT = bytes([0, 255, 0, 255])    # вихід (зелений)
    COL_SPECIAL = bytes([0, 0, 255, 255]) # "F" (синій)

    # 1) Фон
    clear_image(image_address, BG)

    # 2) Шлях (якщо увімкнено)
    if show_path:
        # Якщо хочеш щоб шлях був "тонкою лінією", а не блоками —
        # треба змінити put_cell або зробити окрему функцію.
        for step in path:
            put_cell(image_address, scale, size_line, step[0], step[1], COL_PATH)

    # 3) Старт / Фініш
    put_cell(image_address, scale, size_line, start[0], start[1], COL_START)
    put_cell(image_address, scale, size_line, exit[0], exit[1], COL_EXIT)

    # 4) "Особливі клітинки"
    # УВАГА: tab_str — це список рядків, і кожен символ — hex-цифра.
    # Якщо десь є 'F', то це просто цифра 15, а не "флаг".
    # Якщо тобі 'F' справді означає "спеціальний блок", то це ок.
    for row_idx, row in enumerate(tab_str):
        for col_idx, ch in enumerate(row):
            if ch == "F":
                put_cell(image_address, scale, size_line, col_idx, row_idx, COL_SPECIAL)

    # 5) Стіни
    for row_idx, row in enumerate(tab_str):
        for col_idx, ch in enumerate(row):
            draw_cell_walls(
                ch,
                row_idx,
                col_idx,
                size_line,
                scale,
                image_address,
                wall_color,
            )

    # Виводимо готове зображення у вікно
    mlx.mlx_put_image_to_window(mlx_ptr, window, image, 0, 0)


# ============================================================
#               ОБРОБКА КЛАВІШ
# ============================================================
def handle_key(keycode: int, args: Dict) -> None:
    """
    Обробка клавіатури:
    - ESC (65307): закрити вікно
    - SPACE (32): випадковий колір стін
    - ENTER (65293): показати/сховати шлях

    args — словник зі станом та всіма потрібними параметрами.
    Це зручно, бо MLX callback передає нам тільки keycode і param.
    """
    mlx: Mlx = args["mlx"]
    window = args["window"]
    mlx_ptr = args["mlx_ptr"]

    draw: Callable = args["draw"]         # функція рендера (draw_scene)
    draw_args = args["draw_args"]         # "фіксовані" аргументи рендера

    # ESC: вихід
    if keycode == 65307:
        mlx.mlx_destroy_window(mlx_ptr, window)
        mlx.mlx_loop_exit(mlx_ptr)
        return

    # SPACE: змінюємо колір стін на випадковий
    if keycode == 32:
        args["wall_color"] = random_rgba()
        draw(*draw_args, args["show_path"], args["wall_color"])
        return

    # ENTER: перемикаємо показ шляху
    if keycode == 65293:
        args["show_path"] = not args["show_path"]
        draw(*draw_args, args["show_path"], args["wall_color"])
        return


# ============================================================
#               НАЛАШТУВАННЯ MLX
# ============================================================
def setup_mlx(window_w: int, window_h: int, title: str):
    """
    Ініціалізує MLX, створює вікно.

    Повертає:
    - mlx (об'єкт-обгортка)
    - mlx_ptr (внутрішній pointer)
    - window (вікно)
    """
    mlx = Mlx()
    mlx_ptr = mlx.mlx_init()
    window = mlx.mlx_new_window(mlx_ptr, window_w, window_h, title)
    return mlx, mlx_ptr, window


def create_canvas(mlx: Mlx, mlx_ptr, width: int, height: int):
    """
    Створює image (полотно) і дає доступ до буфера пікселів.

    Повертає:
    - image
    - image_address (bytearray)
    - size_line (stride)
    """
    image = mlx.mlx_new_image(mlx_ptr, width, height)
    (image_address, bpp, size_line, theformat) = mlx.mlx_get_data_addr(image)
    return image, image_address, size_line


# ============================================================
#               MAIN
# ============================================================
def main() -> None:
    # ----------------------------
    # НАЛАШТУВАННЯ ВІКНА / ПОЛОТНА
    # ----------------------------
    WINDOW_W = 1500
    WINDOW_H = 800
    CANVAS_H = 750  # висота image (щоб залишити місце для тексту знизу)
    TITLE = "Natalia"

    # ----------------------------
    # ДАНІ ШЛЯХУ
    # ----------------------------
    path_str = (
        "EESSESSSESEESSSWSWSSWWSSSWSSWWSSESSESESEESESENNNEEEEEEEEENEESEESSSSSENENNEEENWWNNNEENEEESESSSSSSSS"
    )

    # ----------------------------
    # ДАНІ ЛАБІРИНТУ (HEX)
    # ----------------------------
    maze_str = (
        "D53BD15153B95179155115117D3BD3\n"
        "B94056D6946C3C3AC7BEC7EC150416\n"
        "AC7AB9156BD3ABAA93ABB93D692B87\n"
        "C3BC2EEB94542AEC6EAC2EABBAAA87\n"
        "94692D52EB93AC53954101402EAAAB\n"
        "ABD2A97AB86E8556C392AEBA83C2C2\n"
        "843A82D4407941553AEEAD2EE87ED2\n"
        "ED2EEC13BAB87ABBAC792B83D6BD52\n"
        "B96D17EA86C4782A8512EAAC794792\n"
        "C43947B8057B96AC6BAC3C2BBABBEA\n"
        "D12C3B86C3D46BC392AB852A86AABA\n"
        "9681286BB87B96D02A86EB82A96A86\n"
        "E96EAAD004546952EEC3BAEC441447\n"
        "D69142D2EBBBF87EFFFEA83D394397\n"
        "BBA87ABE9282FC5557FB82EBAEBAC3\n"
        "86E83C296AEAFFFBFFFC2EBC07A852\n"
        "8516ED287EBC3BFAFD5107852D2ED2\n"
        "C787B9683947AAFAFFFE8143C7C53A\n"
        "9507AA96C6BD043ABD3BEABE917B82\n"
        "ABC7868155416D684146BA856EB86E\n"
        "82D3C7EC3D3C53BAD4152AAD510417\n"
        "A8501797856D102C57EBC2C112E943\n"
        "E83EEBC52D53EEC79138787AA83C7A\n"
        "96C3BC39055451552EC43C52EEED52\n"
        "EBBC43AAC5157AD3A93B87D45153D2\n"
        "D2C1542ABD07D03A86EAAB9552D6BA\n"
        "D05697C46D6BD6EC057C2AAD3ED142\n"
        "BC152B97B9787BB907D52843C17C7A\n"
        "A92BEA8380141442C13B843ED01792\n"
        "C6C6D46C6EC7ED547EC6C7ED56C56E"
    )

    tab_str = parse_maze(maze_str)

    # Розміри лабіринту
    maze_h = len(tab_str)        # кількість рядків
    maze_w = len(tab_str[0])     # кількість колонок

    # Масштаб клітинки (у пікселях)
    scale = compute_scale(WINDOW_W, CANVAS_H, maze_h, maze_w)

    # ----------------------------
    # MLX INIT
    # ----------------------------
    mlx, mlx_ptr, window = setup_mlx(WINDOW_W, WINDOW_H, TITLE)
    image, image_address, size_line = create_canvas(mlx, mlx_ptr, WINDOW_W, CANVAS_H)

    # ----------------------------
    # СТАРТ / ВИХІД / ШЛЯХ
    # ----------------------------
    start = (1, 1)
    exit = (29, 29)

    # Формуємо список координат шляху
    path = build_path(path_str, start)

    # ----------------------------
    # СТАН (можна змінювати з клавіатури)
    # ----------------------------
    wall_color: RGBA = bytes([255, 255, 255, 255])  # початковий колір стін
    show_path = False                                # чи показувати шлях

    # Перший рендер
    draw_scene(
        mlx,
        mlx_ptr,
        window,
        image,
        tab_str,
        size_line,
        scale,
        image_address,
        start,
        exit,
        path,
        show_path,
        wall_color,
    )

    # ----------------------------
    # ТЕКСТ У ВІКНІ (під полотном)
    # ----------------------------
    mlx.mlx_string_put(mlx_ptr, window, 50, 760, 0xFFFFFFFF, "SPACE: random wall color")
    mlx.mlx_string_put(mlx_ptr, window, 50, 775, 0xFFFFFFFF, "ENTER: toggle path | ESC: exit")

    # ----------------------------
    # ДАНІ ДЛЯ CALLBACK'а КЛАВІШ
    # ----------------------------
    # draw_args — це аргументи, які НЕ змінюються при натисканні клавіш.
    # show_path і wall_color ми додаємо в кінці при виклику draw_scene.
    hook_args = {
        "mlx": mlx,
        "mlx_ptr": mlx_ptr,
        "window": window,
        "draw": draw_scene,
        "wall_color": wall_color,
        "show_path": show_path,
        "draw_args": (
            mlx,
            mlx_ptr,
            window,
            image,
            tab_str,
            size_line,
            scale,
            image_address,
            start,
            exit,
            path,
        ),
    }

    # Встановлюємо хук і запускаємо loop
    mlx.mlx_key_hook(window, handle_key, hook_args)
    mlx.mlx_loop(mlx_ptr)


if __name__ == "__main__":
    main()
