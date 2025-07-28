# !usr/bin/env python3
# -*- codiing: utf-8 -*-
from enum import Enum

class Screen(object):

    def __init__(self):
        pass

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be an integer!')
        if value < 0:
            raise ValueError('width must be greater than 0!')
        self._width = value

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('height must be an integer!')
        if value < 0:
            raise ValueError('height must be greater than 0!')
        self._height = value
        
    @property
    def resolution(self):
        return self._width * self._height
    
if __name__ == '__main__':
    sc = Screen()
    sc.width = 1024
    sc.height = 768
    print('resolution =', sc.resolution)
