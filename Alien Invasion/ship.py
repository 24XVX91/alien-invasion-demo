import pygame
from pygame.sprite import Sprite

class Ship:
    """管理飞船类"""

    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #  加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #  每艘新飞船都放在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom

        #  在飞船的属性X,Y中存储一个浮点数
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #  移动标志(飞船一开始不移动)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船位置"""
        #  更新飞船而不是rect对象的x值
        if self.moving_right and self.rect.right < self.screen_rect.right:  # 判断右边是否到达临界
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:  # 判断左边是否到达临界
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:   # 判断是否到达顶部
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:   # 判断是否到达底部
            self.y += self.settings.ship_speed

        #  根据self.x 和self.y 更新rect对象
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """指定绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """将飞船放在屏幕底部的中央"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)