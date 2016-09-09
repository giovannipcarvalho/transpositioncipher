#!/usr/bin/python

'''
Transposition cipher.
Author: Giovanni Paolo
'''

import random
import string
import sys

def cipher(msg, key):
	'''
	Ciphers message using key.
		- key cannot contain repeating characters
		- spaces in message will be trimmed
		- message will be completed with random characters
		so that it can be evenly divided by the key length
	'''
	msg = msg.replace(' ', '')
	while len(msg) % len(key) != 0:
		msg += random.choice(string.uppercase)
	chunks = [msg[i:i+len(key)] for i in xrange(0, len(msg), len(key))]
	order = [''.join(sorted(key)).find(x) for x in key]
	x = map(lambda k: [c for (y,c) in sorted(zip(order, k))], chunks)
	result = [l[i] for i in range(len(key)) for l in x]
	result = ''.join(result)
	return result

def decipher(msg, key):
	'''
	Deciphers message using key.
		- decrypted message may be suffixed by nulls/garbage
		characters
	'''
	order = [key.find(x) for x in sorted(key)]
	chunks = [msg[k+x*len(msg)/len(key)] for k in range(len(msg)/len(key)) for x in range(len(key))]
	chunks = ''.join(chunks)
	chunks = [chunks[i:i+len(key)] for i in xrange(0, len(chunks), len(key))]
	x = map(lambda k: ''.join([c for (y,c) in sorted(zip(order, k))]), chunks)
	return ''.join(x)

if __name__ == '__main__':
	if len(sys.argv) < 4:
		print 'Usage:', sys.argv[0], '[cipher/decipher] <msg> <key>'
	else:
		if sys.argv[1] == 'cipher':
			print cipher(sys.argv[2], sys.argv[3])
		elif sys.argv[1] == 'decipher':
			print decipher(sys.argv[2], sys.argv[3])
		else:
			print 'Invalid command.'
