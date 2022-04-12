# Eric Liu

##Helpful Functions
#chr(ASCIICODE) --> character
#ord(CHARACTER) --> ASCII value

def encrypt(message,key):
    encrypted=""
    message = message.upper()
    key = key.upper()
    i = 0
    while (i<len(message)): #iterating through the message
        iKey = i%len(key) #index of key string
        #getting each letter's ASCII and converting to 0-25
        p = ord(message[i])-65 #ord to convert chr to ascii, 65 due to A's ascii code
        d = ord(key[iKey])-65

        #vigenere encryption formula per char: C = (P+d)%26
        #adding by d in order to move that many steps ahead
        c = chr(((p+d)%26)+65) #add 65 again to get to letters in ascii code
        encrypted+=c
        i+=1
    return encrypted

def decrypt(secret,key):
    decrypted = "" #an empty string to build on
    #make all of your cases upper for both secret and key
    #use a while loop to iterate through message and key
    #convert both the encrypted char and the key into ASCII codes
    #use the decryption formula of P = (c-d)%26
    #convert the decrypted ASCII into a character
    #concatenate on to the decrypted subtracting
    message = secret.upper()
    key = key.upper()
    i = 0
    while (i<len(message)): #iterating through the message
        iKey = i%len(key) #index of key string
        #getting each letter's ASCII and converting to 0-25
        c = ord(message[i])-65 #ord to convert chr to ascii, 65 due to A's ascii code
        d = ord(key[iKey])-65

        p = chr(((c-d)%26) + 65) #add 65 again to get to letters in ascii code
        decrypted += p
        i+=1   

    return decrypted

m = "computerscience"
k = "bcd"

#Use this resource to check your work: https://www.dcode.fr/vigenere-cipher

encrypted = encrypt(m,k)
decrypted = decrypt(encrypted,k)

print("Encrypted:", encrypted)
print("key:", k)
print("Decrypted:", decrypted)
