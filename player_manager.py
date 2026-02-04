from engine.roles.base_role import Role


class Player:
    def __init__(self, seat_id: int, is_human: bool = False):
        self.seat_id = seat_id
        self.is_human = is_human

        # 身份相关
        self.true_role: Role = None
        self.perceived_role: str = ""
        self.bluff_role: str = ""
        self.alignment: str = ""

        # AI 状态
        self.personality = "理智且谨慎"
        self.ai_thought_log = []
        self.known_teammates = []
        self.demon_bluffs = []
        self.initial_strategy = {}

        # 状态与信息缓冲
        self.night_messages = []
        self.pending_death = False

        # 特殊状态
        self.master_seat_id = None  # 管家的主人
        self.has_voted_this_round = False  # 本轮投票是否已举手

        # 社交记忆
        self.known_claims = {}
        self.private_chat_history = {}

        # 状态标记
        self.is_alive = True
        self.is_drunk = False
        self.is_poisoned = False
        self.is_protected = False
        self.is_demon_target = False

        self.has_voted = False  # 死人票标记 (整局游戏)
        self.has_nominated = False  # 每日是否已提名
        self.dead_vote_used = False  # 真正记录死人票是否用过

    def assign_role(self, role: Role):
        self.true_role = role
        self.alignment = role.alignment
        self.perceived_role = role.name
        self.bluff_role = role.name

    def add_thought(self, thought: str):
        self.ai_thought_log.append(f"Day {len(self.ai_thought_log)}: {thought}")

    def add_chat_record(self, target_id: int, message: str, is_me: bool):
        if target_id not in self.private_chat_history:
            self.private_chat_history[target_id] = []
        sender = "我" if is_me else f"{target_id}号"
        self.private_chat_history[target_id].append(f"{sender}: {message}")

    def kill(self):
        if self.is_alive:
            self.is_alive = False
            return True
        return False

    def reset_night_status(self):
        self.is_poisoned = False
        self.is_protected = False
        self.is_demon_target = False
        self.night_messages = []
        # master_seat_id 不重置，管家每晚选新的会覆盖，死后可能保留

    def __repr__(self):
        status = "存活" if self.is_alive else "死亡"
        human_tag = "[真人]" if self.is_human else "[AI]"
        role_show = self.true_role.name if self.true_role else "未知"
        state_mark = ""
        if self.is_poisoned: state_mark += "[毒]"
        if self.is_protected: state_mark += "[盾]"
        if self.is_drunk: state_mark += "[酒]"
        return f"{self.seat_id}号{human_tag} {role_show}{state_mark} ({status})"