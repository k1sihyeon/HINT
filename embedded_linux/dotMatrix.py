import time
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

# 1. init
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=1, block_orientation=0, rotate=2)

print("Matrix test started")

# 밝기 조절 0~255
device.contrast(30)

try:
    # 예제1: 간단한 텍스트 스크롤
    show_message(device, "Hello World!", fill="white", font=proportional(CP437_FONT), scroll_delay=0.05)
    time.sleep(1)
    
    # 예제2: 캔버스에 직접 픽셀
    with canvas(device) as draw:
        heart = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]
        
        for y, row in enumerate(heart):
            for x, pixel in enumerate(row):
                if pixel == 1:
                    draw.point((x, y), fill="white")
                
    print("Heart shape displayed")
    time.sleep(3)
    
except KeyboardInterrupt:
    print("Matrix test interrupted")
    
finally:
    device.clear()
    print("Matrix test finished")