:: ใช้สำหรับ set env variable หลังจากติดตั้ง mosquitto ครั้งแรกเพื่อให้สามารถเรียก mosquitto ผ่าน command prompt ได้
@echo off
setlocal

:: กำหนดเส้นทางที่ต้องการเพิ่ม
set "newPath=C:\Program Files\mosquitto"

:: ตรวจสอบว่าเส้นทางใหม่มีอยู่แล้วใน PATH หรือไม่
echo %PATH% | find /i "%newPath%" >nul
if %ERRORLEVEL% EQU 0 (
    echo The path "%newPath%" is already in the PATH environment variable.
    goto :EOF
)

:: เพิ่มเส้นทางใหม่ไปยัง PATH
setx PATH "%PATH%;%newPath%"

echo Path "%newPath%" has been added to the PATH environment variable.

endlocal

pause