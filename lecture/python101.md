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
