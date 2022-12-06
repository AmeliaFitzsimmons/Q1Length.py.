print("Enter a word, and I will give you the length of the word")
name=input("enter your word:")
lowercase=0
for x in name:
  if x.islower():
    lowercase=lowercase+1
print("The length of your word is:", lowercase)