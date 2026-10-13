from ultralytics import YOLO
import cv2

CAMERA_INDEX = 0
MODEL_PATH = "yolo26n.pt"
FRAME_WIDTH = 1280
FRAME_HEIGHT = 720
FPS = 30
INFERENCE_SIZE = 640

# model = YOLO(MODEL_PATH)
camera = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_V4L2)

model = YOLO("yolo26n_ncnn_model")

try:
    if not camera.isOpened():
        raise Exception("cannot open camera")
    
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)
    camera.set(cv2.CAP_PROP_FPS, FPS)
    camera.set(cv2.CAP_PROP_BUFFERSIZE, 1)  # Set buffer size to 1 for low latency
    
    actual_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
    actual_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
    actual_fps = int(camera.get(cv2.CAP_PROP_FPS))
    print(f"Camera opened: {actual_width}x{actual_height} @ {actual_fps} FPS")
    
    while True:
        ret, image = camera.read()

        if not ret:
            print("Failed to capture image")
            break

        results = model.predict(source=image, imgsz=INFERENCE_SIZE, conf=0.25, verbose=False)
        annotated = results[0].plot()  

        cv2.imshow("YOLO", annotated)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
except Exception as e:    
    print(f"Error opening camera: {e}")

except KeyboardInterrupt:
    print("Keyboard interrupt received. Exiting...")
    
finally:
    camera.release()
    cv2.destroyAllWindows()