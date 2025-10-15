words=input("enter words separated by spaces:").split()
longest_length= len(max(words,key=len))
print("length of the longest word:",longest_length)
