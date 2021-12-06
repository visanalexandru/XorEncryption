# XorEncrypt

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
