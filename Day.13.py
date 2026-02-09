# wap to input a sentence , and print the words in separate lines . 
sentence = str(input("Enter a sentence: "))
words = sentence.split() #here words is a list of words 
for word in words:
    print(word)