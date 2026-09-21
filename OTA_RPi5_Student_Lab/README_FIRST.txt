자동차 사이버보안 · OTA Raspberry Pi 5 실습 파일
==================================================

실습 구조
- Windows PC = OEM / OTA Backend 역할
- Raspberry Pi 5 = Vehicle OTA Client + Virtual ECU 역할
- PC와 Raspberry Pi는 동일 Wi-Fi/LAN에서 실제 HTTP 통신을 수행합니다.

폴더 사용 방법
1) PC_SERVER 폴더는 Windows PC에 둡니다.
2) auto_ota_rpi5_lab 폴더 전체를 Raspberry Pi의 /home/student/ 로 복사합니다.
3) Raspberry Pi에서 common/set_server_ip.py를 사용하여 Windows PC의 IPv4 주소를 설정합니다.

Day 2
- Basic HTTP OTA
- 정상 Firmware Update
- Server Repository Firmware Tampering
- 검증 부재로 변조 Firmware가 설치되는 문제 확인

Day 3
- Manifest Digital Signature
- Firmware SHA-256
- Anti-Rollback
- A/B Slot 및 Health Check Recovery

이번 수정본 반영 사항
- Day 2/Day 3 HTTP Server가 요청 대기 중에도 Ctrl+C로 종료되도록 개선
- Windows PowerShell 5.1에서 변조 JSON 저장 시 UTF-8 BOM이 붙지 않도록 수정
- Raspberry Pi 배포 폴더명을 auto_ota_rpi5_lab로 통일

주의
- 본 실습은 교육 목적의 HTTP와 테스트 키를 사용합니다.
- 실제 양산 OTA에서는 HTTPS/TLS, 인증·인가, 키 보호, 보안 Backend, Secure Boot 등 추가 보호기술이 적용됩니다.
- PC_SERVER/day3_secure_ota/keys/oem_private_key.pem은 교육용 테스트 키이며 실제 제품·업무·외부 서비스에 사용하지 마십시오.
