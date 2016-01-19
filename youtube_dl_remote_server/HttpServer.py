#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import re
import os
import subprocess
import urllib2
import threading
from Paths import Paths
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn

class HttpServerThread(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

class HttpServerHandler(BaseHTTPRequestHandler):
    def do_GET (self):
        self.send_response(200)
        if (re.match('/http(.+)', self.path)):
            url = re.findall(r'/(.+)', self.path)[0]

            try:
                outputYoutubeDl = subprocess.check_output([Paths().getYdlLocation(), '-g', '--get-filename', '--no-playlist', '--no-playlist', '-f', 'best', '--no-check-certificate', url])
                getVars = outputYoutubeDl.split('\n')

                if len(getVars) > 3: #'URL','Name',''
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write('<h2>Unsupported url</h2>')
                    self.wfile.write('<p>Unexpected response from youtube-dl</p>')

                else:
                    getVars = outputYoutubeDl.split('\n')
                    trueUrl = getVars[0]
                    nameExt = getVars[1]

                    req = urllib2.urlopen(trueUrl)
                    reqLength = req.info().getheader('Content-Length')

                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write('<html>')
                    self.wfile.write('  <head>')
                    self.wfile.write('    <meta http-equiv="Content-type" content="text/html;charset=UTF-8">')
                    self.wfile.write('    <meta charset="UTF-8">')
                    self.wfile.write('    <script language="JavaScript">')
                    self.wfile.write('      setTimeout("history.back()", 3000);')
                    self.wfile.write('    </script>')
                    self.wfile.write('  </head>')
                    self.wfile.write('  <body>')
                    self.wfile.write('    <h2>Downloading ' + nameExt + '</h2>')
                    self.wfile.write('  </body>')
                    self.wfile.write('</html>')

                    fPath = Paths().getYdlDownloadFolder() + '/' + nameExt
                    f = open(fPath + '.part', 'w')

                    while True:
                        chunk = req.read(524288) #512*1024
                        if not chunk:
                            break
                        f.write(chunk)
                    f.close()
                    os.rename(fPath + '.part', fPath)

            except:
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write('<h2>Unsupported url</h2>')
                self.wfile.write('<p>youtube-dl can\'t find video URL</p>')

        else:
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            output  = 'Download videos on your server from some video platforms via http requests using youtube-dl<br /><br />'
            output += 'USAGE:<br />'
            output += 'http://localhost:49148/URL VIDEO<br /><br />'
            output += 'LINKS:<br />'
            output += '<a href="https://github.com/rg3/youtube-dl">youtube-dl</a><br />'
            output += '<a href="https://github.com/r4mos/youtube-dl-remote-server">youtube-dl-remote-server</a>'
            self.wfile.write(output)

        return
