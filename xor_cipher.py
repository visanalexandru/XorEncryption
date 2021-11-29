#This class implements a basic xor cipher. Given a key, we can generate the cyphertext by applying  
#the XOR operation to every byte in the input with the corresponding byte in the key, as the key
#is repeating.

#For example, let's say the input text is "LINUX" and the key is "GNU". 
#The result of the operation will be L^G , I^N , N^U , U^G , X^N

class XorCipher: 
    #We need a key in bytes
    def __init__(self,key):

        if not isinstance(key,bytes): #Throw an error if we didn't receive a "bytes" object
            raise TypeError(f"Expected bytes, got "+type(key).__name__) 

        self.key=key
        self.key_length=len(key)


    #Apply the key to a bytes object and return the result
    def apply(self,data):

        if not isinstance(data,bytes):
            raise TypeError(f"Expected bytes, got "+type(data).__name__) 

        result=[]

        for x in enumerate(data):
            #Get the corresponding byte in the key, as the key is repeating. 
            key_index=x[0] % self.key_length
            key_byte=self.key[key_index]

            data_byte=x[1] 
            result.append(data_byte^key_byte)

        return bytes(result)



