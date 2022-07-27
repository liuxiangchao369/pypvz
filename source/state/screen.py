import pygame as pg
import os
from .. import tool
from .. import constants as c

class Screen(tool.State):
    def __init__(self):
        tool.State.__init__(self)
        self.end_time = 3000

    def startup(self, current_time, persist):
        pass
    
    def getImageName(self):
        pass

    def set_next_state(self):
        pass

    def setupImage(self, name):
        frame_rect = [0, 0, 800, 600]
        self.image = tool.get_image(tool.GFX[name], *frame_rect)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self, surface, current_time, mouse_pos, mouse_click):
        if (current_time - self.start_time) < self.end_time:
            surface.fill(c.WHITE)
            surface.blit(self.image, self.rect)
        else:
            self.done = True

class GameVictoryScreen(Screen):
    def __init__(self):
        Screen.__init__(self)
    
    def getImageName(self):
        return c.GAME_VICTORY_IMAGE
    
    def set_next_state(self):
        return c.LEVEL
    
    def startup(self, current_time, persist):
        self.start_time = current_time
        self.next = c.LEVEL
        self.persist = persist
        self.game_info = persist
        name = self.getImageName()
        self.setupImage(name)
        self.next = self.set_next_state()
        pg.display.set_caption("pypvz: 战斗胜利！")
        # 播放胜利音效
        pg.mixer.Sound(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))) ,"resources", "sound", "win.ogg")).play()

class GameLoseScreen(Screen):
    def __init__(self):
        Screen.__init__(self)
    
    def getImageName(self):
        return c.GAME_LOSE_IMAGE
    
    def set_next_state(self):
        return c.LEVEL
    
    def startup(self, current_time, persist):
        self.start_time = current_time
        self.next = c.LEVEL
        self.persist = persist
        self.game_info = persist
        name = self.getImageName()
        self.setupImage(name)
        self.next = self.set_next_state()
        pg.display.set_caption("pypvz: 战斗失败！")
        # 播放失败音效
        pg.mixer.Sound(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))) ,"resources", "sound", "lose.ogg")).play()
        pg.mixer.Sound(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))) ,"resources", "sound", "scream.ogg")).play()
