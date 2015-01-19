all: pack

pack:
	zip --quiet youtube-dl-remote-server youtube_dl_remote_server/*.py
	zip --quiet --junk-paths youtube-dl-remote-server youtube_dl_remote_server/__main__.py
	echo '#!/usr/bin/env python' > youtube-dl-remote-server
	cat youtube-dl-remote-server.zip >> youtube-dl-remote-server
	rm youtube-dl-remote-server.zip
	chmod a+x youtube-dl-remote-server

run: pack
	./youtube-dl-remote-server --verbose

clean:
	rm -f youtube-dl-remote-server