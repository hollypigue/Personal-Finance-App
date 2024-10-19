from common import Label, Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.graphics import Color, RoundedRectangle

class RoundedButton(ButtonBehavior, Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (200, 50)
        self.bind(pos=self.update_rect, size=self.update_rect)
        with self.canvas.before:
            Color(0.2, 0.6, 0.2, 0.6)  # Button color
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[30])  # Adjust radius to make it more rounded

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
