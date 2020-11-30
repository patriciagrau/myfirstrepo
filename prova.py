import sys
import argparse


def molasses(hej, lang, mode):
	print(hej, lang, mode)
	pass

def main():
	
	
	sentence = str(list(sys.stdin)[0])
	molasses(sentence[:-1], sys.argv[1], sys.argv[2])
	
	
if __name__ == '__main__':
	main()
