import cv2

camera = cv2.VideoCapture(0, cv2.CAP_V4L2)
ret, image = camera.read()

if ret == True:
    cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Failed to capture image")
    
camera.release()