from PIL import Image
#in this function that presents the length and the width that the image 
def resize_image(size1, size2):
#using this the image is being opened using the pl function
    image = Image.open(r"C:\Users\Thanos\Desktop\coding files\face_rec\test.JPG")
#the current size of the image i printed here 
    print(f"Current size: {image.size}")
#here the image is reisized 
    resized_image = image.resize((size1, size2))
#the resized image now is been saved using the save method 
    resized_image.save(r"C:\Users\Thanos\Desktop\coding files\face_rec\test" + str(size1) + ".JPG")
#in this line the size1 and 2 ar inputed by the user and converted to integers 
size1 = int(input("Enter length: "))
size2 = int(input("Enter width: "))
#finally the resized function is called with the input size 1 and 2 from the user
resize_image(size1, size2)
