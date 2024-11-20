class REV():
    def method(self, SENTENCE):
        words = SENTENCE.split(' ')
        R = ' '.join(reversed(words))
        return R
    
obj = REV()
n = str(input("Enter any string:"))
print("Entered String is:")
print(n)
print("Reverse of the String(word by word):")
print(obj.method(n))

    
    