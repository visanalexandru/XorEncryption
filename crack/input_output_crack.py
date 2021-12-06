a=open("date.in","r")
b=open("binary.out","rb")

#The maximum length of the key is 20, so read only 20 characters from each file.
chunk_size=20

chunk_a=a.read(chunk_size).encode() #encode to binary
chunk_b=b.read(chunk_size) #already binary

#Xor the input with the output
xored=[chr(x[0]^x[1]) for x in zip(chunk_a,chunk_b)]

print(*xored)


