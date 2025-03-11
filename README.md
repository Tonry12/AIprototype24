# 🤖 AIPrototype24 - 2024 
## Prototyping for AI & Machine Learning Systems
SC664401 | การสร้างต้นแบบระบบปัญญาประดิษฐ์และการเรียนรู้ของเครื่อง

👨🏻‍🎓 **Thanabodi Puchomsi** 📝  
📌 **Student ID:** 643020502-4

---

## 📅 ตารางเรียน
| ครั้งที่ | วันที่       | หัวข้อบทเรียน           | ลิงก์บันทึกการสอน |
|:-------:|:----------:|:-------------------:|:-------------------:|
| I       | 02/12/67  | คำสั่ง Ubuntu CLI   | [`คำสั่ง Ubuntu_พื้นฐาน.md`](https://github.com/Tonry12/AIprototype24/blob/main/LinuxCommandLine(%E0%B8%9A%E0%B8%99%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%87).md) |
| II      | 11/12/67  | เครื่องเสมือน (VM) | [`Lecture Class II.md`](https://github.com/Ratchanontt/AIPrototype24/blob/main/Lecture%20Class%20II.md) |
| III     | 24/12/67  | Cloud VM           | [`Lecture Class III.md`](https://github.com/Ratchanontt/AIPrototype24/blob/main/Lecture%20Class%20III.md) |
| IV      | 07/01/68  | การสร้างเว็บ        | [`Lecture Class IV.md`](https://github.com/Ratchanontt/AIPrototype24/blob/main/Lecture%20Class%20IV.md) |
| V       | 21/01/68  | สภาพแวดล้อม Conda | [`Lecture Class V.md`](https://github.com/Ratchanontt/AIPrototype24/blob/main/Lecture%20Class%20V.md) |
| VI      | 19/02/68  | Web Service        | [`Lecture Class VI.md`](https://github.com/Ratchanontt/AIPrototype24/blob/main/Lecture%20Class%20VI.md) |
| VII     | 11/03/68  | Deep Learning      | [`Lecture Class VII.md`](https://github.com/Ratchanontt/AIPrototype24/blob/main/Lecture%20Class%20VII.md) |

---

## 📂 **เนื้อหาเรียน**
<details>
  <summary>Ubuntu บน Windows (WSL)</summary>

### 🔧 คำสั่งพื้นฐานบน Terminal
- **ดูตำแหน่งปัจจุบัน** → `pwd`
- **แสดงไฟล์ทั้งหมด** → `ls -l`
- **สร้างโฟลเดอร์ใหม่** → `mkdir [ชื่อโฟลเดอร์]`
- **เปลี่ยนไดเร็กทอรี** → `cd [ชื่อโฟลเดอร์]` | `cd ..` (ถอยหลัง)
- **สร้างไฟล์ใหม่** → `vi [ชื่อไฟล์]`
- **คัดลอกไฟล์** → `cp [ไฟล์ต้นฉบับ] [ปลายทาง]`
- **ย้ายไฟล์** → `mv [ไฟล์ต้นทาง] [ปลายทาง]`
- **ลบไฟล์หรือโฟลเดอร์** → `rm -r [ชื่อไฟล์/โฟลเดอร์]`
- **ตรวจสอบทรัพยากรระบบ** → `htop`
</details>

<details>
  <summary>เครื่องเสมือน (Virtual Machines)</summary>

### 🖥️ ใช้งาน Server ผ่าน SSH
- **เข้าสู่เซิร์ฟเวอร์** → `ssh [username]@[IP address]`
- **เพิ่มผู้ใช้ใหม่** → `sudo adduser [username]`
- **ดูการทำงานของเซิร์ฟเวอร์** → `htop`
- **เพิ่มสิทธิ์ sudo ให้ผู้ใช้** → `sudo adduser [username] sudo`
</details>

<details>
  <summary>Cloud VM</summary>

### ☁️ การสร้างและจัดการ VM บน Cloud
- **สร้าง VM** ผ่าน Azure Portal
- **เข้าสู่เซิร์ฟเวอร์ผ่าน SSH** → `ssh [username]@[IP]`
- **ออกจากระบบ** → `exit`
- **คัดลอกไฟล์ไปยัง Cloud** → `scp [ไฟล์ต้นทาง] [user]@[IP]:[ตำแหน่งปลายทาง]`
- **ดึงไฟล์จาก Cloud** → `scp [user]@[IP]:[ตำแหน่งต้นทาง] [ปลายทาง]`
</details>

<details>
  <summary>Web Development</summary>

### 🌐 ประเภทของเว็บ
1. **Static Web** – เว็บแสดงข้อมูลคงที่ (HTML, CSS)
2. **Dynamic Web** – เว็บโต้ตอบได้ ใช้ฐานข้อมูล (PHP, Python, Node.js)
3. **Web Application** – เว็บที่รองรับฟังก์ชันต่างๆ
4. **Web Service** – API ที่ให้โปรแกรมอื่นเข้าถึงข้อมูล

### 🛠️ เทคโนโลยีเว็บที่เกี่ยวข้อง
- **HTML** – สร้างโครงสร้างเว็บ
- **CSS** – ปรับแต่งดีไซน์
- **JavaScript** – เพิ่มลูกเล่นให้เว็บ
- **Python (Flask)** – ใช้พัฒนา Back-End
</details>

<details>
  <summary>Deep Learning</summary>

### 🧠 การเรียนรู้เชิงลึก (Deep Learning)
- **โครงข่ายประสาทเทียม (Neural Networks)**
- **การฝึกโมเดลด้วย TensorFlow/PyTorch**
- **การใช้ GPU/TPU ในการเร่งประสิทธิภาพ**
</details>

---

## 🎯 **การบ้าน**
<details>
  <summary>📌 HW1: คำนวณจำนวนวันที่มีชีวิตอยู่</summary>
👉 คำนวณวันเกิดและแสดงเวลาถึงวันเกิดถัดไป

[`myfirstpy.py`](https://github.com/Ratchanontt/AIPrototype24/blob/main/myfirstpy.py)
</details>

<details>
  <summary>📌 HW2: ส่งข้อความหาเพื่อนผ่านเซิร์ฟเวอร์</summary>
👉 ระบบส่งข้อความผ่าน API ไปยัง IP Address ที่บันทึกไว้

[`call_web_service.py`](https://github.com/Ratchanontt/AIPrototype24/blob/main/call_web_service.py)
</details>
