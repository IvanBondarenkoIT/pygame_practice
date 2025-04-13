# --- Imports ---
import pygame as pg
from decouple import config


# --- Constants ---
WINDOW_WIDTH = int(config("DEFAULT_WINDOW_WIDTH"))
WINDOW_HEIGHT = int(config("DEFAULT_WINDOW_HEIGHT"))

# --- Classes ---


# --- Functions ---
def main():
    # --- Initialize pg ---
    pg.init()
    print(WINDOW_WIDTH, WINDOW_HEIGHT)
    pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    # --- Main loop ---
    run = True
    while run:
        for event in pg.event.get():
            # 1-й Раздел ----- Обработка событий -----------

            # --- Exit event ---
            if event.type == pg.QUIT:
                run = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP or event.key == pg.K_w:
                    print(f'Движение вверх, клавиша: {pg.key.name(event.key)}')
                if event.key == pg.K_DOWN or event.key == pg.K_s:
                    print(f'Движение вниз, клавиша: {pg.key.name(event.key)}')
                if event.key == pg.K_LEFT or event.key == pg.K_a:
                    print(f'Движение влево, клавиша: {pg.key.name(event.key)}')
                if event.key == pg.K_RIGHT or event.key == pg.K_d:
                    print(f'Движение вправо, клавиша: {pg.key.name(event.key)}')

            # -----------------------------------------------
            if event.type == pg.KEYDOWN:  # Если нажата клавиша
                my_key = event.key
                my_mod = event.mod
                print(f"Button {pg.key.name(my_key)} is pressed")
                print(f"Mod {pg.key.name(my_mod)} is pressed")


            # -----------------------------------------------
            if event.type == pg.MOUSEBUTTONDOWN:  # Если нажата кнопка мыши
                my_pos = event.pos
                my_button = event.button
                print(f"Mouse position: {my_pos}")
                print(f"Mouse button ID: {my_button}")

            # -----------------------------------------------
            if event.type == pg.MOUSEMOTION:  # Если мышь двигается
                my_pos = event.pos
                print(f"Mouse position: {my_pos}")

            # -----------------------------------------------



        # -----------------------------------------------

        # 2-й Раздел ----- Логика игры ------------------
        #
        # -----------------------------------------------

        # 3-й Раздел -----  Отображение графики ---------
        # Очищаем экран
        # Рисуем все объекты на экране
        # Обновление экрана
        # -----------------------------------------------

    # --- Close all modules pg ---
    pg.quit()


# --- Main ---
if __name__ == "__main__":
    main()
