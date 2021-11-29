import sys
from xor_cipher import XorCipher


def main(argv):
    if(len(argv)!=3):
        print("Arguments: [password] [input_path] [output_path]")
        return

    
    chunk_size=4096
    key=argv[0].encode() 
    decoder=XorCipher(key) 

    with open(argv[1],"rb") as fin:
        with open(argv[2],"w") as fout:

            chunk=fin.read(chunk_size)
            fout.write(decoder.apply(chunk).decode())

            while(len(chunk)==chunk_size):
                chunk=fin.read(chunk_size)
                fout.write(decoder.apply(chunk).decode())

if __name__=="__main__":
    main(sys.argv[1:])