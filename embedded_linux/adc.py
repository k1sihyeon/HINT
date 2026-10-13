import time
from smbus2 import SMBus

ADDRESS = 0x48  # I2C address of HW-011 / PCF8591

# 0x40: AIN0 // 주로 외부 입력 또는 가변저항
# 0x41: AIN1 // 주로 광센서 / 조도센서
# 0x42: AIN2 // 주로 온도센서 / 서미스터
# 0x43: AIN3 // 주로 전류센서 / 전류측정 / 가변저항

AIN0 = 0x40

def read_adc(channel):
    with SMBus(1) as bus:
        bus.write_byte(ADDRESS, channel)
        bus.read_byte(ADDRESS)  # Dummy read to initiate conversion
        
        value = bus.read_byte(ADDRESS)
        return value
    
print("Reading ADC values...")

while True:
    # 각 채널의 아날로그 값 0~255 범위로 읽기
    pot_val = read_adc(AIN0)
    
    print(f"Potentiometer Value (AIN0): {pot_val:<4}")
    time.sleep(0.5)