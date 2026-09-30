import cv2

# 웹캠에서 비디오 캡처 객체를 생성합니다.
cap = cv2.VideoCapture('http://127.0.0.1:5000/video')

# 비디오 스트림을 반복적으로 처리합니다.
while True:
    # 현재 프레임을 캡처합니다.
    ret, frame = cap.read()

    # 프레임이 제대로 캡처되었는지 확인합니다.
    if not ret:
        print("Failed to grab frame")
        break

    # 캡처된 프레임을 윈도우에 표시합니다.
    cv2.imshow('Webcam Stream', frame)

    # 'q' 키를 누르면 반복문에서 빠져나옵니다.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 사용이 끝난 자원을 해제합니다.
cap.release()
cv2.destroyAllWindows()