#!/usr/bin/python
if __name__ == '__main__':
	import sys
	if len(sys.argv) < 2:
		print 'Usage> '+sys.argv[0] + ' filename'
		sys.exit(0)
	from SHA256TreeHash import *
	obj = SHA256TreeHash(sys.argv[1])
	print 'SHA-256 Tree Hash = '+''.join(x.encode('hex') for x in obj.computeSHA256TreeHash())
