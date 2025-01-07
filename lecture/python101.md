# อธิบายโค้ด Python `.py` ไฟล์

นี่คือ code ทั้งหมด
```python
import argparse

def parse_input():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--name',
        type=str,
        default= 'Tonry',
        help= 'input name of people who are using the app'     
    )
    args = parser.parse_args()
    return args

def printHello(who):
    print(f"Hello world!, {who}!!")
    
if __name__ == "__main__":
    input_v = parse_input()
    print('this is my frist .py file.')
    printHello(input_v.name)

```
## **1. Import Module**
```python
import argparse
```
- โมดูล argparse ใช้สำหรับจัดการ Argument ที่ผู้ใช้ส่งเข้ามาผ่าน Command Line
- ช่วยให้สามารถตั้งค่า Input แบบ Dynamic เช่น การใส่ชื่อผู้ใช้หรือค่าต่าง ๆ ที่ต้องการในขณะรันโปรแกรม

## **2. ฟังก์ชัน parse_input()**
```python
def parse_input():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--name',
        type=str,
        default='Tonry',
        help='input name of people who are using the app'
    )
    args = parser.parse_args()
    return args
```
### **2.1 สร้าง Argument Parser**
- argparse.ArgumentParser() สร้างอ็อบเจ็กต์สำหรับจัดการ Argument
- add_argument เพิ่ม Argument ที่สามารถรับค่าจาก Command Line:
    - --name: รับค่าชื่อจากผู้ใช้ (ชนิด str)
    - default='Tonry': หากผู้ใช้ไม่ใส่ชื่อ ระบบจะใช้ชื่อ Tonry เป็นค่าเริ่มต้น
    - help: คำอธิบายสำหรับ Argument เพื่อแสดงใน Command Line เมื่อใช้ --help
### **2.2 คืนค่า Argument**
- args = parser.parse_args(): รับค่า Argument ที่ส่งมาผ่าน Command Line
- return args: ส่งค่าที่ได้กลับไปใช้งานในโปรแกรม
