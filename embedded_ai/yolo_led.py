import cv2
from ultralytics import YOLO
from gpiozero import LED

# =====사용자 설정 =====
CAMERA_INDEX = 0            # USB웹캠 번호
MODEL_PATH = "yolov8n.pt"  # 원본과 동일한 모델 사용
OUTPUT_PIN = 14  # BCMGPIO번호
FRAME_WIDTH = 1280
FRAME_HEIGHT = 720
INFERENCE_SIZE = 160  # 원본과 동일한 추론 입력 크기

# COCO사전 학습 모델 기준:0=사람,73=책
OBJECTS_TO_DETECT = [0, 73]

# True:탐지 결과를 영상 창으로 표시
# False:창 없이 실행하며 GPIO만 제어
SHOW_WINDOW = False

def main()->None:
    cap = None
    output = None
    
    try:
        #GPIO 출력 초기화:처음에는 OFF
        output = LED(OUTPUT_PIN,initial_value=False)
        
        #YOLO모델 로드
        model=YOLO(MODEL_PATH)
        
        #USB웹캠 열기
        cap=cv2.VideoCapture(CAMERA_INDEX)
        
        if not cap.isOpened():
            raise RuntimeError(
                f"웹캠을 열 수 없습니다."
                f"USB 연결과 카메라 번호({CAMERA_INDEX})를 확인하세요."
            )
            
        #객체 탐지 실행
        results = model(
            frame,
            imgsz=INFERENCE_SIZE,
            conf=0.25,
            verbose=False,
        )
        
        #감지된 객체의 클래스 ID가져오기
        boxes=results[0].boxes
        
        if boxes is not None:
            detected_objects =[
                int(class_id)
                for class_id in boxes.cls.cpu().tolist()
            ]
        else:
            detected_objects =[]
            
        #지정한 객체 중 하나라도 감지되었는지 확인
        found_ids =[
            object_id
            for object_id in OBJECTS_TO_DETECT
            if object_id in detected_objects
        ]
        
        object_found = bool(found_ids)
        
        #탐지 결과에 따라 GPIO제어
        if object_found:
            output.on()
        else:
            output.off()
        
        #GPIO상태가 바뀔 때만 메시지 출력
        if object_found != previous_state:
            if object_found:
                print(
                    f"객체 감지:클래스 ID{found_ids}"
                    f"→ GPIO{OUTPUT_PIN}ON"
                )
            else:
                print(
                    f"객체 미감지:클래스 ID{OBJECTS_TO_DETECT}"
                    f"→ GPIO{OUTPUT_PIN}OFF"
                )
            
            previous_state = object_found
            
        if SHOW_WINDOW:
            annotated_frame =results[0].plot()
            cv2.imshow("YOLO USB Webcam", annotated_frame)
            
            #영상 창에서 q키를 누르면 종료
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break