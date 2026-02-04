AI Blood on the Clocktower - Trouble Brewing

Project Overview

This project is a single-player implementation of the social deduction game "Blood on the Clocktower", specifically using the "Trouble Brewing" script. It utilizes Large Language Models (LLM) to drive the logic and dialogue of Non-Player Characters (NPCs), allowing a human player to interact with 5 AI players in a simulated 6-player session. The system includes a rule-based storyteller engine to handle complex game states and interactions.

Key Features

LLM-Driven Gameplay

Integrates OpenAI-compatible APIs (configured for Qwen-plus) to generate realistic dialogue, logic reasoning, and deceptive strategies for AI players. Each AI maintains its own internal state, memory, and personality.

Custom 6-Player Setup

Adapted rules for a 6-player configuration (5 AI + 1 Human). Includes specific logic adjustments for role balance, such as the Baron's ability adding 1 Outsider and removing 1 Townsfolk to fit the player count.

Complete Game Phases

Fully implements the game loop:

Night 0: Initial role distribution and evil team acknowledgement.

Day Phase: Includes private chats (with turn-based restrictions) and public speeches.

Nomination & Voting: Logic for nominations, self-defense speeches, and voting execution.

Night Action: Ability processing for active roles.

Role Mechanics

Implements specific ability logic for roles including:

Slayer: Checks for valid targets and processes kills on the Demon.

Butler: Enforces voting constraints based on the chosen "Master".

Spy: Allows viewing the Grimoire (true roles of all players).

Poisoner/Drunk: AI-generated misinformation logic to mislead players when their information is impaired.

Graphical User Interface

Features a Pygame-based GUI with visualization for:

Seating arrangement and status indicators (dead/alive, voting tokens).

Role display and night information logs.

Scrolling chat history.

Chinese text input support (including clipboard pasting via Ctrl+V).

Project Structure

main_gui.py: The entry point for the graphical version of the game.

config.py: Configuration file for game settings, API keys, and role distributions.

engine/: Contains the core game loop, state management, and role definitions.

ai/: Handles LLM communication, prompt engineering, and strategy templates.

ui/: Manages the Pygame rendering and input handling.

Prerequisites

Python 3.8 or higher

pygame

openai (for API communication)

Setup and Usage

Install the required dependencies:
pip install pygame openai

Configure the API key:
Open 开发中/config.py and set your DASHSCOPE_API_KEY.

Run the game:
python main_gui.py

Disclaimer

This project is a fan-made implementation for educational and research purposes. It is not affiliated with the official Blood on the Clocktower brand or The Pandemonium Institute.

AI 血染钟楼 - 灾祸滋生 (AI Blood on the Clocktower)

项目概述

本项目是社交推理游戏《血染钟楼》（灾祸滋生板子）的单机版实现。项目利用大语言模型（LLM）来驱动 NPC 玩家的逻辑与对话，允许一名真人玩家与 5 名 AI 玩家进行模拟对局。系统内置了基于规则的“说书人”引擎，负责处理复杂的结算流程。

核心功能

LLM 驱动的游戏体验

集成 OpenAI 兼容接口（默认配置为 Qwen-plus），为 AI 玩家生成逼真的对话、逻辑推理及欺诈策略。每个 AI 都有独立的内部状态、记忆和性格。

6 人局定制规则

适配了 6 人局配置（5 AI + 1 真人）。包含特殊的板子平衡调整逻辑，例如男爵在场时自动增加 1 名外来者并减少 1 名村民。

完整的游戏流程

完整实现了游戏循环：

第 0 夜：初始身份分配与邪恶阵营确认。

白天阶段：包含私聊（受轮次限制）和公开发言。

提名与投票：包含提名、自辩发言以及投票结算逻辑。

夜晚行动：处理所有角色的夜晚技能结算。

角色机制实现

实现了复杂的角色技能逻辑，包括：

杀手：判断技能是否发动成功并处决恶魔。

管家：强制执行投票限制（必须跟随主人投票）。

间谍：允许查看魔典（所有玩家的真实身份）。

中毒/酒鬼：通过 AI 生成误导性假信息，干扰玩家判断。

图形用户界面

基于 Pygame 开发的 GUI，支持以下功能：

座位图可视化及状态显示（存活/死亡、投票标记）。

身份显示及夜晚信息日志。

可滚动的聊天记录。

中文输入支持（支持 Ctrl+V 粘贴文本）。

项目结构

main_gui.py: 图形化游戏版本的启动入口。

config.py: 配置文件，包含游戏参数、API 密钥设置及角色分布配置。

engine/: 包含核心游戏循环、状态管理及角色定义。

ai/: 处理 LLM 通信、提示词工程（Prompt Engineering）及策略模板。

ui/: 管理 Pygame 的渲染及输入处理。

环境要求

Python 3.8 或更高版本

pygame

openai (用于 API 通信)

安装与运行

安装依赖库：
pip install pygame openai

配置 API 密钥：
打开 config.py 文件，设置 DASHSCOPE_API_KEY。

启动游戏：
python main_gui.py

免责声明

本项目是用于教育和研究目的的粉丝自制实现，与《血染钟楼》官方品牌或 The Pandemonium Institute 无关联。
