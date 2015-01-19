#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import os

class Paths():
    _ydlname = ''
    _ydlpath = ''
    _ydllocation = ''
    _ydlDownloadFolder = ''

    def __init__(self):
        self._ydlname = 'youtube-dl'
        self._ydlpath = os.path.expanduser('~') + '/.config/ydlrs'
        self._ydllocation = self._ydlpath + '/' + self._ydlname
        self._ydlDownloadFolder = self._ydlpath + '/' + 'downloads'

    def getYdlName(self):
        return self._ydlname

    def getYdlPath(self):
        return self._ydlpath

    def getYdlLocation(self):
        return self._ydllocation

    def getYdlDownloadFolder(self):
        return self._ydlDownloadFolder