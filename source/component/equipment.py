from source import tool
from .. import constants as c
import pygame as pg


class Equipment(pg.sprite.Sprite):
    def __init__(self, name, index, effect, scale=1):
        pg.sprite.Sprite.__init__(self)

        self.name = name
        self.index = index  # 装备索引
        self.effect = effect  # 装备效果描述
        self.frames = []
        self.frame_index = 0
        self.loadImages(name, scale)
        self.frame_num = len(self.frames)
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)

    def loadFrames(self, frames, name, scale=1, color=(0, 0, 0)):
        frame_list = tool.GFX[name]
        for frame in frame_list:
            image = tool.get_image(frame, 0, 0, frame.get_width(), frame.get_height(), color, scale)
            scaled_image = pg.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
            frames.append(scaled_image)

    def loadImages(self, name, scale):
        self.loadFrames(self.frames, name, scale)

    def update(self):
        self.image = self.frames[self.frame_index]
        self.mask = pg.mask.from_surface(self.image)
        self.frame_index = (self.frame_index + 1) % self.frame_num
