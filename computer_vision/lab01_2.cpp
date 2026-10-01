#include <iostream>
#include <string>

#include <opencv2/opencv.hpp>

int main(int argc, char** argv) {
    const std::string inputPath = argc > 1
        ? argv[1]
        : "./data/zebra.jpg";

    const cv::Mat original = cv::imread(inputPath, cv::IMREAD_COLOR);
    if (original.empty()) {
        std::cerr << "이미지를 불러올 수 없습니다: " << inputPath << '\n';
        return 1;
    }

    constexpr int screenWidth = 800;
    constexpr int screenHeight = 600;
    const cv::Size screenSize(screenWidth, screenHeight);

    // 컬러 원본을 먼저 800x600으로 표준화합니다.
    cv::Mat standardizedColor;
    cv::resize(original, standardizedColor, screenSize, 0.0, 0.0, cv::INTER_AREA);

    // 배경은 grayscale로 처리한 뒤 BGR로 변환해 컬러 HUD를 그립니다.
    cv::Mat grayscale;
    cv::Mat background;
    cv::cvtColor(standardizedColor, grayscale, cv::COLOR_BGR2GRAY);
    background = grayscale;
    cv::cvtColor(background, background, cv::COLOR_GRAY2BGR);

    // 원본 컬러 영상의 PIP를 우측 하단에 배치합니다.
    const cv::Size pipSize(
        static_cast<int>(screenWidth * 0.3),
        static_cast<int>(screenHeight * 0.3));
    cv::Mat pip;
    cv::resize(standardizedColor, pip, pipSize, 0.0, 0.0, cv::INTER_AREA);

    const int margin = 20;
    const cv::Rect pipRect(
        screenWidth - pip.cols - margin,
        screenHeight - pip.rows - margin,
        pip.cols,
        pip.rows);
    pip.copyTo(background(pipRect));
    cv::rectangle(background, pipRect, cv::Scalar(0, 0, 255), 2, cv::LINE_AA);

    const cv::Point center(screenWidth / 2, screenHeight / 2);
    cv::circle(background, center, 100, cv::Scalar(0, 255, 0), 2, cv::LINE_AA);
    cv::line(background,
             cv::Point(center.x - 130, center.y),
             cv::Point(center.x + 130, center.y),
             cv::Scalar(0, 0, 255), 2, cv::LINE_AA);
    cv::line(background,
             cv::Point(center.x, center.y - 130),
             cv::Point(center.x, center.y + 130),
             cv::Scalar(0, 0, 255), 2, cv::LINE_AA);

    constexpr int fontFace = cv::FONT_HERSHEY_SIMPLEX;
    cv::putText(background, "CCTV-01 [REC]", cv::Point(20, 35),
                fontFace, 0.8, cv::Scalar(0, 0, 255), 2, cv::LINE_AA);
    cv::putText(background, "STATUS: TARGET DETECTED", cv::Point(20, 70),
                fontFace, 0.65, cv::Scalar(255, 255, 255), 2, cv::LINE_AA);

    const std::string outputPath = "cctv_output.jpg";
    if (!cv::imwrite(outputPath, background)) {
        std::cerr << "결과 이미지를 저장할 수 없습니다: " << outputPath << '\n';
        return 1;
    }

    cv::imshow("Original", standardizedColor);
    cv::imshow("CCTV Monitoring", background);
    cv::waitKey(0);
    return 0;
}