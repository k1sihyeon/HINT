#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;

int main(int argc, char** argv)
{
    cv::Mat img = cv::imread("C:\\dev\\opencv\\sources\\samples\\data\\lena.jpg", cv::IMREAD_COLOR);
    if (img.empty()) {
        cout << "Could not read the image" << endl;
        return 1;
    }
    cv::imshow("Display window", img);
    int k = cv::waitKey(0);
    if (k == 's') {
        cv::imwrite("C:\\dev\\opencv\\sources\\samples\\data\\lena_copy.png", img);
    }
    return 0;
}