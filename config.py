# 游戏基础配置
PLAYER_COUNT = 6  # 5 AI + 1 真人
HUMAN_SEAT_ID = 4 # 真人固定在 4 号位

# LLM 配置
DASHSCOPE_API_KEY = "key" # 请确保这是有效的 Key
LLM_MODEL = "qwen-plus-2025-01-25"
LLM_API_BASE = "https://dashscope.aliyuncs.com/compatible-mode/v1"

# 游戏参数
PUBLIC_CHAT_ROUNDS = 2  # 公聊轮数

# 初始配置 (如果无男爵)
# 6人局推荐: 3村民, 1外来者, 1爪牙, 1恶魔
SETUP_DISTRIBUTION = {
    "Townsfolk": 3,
    "Outsider": 1,
    "Minion": 1,
    "Demon": 1
}

# 角色数据
ROLES_DATA = {
    "Townsfolk": [
        "洗衣妇", "图书管理员", "调查员", "厨师", "共情者",
        "占卜师", "送葬者", "僧侣", "守鸦人",
        "处女", "杀手", "士兵", "市长"
    ],
    "Outsider": [
        "管家", "酒鬼", "隐士", "圣徒"
    ],
    "Minion": [
        "投毒者", "间谍", "男爵", "红唇女郎"
    ],
    "Demon": [
        "小恶魔"
    ]
}

# 夜晚行动顺序 (唤醒表)
NIGHT_ACTION_ORDER = [
    "投毒者",
    "僧侣",
    "红唇女郎",
    "小恶魔",
    "守鸦人",
    "送葬者",
    "洗衣妇",
    "图书管理员",
    "调查员",
    "厨师",
    "共情者",
    "占卜师",
    "管家", # 管家需要选主人
    "间谍"
]

# 需要在夜晚选择目标的角色 (主动技能)
# 管家也需要选人(主人)
TARGET_REQUIRED_ROLES = [
    "投毒者", "僧侣", "小恶魔", "守鸦人", "占卜师", "管家"
]