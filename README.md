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


