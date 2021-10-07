import cv2
path = r'F:\University\7TH SEMESTER\FYP - 2\flower.jpg'   #path of image
image = cv2.imread(path)   #read image through path
window_name = 'image'   #the name in which image is displayed
cv2.imshow(window_name, image)   #displaying image using cv2.imshow() method
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Converting color image to grayscale image using builtin cvtcolor() function
cv2.imshow("Converted Image",gray) # Showing the converted image
alpha = 2.5    #Contrast control (1.0-3.0)
beta = 30       # Brightness control (0-100)
adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
cv2.imshow('original', image)
cv2.imshow('adjusted', adjusted)
cv2.waitKey(0)   #waits for user to press any key
cv2.destroyAllWindows()
