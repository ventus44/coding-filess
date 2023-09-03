#here we define main so we can call our program later
def main():
#here we print a welcome text for our user
    print("welcome to the email slicer")
#this extra line is purely for readability purposes
    print("")
#this is an input prompt that will prompt us to input our email
    email_input = input("input your email adress: ")
#this line split the username and the domain respectivly
    (username, domain) = email_input.split("@")
#this line splits the domain and the extension respecivly 
    (domain, extension) = domain.split(".")
#here we will print the split part that is the username
    print("Username:", username)
#here we print the split domain part 
    print("Domain:", domain)
#here we print the split extension part 
    print("Extension", extension)
#here we call our function main to run our program
main()