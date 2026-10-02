from pathlib import Path

import cv2


def main() -> None:
    image_path = Path(__file__).parent / "data" / "lenna.png"
    image = cv2.imread(str(image_path), cv2.IMREAD_COLOR)

    if image is None:
        raise FileNotFoundError(f"이미지를 읽을 수 없습니다: {image_path}")

    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(grayscale, 100, 200)

    cv2.imshow("Grayscale", grayscale)
    cv2.imshow("Canny edges", edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()