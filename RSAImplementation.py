import math
import random

# A set of collection of prime numbers to select random p and q
primes = set()
n = 0

def gcd(a , b):
    if b == 0:
        return a
    return gcd(b , a%b)

def decrypt(encoded_text):
    d = private_key
    decrypted_text = 1
    while(d):
        decrypted_text *= encoded_text
        decrypted_text %= n
        d-=1
    return decrypted_text

def encrypt(message):
    e = public_key
    encrypted_text = 1
    while(e):
        encrypted_text *= message
        encrypted_text %= n
        e-=1
    return encrypted_text

def prime_fillers():
    sieve = [True]*250
    sieve[0] = sieve[1] = False
    for i in range(2, 251):
        for j in range(2*i, 250, i):
            sieve[j] = False
    for i, elem in enumerate(sieve):
        if(elem):
            primes.add(i)
            
def pickRandomPrimes():
    ret = random.choice(list(primes))
    primes.remove(ret)
    return ret
            
def setKeys():
    global private_key
    global public_key
    
    prime1 = pickRandomPrimes()
    prime2 = pickRandomPrimes()
    
    global n
    n = prime1*prime2
    fi = (prime1-1) * (prime2-1)
    e = 2
    
    while(1):
        if (gcd(e, fi) == 1):
            break
        e+=1
    public_key = e
    
    d = 2
    while(1):
        if((d*e)%fi == 1):
            break
        d +=1
    private_key = d
    return (public_key, private_key)

def encoder(msg):
    form = []
    for letter in msg:
        form.append(encrypt(ord(letter)))
    return form
        

def decoder(encoded_str):
    s = ""
    for num in encoded_str:
        s += chr(decrypt(num))
    return s

def main():
    prime_fillers()
    print('Primes ', primes)
    public_key, private_key = setKeys()
    print("Public key ", public_key)
    print("Private key , ", private_key)
    message = "This is a text message!"
    coded = encoder(message)
    print("Message encoded to : ", coded)
    decoded = decoder(coded)
    print("The decoded message is ", decoded)

if __name__ == "__main__":
    # print("-", gcd(3, 15))
    main()