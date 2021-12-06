#This script converts a text file that contains ones and zeroes to a proper binary file. 

fin=open("date.out","r")
data=fin.read().strip()

with open("binary.out","wb") as fout:

    for x in range(0,len(data),8):
        chunk=data[x:x+8]
        to_int=int(chunk,2)
        to_bytes=to_int.to_bytes(1,byteorder="big")
        fout.write(to_bytes)

