from engine.game_manager import GameManager
from ui.pygame_adapter import PyGameAdapter
import sys
import pygame.scrap


def main():
    gui = PyGameAdapter()
    # 初始化剪贴板模块
    pygame.scrap.init()

    gm = GameManager(io_handler=gui)
    try:
        gm.start_game_loop()
    except KeyboardInterrupt:
        pass
    except SystemExit:
        pass
    except Exception as e:
        print(f"Error: {e}")
        import traceback;
        traceback.print_exc()

    gui.output("游戏结束。")
    while True:
        gui.input("按回车退出...")


if __name__ == "__main__":
    main()