from dearpygui.core import *
from dearpygui.simple import *

ver = "0.64g"

def main():
    # set_main_window_size(600, 650)
    set_main_window_resizable(False)
    set_main_window_title(f"Movoda Price Database v{ver}")
    with window("main"):
        add_text("Movoda Price Database")
        add_same_line()
    start_dearpygui(primary_window="main")


if __name__ == "__main__":
    main()