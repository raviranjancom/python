import random as r
import string

def main():
    def encrypt(data,key,chars):
        r.shuffle(key)
        cypher=""
        for i in range(len(data)):
            index=chars.index(data[i])
            cypher+=key[index]
        return cypher

    def decrypt(data,key,chars):
        cypher=""
        for i in range(0,len(data)):
            index=key.index(data[i])
            cypher+=chars[index]
        return cypher

    print("---------- CYBER ----------")
    running = True
    chars=string.punctuation+string.ascii_lowercase+string.ascii_uppercase+" ";
    chars=list(chars)
    key=chars

    while(running):
        data=input("Enter your data (q to quit): ")
        if(data.lower()=='q'):
            running = False

        print("1. Encrypt")
        print("2. Decrypt")

        option = input("Enter an option : ")

        if(not option.isdigit()):
            print("Enter a valid option!")
        
        else:
            match (int(option)):
                case 1:
                    print(encrypt(data,key,chars))
                case 2:
                    print(decrypt(data,key,chars))

if(__name__=="__main__"):
    main()

