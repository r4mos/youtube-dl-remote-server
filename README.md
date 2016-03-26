youtube-dl-remote-server - download videos on your server from some video platforms via http requests using youtube-dl

# USAGE
**youtube-dl-simple-server** [-h] [-v] [-u] [-s SERVER] [-p PORT] [--verbose]

# DESCRIPTION
It is a HTTP server that responds GET requests like:
http://SERVER:49148/URL VIDEO

And start downloading in /home/USER/.config/ydlrs/downloads on your server.

# OPTIONS
	-h, --help            show this help message and exit
	-v, --version         show program's version number and exit
	-u, --update          update or install youtube-dl and exit                        
	-s SERVER, --server SERVER
	                      select server (0.0.0.0 by default)
	-p PORT, --port PORT  select server listening port (49148 by default)
 	--verbose             show what the program is doing


# INSTALLATION
For function only need install the server for your platform, but browser plugin makes it easier download videos

## LINUX SERVER
Download the server an run:

    wget https://github.com/r4mos/youtube-dl-remote-server/raw/master/bin/youtube-dl-remote-server
    chmod +x youtube-dl-remote-server
    ./youtube-dl-remote-server

Files are downloaded to the following directory:

	~/.config/ydlrs/downloads

To uninstall, delete the file youtube-dl-remote-server and the directory ~/.config/ydlrs

## CHROME-CHROMIUM PLUGIN
The plugin was removed from the webstore so only be installed manually.

Init chrome or chromiun with --enable-easy-off-store-extension-install flag.

For example:

	chromium-browser --enable-easy-off-store-extension-install

Then, open the extensions page (chrome://extensions/) and drag and drop [.crx file](https://github.com/r4mos/youtube-dl-simple-server/raw/master/bin/plugin/chrome-chromium/chrome-chromium.crx)

Finally, configure server and port.

# COMPILE
Linux: make

# TODO
- Option to change the download directory

- Option to change the filename to store

- Show the download process

# LINKS
[youtube-dl](https://github.com/rg3/youtube-dl)

[youtube-dl-remote-server](https://github.com/r4mos/youtube-dl-remote-server)

# LICENSE
The MIT License

Copyright (c) 2014 Carlos Ramos Mellado.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
