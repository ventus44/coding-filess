import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier(r"C:\Users\Thanos\Downloads\haarcascade_frontalface_default.xml")

# Open the video file
cap = cv2.VideoCapture(r"C:\Users\Thanos\Desktop\coding files\face_rec\test.MOV")

while True:
    # Read the frame
    ret, img = cap.read()

    # If frame not successfully read, break loop
    if not ret:
        break

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # Resize the image
    img = cv2.resize(img, (800, 600))  # Adjust the size as needed

    # Display
    cv2.imshow('img', img)

    # Stop if escape key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
