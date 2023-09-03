#this library is being imported to fetch urls
import urllib.request as urllib

#this function takes one argument the url
def main(url):
    print("checking connectivity")
#this line takes the input of the url and it returns the response object
    response = urllib.urlopen(url)
#this line is printed after you succesfully connect to the url
    print("Connected to", url, "succesfully")
#this prints and http code that says if the connection was succesfull
    print("The response code was:", response.getcode())

#this line explains what the program does
print("This is a site conectivly checker program")
#this line takes the url that the user wants to input 
input_url = input("Input the url of the site you want to check: ")
#here we call our function main 
main(input_url)

