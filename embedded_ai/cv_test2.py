import cv2

camera = cv2.VideoCapture(0, cv2.CAP_V4L2)

camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
camera.set(cv2.CAP_PROP_FPS, 30)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi', fourcc, 30.0, (640, 480))

while True:
    ret, image = camera.read()
    
    if ret:
        cv2.imshow("image", image)
        out.write(image)
        
    else:
        print("Failed to capture image")
        break
    
    if cv2.waitKey(1) == 27:
        break
    
camera.release()
out.release()
cv2.destroyAllWindows()