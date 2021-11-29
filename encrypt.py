import sys
from xor_cipher import XorCipher

def main(argv):
	if len(argv) != 3:
		print("Argument: [password] [input_path] [output_path]")
		return

if __name__ == "__main__":
	main(sys.argv[1:])
