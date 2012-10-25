#!/usr/bin/env python
import time
import urllib2
from pacmanprogressbar import Pacman



if __name__ == "__main__":

	url="http://www.jesusroldan.com/Alberto%20Laiseca%20-%20Cuentos%20de%20Terror.tar.gz"

	file_name = url.split('/')[-1]
	u = urllib2.urlopen(url)
	f = open(file_name, 'wb')
	meta = u.info()
	file_size = int(meta.getheaders("Content-Length")[0])
	p = Pacman(end=file_size, text="Downloading")
	file_size_dl = 0
	block_sz = 8192
	while True:
	    buffer = u.read(block_sz)
	    if not buffer:
	        break
	    file_size_dl += len(buffer)
	    f.write(buffer)
	    p.progress(value=file_size_dl)
	f.close()       
	print("Finished")
