from PyDictionary import PyDictionary
#we pass arguments in the pyctionary that we want the meaning of
dictionary = PyDictionary("eyes", "head", "birth")
  
#here is where the program actually runs and it gets the meanings of the words and print them out
print(dictionary.getMeanings())
