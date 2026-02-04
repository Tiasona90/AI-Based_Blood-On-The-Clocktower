class Role:
    def __init__(self, name: str, role_type: str):
        """
        :param name: 角色名称 (e.g., "小恶魔", "洗衣妇")
        :param role_type: 角色类型 ("Townsfolk", "Outsider", "Minion", "Demon")
        """
        self.name = name
        self.role_type = role_type

        # 确定阵营 (汉化)
        if role_type in ["Townsfolk", "Outsider"]:
            self.alignment = "善良"
        else:
            self.alignment = "邪恶"

    def on_night(self, game_state, player):
        """夜晚行动逻辑"""
        pass

    def on_day(self, game_state, player):
        """白天被动技能"""
        pass

    def __str__(self):
        return f"{self.name} ({self.alignment})"