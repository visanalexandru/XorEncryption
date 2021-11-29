import sys
from xor_cipher import XorCipher

def main(argv):
    if len(argv) != 3:
        print("Argument: [password] [input_path] [output_path]")
        return

        chunk_size = 4096
        secret_key = argv[0].encode()
        encoder = XorCipher(secret_key)

        with open(argv[1], "r") as input:
            with open(argv[2], "wb") as output:
                chunk = input.read(chunk_size).encode()
                output.write(encoder.apply(chunk))

                while len(chunk) == chunk_size:
                    chunk = input.read(chunk_size).encode()
                    output.write(encoder.apply(chunk))


if __name__ == "__main__":
    main(sys.argv[1:])
