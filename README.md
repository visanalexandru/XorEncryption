# XorEncryption

This python project is a simple implementation of the xor encryption method. 


## Usage
  File encryption:
  ``` python3 encrypt.py [password] [input_path] [output_path] ```  
  Encrypting a file will require a password, which is then applied to the input to generate a binary file.
  
  File decryption:
  ``` python3 decrypt.py [password] [input_path] [output_path] ```  
  Decrypting a file will require a password, which is then applied to a binary file to generate a text file. Without the correct password, the output will not
  be correct.

## Cracking
  Team name: **CSV**  
  Opponent team name: **RAR2002**  
  Opponent team repository: https://github.com/aberbecaru/RAR2002
  
  All the code used in this section is available in the [crack](crack) folder
  ### 1. Converting the cyphertext into a proper binary file
  The opponent team did not provide a proper binary file, but a [text file](https://github.com/aberbecaru/RAR2002/blob/master/date.out) which contains a string of ones and zeroes. We need to convert this text file into a proper binary file to be able to crack it.  
  The following [script](crack/get_data.py) was used to get the binary file:  
  ```python
  #This script converts a text file that contains ones and zeroes to a proper binary file. 

fin=open("date.out","r")
data=fin.read().strip()

with open("binary.out","wb") as fout:

    for x in range(0,len(data),8):
        chunk=data[x:x+8]
        to_int=int(chunk,2)
        to_bytes=to_int.to_bytes(1,byteorder="big")
        fout.write(to_bytes)

```
Now that we have the [binary file](crack/binary.out) we can continue with our crack.

### 2. Cracking the key using the input text file and the output binary file
If we have access to both the [input text file](https://github.com/aberbecaru/RAR2002/blob/master/date.in) and the [output binary file](crack/binary.out) we can use the self-inverse property of the XOR operation to find the key.  
Let's denote the input with A, the key with K, and the output with B.

B = A ⊕ K  
A ⊕ A = 0  
A ⊕ B = A ⊕ A ⊕ K = 0 ⊕ K = K  

Therefore, we can find the key by computing the XOR of A and B.  
This [script](crack/input_output_crack.py) does exactly that:

```python
a=open("date.in","r")
b=open("binary.out","rb")

#The maximum length of the key is 20, so read only 20 characters from each file.
chunk_size=20

chunk_a=a.read(chunk_size).encode() #encode to binary
chunk_b=b.read(chunk_size) #already binary

#Xor the input with the output
xored=[chr(x[0]^x[1]) for x in zip(chunk_a,chunk_b)]

print(*xored)
```

Executing the script gives us the following output: ```A 3 q t R y 7 8 K L o a 1 9 A 3 q t R y```.  
Therefore we can conclude that the key is ```A3qtRy78KLoa19```


### 3. Cracking the key using only the output binary file
Through analysis we have concluded that the most frequent characters used in a file that contains romainian text are:  
- the space character (**32** in ASCII),
- the letter "a" (**97** in ASCII)
- the letter "i" (**105** in ASCII)
- the letter "e" (**101** in ASCII)

We know that the key length is between 10 and 15 characters. We start by guessing the key length, let us denote it "L".

For every position X in the key, we will look at the bytes in the binary file that we know are the result of the XOR operation between the corresponding character in the input file and the X-th character of the key.  

That is, we will examine the bytes at indicies congruent to X (**modulo L**). We will analyse the frequency of each such symbol.  

We can assume that the most frequent symbol is the result of the XOR operation between one of the characters above and the X-th character of the key.   Therefore, we can find the X-th character of the key by "XOR-ing" together the most frequent symbol and one of the characters above.

The following [script](crack/output_crack.py) implements the algorithm we just described.
```python
input = open("binary.out", "rb")

def bun(x):
    return (x >= ord('0') and x <= ord('9')) or (x >= ord('a') and x <= ord('z')) or (x >= ord('A') and x <= ord('Z'))

def alege(x):
    if bun(x^ord(' ')):
        return (x^ord(' '))
    if bun(x^ord('a')):
        return (x^ord('a'))
    if bun(x ^ ord('i')):
        return (x ^ ord('i'))
    return (x ^ ord('e'))

for key_len in range(10, 16):
    input.seek(0)
    index = 0
    frq = [{} for _ in range(0, key_len)]
    byte = input.read(1)
    while byte:
        if byte not in frq[index]:
            frq[index][byte] = 1
        else:
            frq[index][byte] += 1
        index += 1
        index %= key_len
        byte = input.read(1)

    lst = []
    for i in range(0, key_len):
        acm = [(x, frq[i][x]) for x in frq[i]]
        acm = sorted(acm, key=(lambda x:-x[1]))
        lst.append(alege(int.from_bytes(acm[0][0], 'little')))

    acm = ""
    for x in lst:
        acm += chr(x)

    print(acm)

```

