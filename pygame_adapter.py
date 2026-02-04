import pygame
import sys
import math
import time
import os
from engine.game_manager import GameIO
from engine.player_manager import Player

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BG_COLOR = (30, 30, 30)
TEXT_COLOR = (200, 200, 200)
INPUT_BG_COLOR = (50, 50, 50)
PLAYER_RADIUS = 40
SEAT_CENTER = (350, 360)
SEAT_RADIUS = 200


class PyGameAdapter(GameIO):
    def __init__(self):
        pygame.init()
        pygame.key.start_text_input()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("血染钟楼 AI 单机版")
        self.font_path = self._find_chinese_font()

        try:
            self.font = pygame.font.Font(self.font_path, 20)
            self.ui_font = pygame.font.Font(self.font_path, 24)
        except:
            self.font = pygame.font.SysFont(['simhei', 'microsoftyahei'], 22)
            self.ui_font = pygame.font.SysFont(['simhei', 'microsoftyahei'], 26)

        self.logs = []
        self.input_buffer = ""
        self.composition = ""
        self.players = []
        self.running = True

        input_height = 120
        padding = 20
        gap = 15
        log_height = SCREEN_HEIGHT - input_height - 2 * padding - gap
        self.log_area = pygame.Rect(700, padding, 550, log_height)
        self.input_area = pygame.Rect(700, SCREEN_HEIGHT - input_height - padding, 550, input_height)
        pygame.key.set_text_input_rect(self.input_area)

    def _find_chinese_font(self):
        if os.name == 'nt':
            fallbacks = ["C:\\Windows\\Fonts\\simhei.ttf", "C:\\Windows\\Fonts\\msyh.ttc"]
            for f in fallbacks:
                if os.path.exists(f): return f
        return None

    def update_ui(self, players: list):
        self.players = players
        self.render()

    def _wrap_text(self, text, max_width, font):
        lines = []
        current_line = ""
        for char in text:
            test_line = current_line + char
            width, _ = font.size(test_line)
            if width <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = char
        if current_line: lines.append(current_line)
        return lines

    def output(self, text: str):
        raw_lines = text.split('\n')
        wrapped = []
        max_w = self.log_area.width - 20
        for line in raw_lines:
            wrapped.extend(self._wrap_text(line, max_w, self.font))
        self.logs.extend(wrapped)
        if len(self.logs) > 200: self.logs = self.logs[-200:]
        self.render()
        self._pump_events()

    def input(self, prompt: str) -> str:
        self.output(prompt)
        self.input_buffer = ""
        self.composition = ""
        input_active = True

        while input_active and self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False;
                    pygame.quit();
                    sys.exit()

                # Ctrl+V 粘贴
                if event.type == pygame.KEYDOWN and event.key == pygame.K_v and (event.mod & pygame.KMOD_CTRL):
                    try:
                        clip = pygame.scrap.get(pygame.SCRAP_TEXT)
                        if clip:
                            # Pygame 2.0 scrap might return bytes
                            text = clip.decode('utf-8').strip('\x00') if isinstance(clip, bytes) else clip
                            self.input_buffer += text
                    except:
                        pass  # scrap not initialized or error

                if event.type == pygame.TEXTEDITING: self.composition = event.text
                if event.type == pygame.TEXTINPUT: self.input_buffer += event.text; self.composition = ""
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and not self.composition:
                        input_active = False
                    elif event.key == pygame.K_BACKSPACE and not self.composition:
                        self.input_buffer = self.input_buffer[:-1]

            self.render()
            pygame.time.wait(10)

        res = self.input_buffer
        self.input_buffer = ""
        self.output(f"> {res}")
        return res

    def sleep(self, seconds: float):
        end = time.time() + seconds
        while time.time() < end and self.running:
            self._pump_events()
            pygame.time.wait(50)

    def _pump_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: self.running = False; pygame.quit(); sys.exit()

    def render(self):
        if not self.running: return
        self.screen.fill(BG_COLOR)
        self._draw_seats()
        self._draw_logs()
        self._draw_input()
        pygame.display.flip()

    def _draw_seats(self):
        if not self.players: return
        count = len(self.players);
        angle_step = 360 / count
        for i, p in enumerate(self.players):
            angle = -90 + (i * angle_step);
            rad = math.radians(angle)
            x = SEAT_CENTER[0] + SEAT_RADIUS * math.cos(rad)
            y = SEAT_CENTER[1] + SEAT_RADIUS * math.sin(rad)

            color = (100, 255, 100) if p.is_human else ((200, 200, 200) if p.is_alive else (50, 50, 50))
            pygame.draw.circle(self.screen, color, (int(x), int(y)), PLAYER_RADIUS)

            id_surf = self.ui_font.render(f"{p.seat_id}", True, (0, 0, 0))
            id_rect = id_surf.get_rect(center=(int(x), int(y)))
            self.screen.blit(id_surf, id_rect)

            # 显示状态
            status_text = ""
            if p.dead_vote_used and not p.is_alive: status_text += "无票 "
            if p.master_seat_id: status_text += f"主:{p.master_seat_id}"  # 显示管家主人

            if status_text:
                st_surf = self.font.render(status_text, True, (255, 50, 50))
                self.screen.blit(st_surf, (int(x) - 20, int(y) + PLAYER_RADIUS + 5))

            if p.is_human and p.perceived_role:
                role_surf = self.font.render(p.perceived_role, True, (255, 255, 0))
                self.screen.blit(role_surf, (int(x) - 30, int(y) - PLAYER_RADIUS - 25))

    def _draw_logs(self):
        x = self.log_area.left + 5;
        line_h = 28;
        y = self.log_area.bottom - line_h - 5
        for line in reversed(self.logs):
            if y < self.log_area.top: break
            try:
                self.screen.blit(self.font.render(line, True, TEXT_COLOR), (x, y))
            except:
                pass
            y -= line_h
        pygame.draw.rect(self.screen, (100, 100, 100), self.log_area, 1)

    def _draw_input(self):
        pygame.draw.rect(self.screen, INPUT_BG_COLOR, self.input_area)
        pygame.draw.rect(self.screen, (100, 100, 100), self.input_area, 1)
        display_text = self.input_buffer + self.composition + ("|" if time.time() % 1 > 0.5 else "")
        lines = self._wrap_text(display_text, self.input_area.width - 10, self.font)
        max_lines = self.input_area.height // 24
        for i, line in enumerate(lines[-max_lines:]):
            self.screen.blit(self.font.render(line, True, (255, 255, 255)),
                             (self.input_area.x + 5, self.input_area.y + 5 + i * 24))