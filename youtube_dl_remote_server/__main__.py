#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import sys

if __package__ is None and not hasattr(sys, "frozen"):
	print "Run __init__.py"
	sys.exit(0)

import youtube_dl_remote_server

if __name__ == '__main__':
    youtube_dl_remote_server.main()