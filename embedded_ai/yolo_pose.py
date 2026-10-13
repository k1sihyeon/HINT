from ultralytics import YOLO
import cv2

model = YOLO("yolo26n-pose_ncnn_model")

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture image")
        break

    results = model.predict(source=frame, imgsz=640, conf=0.25, verbose=False)
    annotated_frame = results[0].plot()

    cv2.imshow("YOLO Pose Estimation", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
