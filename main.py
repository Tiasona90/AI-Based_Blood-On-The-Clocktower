from engine.game_manager import GameManager


def main():
    print("正在启动 AI Blood on the Clocktower (Single Player)...")

    # 实例化游戏管理器
    gm = GameManager()

    # 开始游戏
    try:
        gm.start_game_loop()
    except KeyboardInterrupt:
        print("\n游戏被用户中断。")


if __name__ == "__main__":
    main()