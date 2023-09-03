#we define a function called replace word
def replace_word():
#we make a string that has a phrase in it
    str = "hi, i'm Thanos, hi hi hi"
#we create an input varibale that prompts us to input the word we want to replace     
    word_to_replace = input("Enter the word to replace: ")
#we create an input variable that prompts us to input the word replacement
    word_replacement = input("Enter the word replacement: ")
#we are now going to print the str with the new words in it
    print(str.replace(word_to_replace, word_replacement))
#now we will call the function
replace_word()