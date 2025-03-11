
# 🌐 Web Service: บริการเชื่อมโยงข้อมูลระหว่างระบบ

Web Service เป็นกลไกสำคัญที่ช่วยให้โปรแกรมหรือระบบต่าง ๆ สามารถสื่อสารและแลกเปลี่ยนข้อมูลกันได้ ไม่ว่าจะเป็นการดึงข้อมูลจากเซิร์ฟเวอร์ การประมวลผล หรือการส่งข้อมูลไปยังระบบอื่น โดยทั่วไป Web Service จะทำงานผ่านโปรโตคอล HTTP และใช้โครงสร้างข้อมูลที่อ่านง่าย เช่น JSON หรือ XML

## 🚀 Web Service ทำงานอย่างไร?
1. **Client** (ผู้ใช้งานหรือโปรแกรมที่ต้องการข้อมูล) ส่งคำขอไปยังเซิร์ฟเวอร์ผ่าน API
2. **Server** รับคำขอ, ดำเนินการ และส่งข้อมูลกลับไปยัง Client
3. **Response** ที่ได้รับอาจเป็นข้อมูลดิบ หรือเป็นโครงสร้างข้อมูลที่ต้องนำไปใช้ต่อ

---

## 📬 Web Service สำหรับส่งข้อความระหว่างผู้ใช้
เราจะสร้าง Web Service ที่ให้ผู้ใช้สามารถส่งข้อความถึงกัน โดยระบบจะแบ่งออกเป็นสองส่วนหลัก ได้แก่:

### 1️⃣ **Client-Side Script** ([`call_web_service.py`](https://github.com/Ratchanontt/AIPrototype24/blob/main/call_web_service.py))
เป็นสคริปต์ที่ช่วยให้ผู้ใช้สามารถป้อนข้อความและเลือกผู้รับข้อความจากรายการที่กำหนดไว้ โดยทำงานตามขั้นตอนต่อไปนี้:
- รับข้อความที่ผู้ใช้ต้องการส่ง
- กำหนดผู้รับและ IP Address
- ส่งข้อมูลไปยัง API ผ่าน HTTP POST

#### 📌 ข้อมูลที่ส่งไปยังเซิร์ฟเวอร์:
- `msg`: ข้อความที่ผู้ใช้ป้อน
- `recipient`: ชื่อของผู้รับ
- `ip`: ที่อยู่ IP ของผู้รับ
- `sender`: ชื่อของผู้ส่ง

#### 🔍 โค้ดตัวอย่าง (Client-Side Script):
```python
import requests
import json

url = 'http://40.81.22.119:5006/simpleAPI'
myobj = {'msg': 'Hello, this is a test message!'}

response = requests.post(url, data=json.dumps(myobj))
print(response.text)
```
---

### 2️⃣ **Server-Side API** ([`firstflask.py`](https://github.com/Ratchanontt/AIPrototype24/blob/main/firstflask.py))
API บนเซิร์ฟเวอร์ที่ทำหน้าที่รับข้อความจากผู้ใช้ บันทึกข้อมูล และตอบกลับไปยัง Client เพื่อยืนยันว่ารับข้อความสำเร็จ

#### 🔍 โค้ดตัวอย่าง (Server-Side API):
```python
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/simpleAPI', methods=['POST'])
def web_service_API():
    payload = request.data.decode("utf-8")
    inmessage = json.loads(payload)
    print("📩 ข้อความที่ได้รับ:", inmessage)
    return jsonify({"status": "Message received!"})

if __name__ == "__main__":
    app.run(debug=True, port=5006)
```

---

## 🌟 REST API Methods ที่ควรรู้
Web Service ส่วนใหญ่ใช้หลักการของ **RESTful API** ซึ่งมีวิธีการสื่อสารที่หลากหลาย เช่น:
| Method  | คำอธิบาย |
|---------|--------------------------------|
| `GET`   | ใช้ดึงข้อมูลจากเซิร์ฟเวอร์ |
| `POST`  | ใช้ส่งข้อมูลไปยังเซิร์ฟเวอร์ |
| `PUT`   | ใช้แก้ไขหรืออัปเดตข้อมูลที่มีอยู่ |
| `DELETE`| ใช้ลบข้อมูลออกจากระบบ |

---

## 🔒 การรักษาความปลอดภัยของ Web Service
เพื่อให้ Web Service ปลอดภัยจากการโจมตีหรือข้อมูลรั่วไหล ควรคำนึงถึง:
- **ใช้ HTTPS** แทน HTTP เพื่อลดความเสี่ยงจากการดักจับข้อมูล
- **เพิ่ม Authentication** เช่น API Key หรือ OAuth2
- **จำกัดการเข้าถึงข้อมูล** โดยกำหนดสิทธิ์ของแต่ละผู้ใช้
- **ป้องกัน SQL Injection และ XSS** ผ่านการกรองข้อมูลที่รับเข้ามา

---

