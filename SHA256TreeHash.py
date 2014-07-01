import hashlib
import os

class SHA256TreeHash:	
	fileSize = 0
	fileName = None
	def __init__(self, filename):
		statinfo = os.stat(filename)
		self.fileSize = statinfo.st_size
		self.fileName = filename
		pass

	def computeSHA256TreeHash(self):
		rawBytes = self.getChunkSHA256Hashes()
		output = rawBytes[:]
		while len(output) > 1:
			outputLength = len(output)
			newOutputLength = outputLength / 2
			if outputLength %2 == 1:
				newOutputLength = newOutputLength + 1
			newOutput = [''] * newOutputLength
			j = 0
			for i in range(0, newOutputLength*2, 2):
				if outputLength - i > 1:
					sha256obj = hashlib.sha256()
					sha256obj.update(output[i])
					sha256obj.update(output[i+1])
					newOutput[j] = sha256obj.digest()
				else:
					newOutput[j] = output[i]
				j = j + 1
			output = newOutput[:]

		return output[0]

	def getChunkSHA256Hashes(self):
		output = []
		numChunks = self.fileSize / (1024*1024)
		if self.fileSize % (1024*1024) > 0:
				numChunks = numChunks + 1
		if numChunks == 0:
			output.append(hashlib.sha256().digest());
		else:
			f = open(self.fileName, 'rb')
			try:
				while 1:
					raw = f.read(1024*1024)
					if raw == '':
						break
					else:
						output.append(hashlib.sha256(raw).digest());
			finally:
				f.close()
		return output

