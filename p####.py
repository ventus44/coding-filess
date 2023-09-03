#we import the library qr code 
import qrcode
#we define a function that generates a qr code 
def generate_qrcode(text):
#this variable store the size of the qr code    
    qr = qrcode.QRCode(
        version=1,
#in this line of code it saves at least 7% of our code 
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
#in this line we call the qe add data function
    qr.add_data(text)
#here we make our qr code fit the minimum amount of space possible 
    qr.make(fit=True)
#here we decide the space we want our qr code to occupy
    img = qr.make_image(fill_color="black", back_color="white")
#here we make our code save the image with a specific name
    img.save("qrfile.png")
#we prompt the user to enter a url 
url = input("Enter your url: ")
#here it prints the url 
generate_qrcode(url)

