# --- Imports ---
import pygame as pg
from decouple import config


# --- Constants ---
WINDOW_WIDTH = config("DEFAULT_WINDOW_WIDTH")
WINDOW_HEIGHT = config("DEFAULT_WINDOW_HEIGHT")

# --- Classes ---


# --- Functions ---
def main():
    # --- Initialize Pygame ---
    pg.init()
    pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    # --- Main loop ---
    run = True
    while run:
        for event in pg.event.get():
            # --- Exit event ---
            if event.type == pg.QUIT:
                run = False
            else:
                pass

    # --- Close all modules Pygame ---
    pg.quit()


# --- Main ---
if __name__ == "__main__":
    main()
