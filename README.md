# AIprototype24
AI Prototyping 2024 Thanabodi Phuchomsi
# 🦾🤖 AIPrototype24 🦿
SC664401 Prototyping for Artificial Intelligence and Machine Learning System 
การสร้างต้นแบบสําหรับระบบปัญญาประดิษฐ์และการเรียนรู้ของเครื่อง


👨🏻‍🎓📚 รัชชานนท์ ทิพย์พิมานพร Ratchanont Thippimanporn ID: 643020515-5 📝

# 🗓️ Calender
|  CLASS  |    DATE    |      DESCRIPTION      |             LECTURE             | 
|:-------:|:----------:|:---------------------:|:-------------------------------:|
|   I     |  02/12/67  | Ubuntu Command Line   | [`Lecture Class I.md`](https://github.com/Ratchanontt/AIPrototype24/blob/main/Lecture%20Class%20I.md)  |
|   II    |  11/12/67  | Virtual Machines      | [`Lecture Class II.md`](https://github.com/Ratchanontt/AIPrototype24/blob/main/Lecture%20Class%20II.md) |
|   III   |  24/12/67  | CloudVM               | [`Lecture Class III.md`](https://github.com/Ratchanontt/AIPrototype24/blob/main/Lecture%20Class%20III.md)|
|   IV    |  07/01/68  | Web page              | [`Lecture Class IV.md`](https://github.com/Ratchanontt/AIPrototype24/blob/main/Lecture%20Class%20IV.md) |
|   V     |  21/01/68  | Environment Conda     | [`Lecture Class V.md`](https://github.com/Ratchanontt/AIPrototype24/blob/main/Lecture%20Class%20V.md)  |
|   VI    |  19/02/68  | Web Service           | [`Lecture Class VI.md`](https://github.com/Ratchanontt/AIPrototype24/blob/main/Lecture%20Class%20VI.md) |
|   VII   |  11/03/68  | Deep Learning         | [`Lecture Class VII.md`](https://github.com/Ratchanontt/AIPrototype24/blob/main/Lecture%20Class%20VII.md) |


# 📔 Contents
<details> 
  <summary> Ubuntu on Windows (Windows Subsystem for Linux (WSL) </summary>

# Command Line พื้นฐานบน Terminal
### 1. ระบุตำแหน่งปัจจุบันที่เราอยู่ในระบบ 
pwd
### 2. list ทุกๆ file/folder ที่อยู่ใน folder ปัจจุบัน 
ls
ls -l
ls -ltr #บอกรายละเอียดไฟล์อย่างละเอียด
### 3. สร้าง Folder
mkdir ชื่อของโฟลเดอร์
### 4. Change directory 
cd 
cd .. #ถอยกลับออกจากโฟลเดอร์ปัจจุบัน 1 ครั้ง
cd ../.. #ออกจากโฟลเดอร์ปัจจุบัน 2 ครั้ง
cd .xxx/yyy/zzz #เปลี่ยน directory แบบระบุปลายทาง
cd filename/ xxx #กรณีที่ชื่อไฟล์มี spacebar คั่น Ex. Class 4 ต้องพิมพ์ `cd Class/ 4`
### 5. Create file 
vi
vi {filename}  #สร้างและเปิดไฟล์
vi {filename.py} #python 
  #กด i เพื่อแก้ไข
  #กด esc + :wq (exit & save)
  #กด esc + :q! (exit but don't save)
### 6. Open file
cat filename #เวลาเราสั่งไม่จำเป็นต้องเข้าไปอยู่ใน folder นั้นๆ
### 7. Move file 
mv {ที่อยู่ต้นทางของ file/folder ที่ต้องการย้าย} {ที่อยู่ปลายทางที่ต้องการที่จะย้าย file/folder ไป}
mv file name .location
mv .xxxxx .zzzzzz #เป็นวิธีการเปลี่ยนชื่อรูปแบบหนึ่ง #Ex. mv ชื่อเก่า ชื่อใหม่
### 8. Copy file
cp {ที่อยู่ต้นทางของ file/folder ที่ต้องการคัดลอก} {ที่อยู่ปลายทางที่ต้องการที่จะคัดลอก file/folder ไป}
cp .zzzzzzz . #คัดลอกไฟล์มาที่โฟลเดอร์ปัจจุบัน
### 9. Manual page
man #ดูเอกสารคำสั่งและโปรแกรมต่าง ๆ ในรูปแบบ "หน้าคู่มือ" 
man ls #ใช้ดูรายการไฟล์ #ใช้ได้กับทุกคำสั่ง ที่เขาเขียน Instruction มาให้
### 10. Delete file
rm # ลบไฟล์
rm -r #.ให้มัน recursive ลบทุกไฟล์ที่มีอยู่ในโฟลเดอร์ เพื่อลบทั้งโฟลเดอร์
### 11. Check Systems Preference
htop #เอาไว้ดูว่ามี RAM อยู่เท่าไหร่ ดูการใช้งานของเครื่อง # ต้อง Install ก่อน

</details>

<details> 
  <summary> Virtual Machines </summary>

# Virtual Machine

### 1. การเข้า Server ด้วย ssh ย่อมาจาก Secure Shell
#คิดเหมือนเปลือกหอย ค่อยๆ หุ้ม ค่อยๆ เข้า
ssh username@IPaddress

### 2. เพิ่ม User เพื่อนให้เข้า server ของเราได้
sudo adduser friendusername

### 3. ใช้ดูการเคลื่อนไหวใน server ของเรา
htop

### 4. ย้าย group
sudo usermod ชื่อเพื่อน ชื่อเรา #ชื่อเพื่อน = group ชื่อเรา = folder
sudo groups ชื่อเรา #เช็คว่ามีใครอยู่ใน server

### 5. เพิ่มเพื่อนให้เป็น SuperUser Do sudo
sudo adduser ชื่อเพื่อน sudo 

</details>

<details> 
  <summary> CloudVM </summary>

# Ubuntu on Cloud VM
## 1. Create VM 
เข้า Portal Azure >>> Education >>> VM >>> Create a virtual machine

## 2. Login & Logout
ssh username@IP #login
exit #logout /// จบ section

## 3. ออกจาก function ex. python
exit()

## 4. scp = secure copy 

- รูปแบบ
  
  scp {path ต้นทาง} {path ปลายทาง}
  

- ส่งไฟล์จากเครื่องเราไปบน Cloud (ต้องรันบนเครื่องเรา)
  
  scp ./xxx nnnt@IP:~/xxx/xxx/. Ex. scp ./testcode.py nnnt@4.221.171.101:~/code/.
  scp -r testfolder1/ nnnt@IP:~/nnnt/. # cp folder in PC to Cloud
  

- ดึงไฟล์จาก cloud มาเครื่องเรา (ต้องรันบนเครื่องเรา)
  
  scp nnnt@IP:/xxx/xxx/yyy.py /home/nnnt
  scp nnnt@4.221.171.101:/home/nnnt/code2/newtest.py /Users/macbookair # move file from folder name code2  on nnnt Cloud to PC
  

## 5. Session
screen -S {screen name} #สร้าง
screen -R #กระโดดกลับเข้่าไปที่ screen
- กด control A+D ออกจาก session
- กด control A+K+y ออกและลบ session
</details>

<details> 
  <summary> GitHub </summary>
  
  - Save code on github
  
  git clone https://github.com/Ratchanontt/AIPrototype24.git
  git add testcloudvm.py
  git commit -m "test cloud server"
  git push
  
  - Check Status
  
  git status
  
  - Setting owner Github (ทำครั้งเดียว)
  
  git config --global user.name "Ratchanontt"
  git config --global user.email "ratchanont.t@kkumail.com"
  

</details>

<details> 
  <summary> Web page </summary>

# Web
## การสร้างเว็บ มี 3 แบบ
- 1. *Web page* no function, only for looking information
  > เป็น web ที่เราเอาข้อมูลของเราใส่เข้าไป เพื่อให้คนอื่นเข้ามาดูข้อมูลของเรา  
- 2. *Web application* add server side project
  > * Server side script* (ใช้ในการคิดคำนวณผลลัพทธ์)  
     >> Server side script เช่น Python (Flask package) : ทำให้ user run บน com ที่ไม่ต้องแรงมากได้เพราะมัน run บน  server และทำให้ code ของ dev ไม่หลุดไปไหน
- 3. *Web service* Server side script only
  > ใช้แค่ Server side script Python (Flask package)  เพราะไม่ได้ต้องการให้คนมาใช้
  > เป็น Back end ล้วนๆ ไม่มี front end

## HTTP Methods
### GET คนเห็นแล้วเปิดได้เลย
GET Method:

- ใช้สำหรับการดึงข้อมูลจากเซิร์ฟเวอร์
- วิธีการนี้ไม่เปลี่ยนแปลงสถานะของเซิร์ฟเวอร์
- ข้อมูลที่ถูกส่งผ่าน GET จะรวมอยู่ใน URL ทำให้ผู้ใช้เปิดดูได้ง่าย เพียงแค่เปิด URL นั้น (อาจมีข้อจำกัดเรื่องขนาดและความปลอดภัย)
- เหมาะสำหรับการค้นหาข้อมูล, เปิดหน้าเว็บ หรือดึงข้อมูลที่ปลอดภัยต่อการเปิดเผย

### Post จับข้อความใส่มาแล้วส่งเลย เป็นการส่งข้อความของฟังก์ชันที่อยู่ข้างใน
POST Method:

- ใช้สำหรับส่งข้อมูลไปยังเซิร์ฟเวอร์ เพื่อประมวลผล เช่น การส่งข้อมูลฟอร์ม, การอัพโหลดไฟล์, การสร้างหรือการเปลี่ยนแปลงข้อมูลเซิร์ฟเวอร์
- ข้อมูลที่ถูกส่งผ่าน POST จะอยู่ใน body ของคำขอ (request body) ทำให้สามารถส่งข้อมูลปริมาณมากได้และมีความปลอดภัยกว่าการแนบมากับ URL
- เหมาะสำหรับการส่งฟอร์มข้อมูล, การทำธุรกรรม, หรือการส่งข้อมูลที่ไม่ควรเปิดเผยใน URL

## Front End
### HTML (จัดรูปแบบหน้า)
- 
<DOCTYPE!>```
  > ส่วนที่ไม่ค่อยมีความสำคัญ เพียงแค่กำหนด
- ```<head>
  > ส่วนที่เป็นหัวเว็บ ตัวอธิบายเว็บ คีย์เวิร์ดของเว็บ โลโก้ ส่วนที่ input สิ่งที่สำคัญๆ
- 
<body>```
  > ส่วนที่จะแสดงอยู่บนเว็บ

### CSS (ช่วย HTML ในการจัดหน้าให้สวยงาม)
- 1. Responsive web
  > เพิ่ม-ลด ขนาดของส่วนประกอบในหน้าเว็บ ตามเครื่องที่ใช้

- 2. Adaptive Web Design (AWD)
  > เว็บไซต์ประเภทนี้ใช้เลย์เอาต์แบบคงที่ที่ปรับไปตามขนาดหน้าจอที่กำหนดเป็นจุด ๆ (breakpoints) เว็บไซต์จะมีหลายเวอร์ชันที่ออกแบบมาสำหรับช่วงของขนาดหน้าจอเฉพาะ เช่น มือถือ แท็บเล็ต และเดสก์ท็อป ซึ่งแตกต่างจาก Responsive Design ที่เลย์เอาต์จะปรับโดยอัตโนมัติตามการย่อขยายของหน้าต่างเบราว์เซอร์

- 3. Static Web Design
  > เว็บไซต์นิ่ง (Static) มีเนื้อหาคงที่และแต่ละหน้าต้องออกแบบแบบแยกกัน ส่วนมากจะใช้ HTML และ CSS โดยไม่ต้องใช้ภาษาโปรแกรมฝั่งเซิร์ฟเวอร์ ทำให้เหมาะสำหรับเว็บไซต์ขนาดเล็กที่เนื้อหาไม่ค่อยเปลี่ยนแปลง

- 4. Dynamic Web Design
  > เว็บไซต์ไดนามิก (Dynamic) สามารถเปลี่ยนแปลงเนื้อหาได้ตามเงื่อนไขหรือเหตุการณ์ที่เกิดขึ้น เช่น การดึงและแสดงข้อมูลที่เปลี่ยนแปลงจากฐานข้อมูล ส่วนมากจะใช้ร่วมกับภาษาโปรแกรมฝั่งเซิร์ฟเวอร์ เช่น PHP, ASP.NET หรือ Java และฐานข้อมูล เช่น MySQL หรือ PostgreSQL

- 5. Single Page Application (SPA)
  > เป็นเว็บไซต์ที่โหลดหน้าเว็บเดียวและเปลี่ยนเนื้อหาภายในหน้านั้นโดยไม่ต้องรีโหลดหน้าทั้งหมด ส่วนมากจะใช้ JavaScript frameworks เช่น React, Angular หรือ Vue.js เพื่อให้การใช้งานที่ลื่นไหลและคล้ายแอปพลิเคชันบนมือถือ

- 6. Progressive Web App (PWA)
  > เป็นการผสมผสานระหว่างเว็บและโมบายแอปพลิเคชัน โดยเสนอลักษณะการทำงานที่คล้ายแอปมือถือ เช่น การเข้าถึงออฟไลน์ การแจ้งเตือนดัน และความสามารถในการติดตั้งบนอุปกรณ์มือถือ

- 7. Mobile-first Web Design
  > การออกแบบเว็บไซต์โดยเน้นที่การแสดงผลบนอุปกรณ์มือถือเป็นหลัก จากนั้นค่อยเพิ่มความซับซ้อนของเลย์เอาต์เมื่อหน้าจอใหญ่ขึ้น วิธีการนี้เน้นการให้ประสบการณ์ที่ดีที่สุดแก่ผู้ใช้บนมือถือก่อน

*แต่ละประเภทมีประโยชน์และความท้าทายที่แตกต่างกัน การเลือกประเภทที่จะใช้ควรพิจารณาจากวัตถุประสงค์ของเว็บไซต์และผู้ใช้งานเป้าหมายเป็นหลัก*

### JavaScript (ควบคุมการทำงาน การกดปุ่มของเครื่อง เพิ่มลูกเล่นให้กับหน้าเว็บ)
- เน้นการใช้งานบนฝั่งไคลเอนต์ (client-side) ของเว็บเบราว์เซอร์ ทำให้เว็บเพจสามารถตอบสนองต่อผู้ใช้และมีลักษณะการทำงานที่โต้ตอบได้ (interactive) มากขึ้น
- ใช้ในการพัฒนาเซิร์ฟเวอร์ (server-side) ผ่าน Node.js
- คุณสมบัติหลักของ JavaScript ได้แก่:
  > - Dynamic Typing: ไม่จำเป็นต้องระบุประเภทของข้อมูล (data type) เมื่อประกาศตัวแปร
  > - Prototype-based: การเขียนโปรแกรมเชิงวัตถุ (Object-Oriented Programming) ที่ใช้ต้นแบบเป็นพื้นฐาน
  > - Event-driven: รองรับการทำงานตามเหตุการณ์ (events) เช่น การคลิกเมาส์หรือการกรอกข้อมูล
  > - First-class Functions: สามารถใช้งานฟังก์ชันเป็นตัวแปร, ส่งผ่านฟังก์ชันไปยังฟังก์ชันอื่น และคืนค่าเป็นผลลัพธ์ได้

## Back End 
- ใช้ได้หลากหลายภาษา วิชานี้ใช้ Python เป็นหลัก

### Python
 Conda สามารถติดตั้งได้จาก
- **Miniconda** 👉 [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)
- **Anaconda** 👉 [https://www.anaconda.com/products/distribution](https://www.anaconda.com/products/distribution)

```sh
conda --version #ตรวจสอบว่าติดตั้งสำเร็จหรือไม่?

#### Python Main Function 
- [https://www.geeksforgeeks.org/python-main-function/](https://www.geeksforgeeks.org/python-main-function/)
Main Function ใช้ควบคุม flow ของ program โดยลำดับการทำงานจะทำตาม Main fc
ดังนั้น จึงจำเป็นต้องมี Main function เพื่อที่เวลาเริ่ม program จะได้รู้ว่าต้อง run อะไรก่อน โดยดูจาก main func


# Python program to demonstrate 
# main() function 

print("Hello") 

# Defining main function 
def main(): 
	print("hey there")  // have only process

# Using the special variable 
# __name__ 
if __name__=="__main__": 
	main()
Output  
Hello  
hey there


#### การรับ input จากภายนอก  
- [Argparse](https://docs.python.org/3/library/argparse.html)
- ใช้สำหรับการประมวลผลและจัดการกับอาร์กิวเมนต์และพารามิเตอร์ที่ส่งเข้ามาในบรรทัดคำสั่ง (command line arguments)
- ช่วยให้สามารถสร้างโปรแกรมที่สามารถรับอาร์กิวเมนต์จากผู้ใช้ได้อย่างสะดวกและใช้งานง่าย
- code ที่ดี ถ้าเสร็จแล้วไม่ควรมาแก้ซ้ำๆ ถ้าจะแก้แค่ input เฉยๆ
- คุณสมบัติหลักของ argparse ได้แก่:
  > - การกำหนดอาร์กิวเมนต์ที่ง่ายดาย: นักพัฒนาสามารถกำหนดอาร์กิวเมนต์ที่โปรแกรมจะรองรับได้อย่างง่ายดาย ทั้งชนิดของข้อมูล (เช่น string, int, float) และค่าเริ่มต้น เป็นต้น
  > - มีการตรวจสอบข้อผิดพลาด: argparse จะตรวจสอบว่าผู้ใช้ได้ส่งอาร์กิวเมนต์ที่ถูกต้องตามที่โปรแกรมกำหนดหรือไม่ และสามารถแสดงข้อความแนะนำวิธีการใช้งานโปรแกรม (help message) ได้โดยอัตโนมัติ
  > - รองรับพารามิเตอร์แบบ positional และ optional: สามารถกำหนดอาร์กิวเมนต์ที่จำเป็นต้องมี (positional) และอาร์กิวเมนต์ที่มีหรือไม่มีก็ได้ (optional)
  > - สร้างคำอธิบายอัตโนมัติ: สามารถสร้างคำอธิบายการใช้งานโปรแกรมและอธิบายอาร์กิวเมนต์ต่าง ๆ ที่โปรแกรมรองรับได้อย่างอัตโนมัติ

import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument('-t', "--time", default = 5)

args = parser.parse_args()
timet = int(args.time)
print(timet)

time.sleep(timet)
input("Press Enter to continue...")
time.sleep(timet)

print("Bye")

</details>

<details> 
  <summary> Environment Conda </summary>

## Install from...
- *Miniconda* 👉 [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)
- *Anaconda* 👉 [https://www.anaconda.com/products/distribution](https://www.anaconda.com/products/distribution)

ssh
- conda --version #ตรวจสอบว่าติดตั้งสำเร็จหรือไม่?

## Manage Environment
- conda create --name {ชื่อ env} python = {versionที่ต้องการ} #สร้าง Environment ใหม่
- conda create -n myenv {name of packager}
- conda activate {ชื่อ env} #เข้าใช้งาน
- conda deactivate #เลิกใช้งาน
- conda remove --name ai_project --all #ลบ Environment
- conda install {ชื่อpackage}

## Install package
อยู่ใน VM และเข้า env แล้ว

- conda install {envi name}
- conda install pandas
</details>

<details> 
  <summary> Web Service </summary>

# Web Service
มีหน้าที่ประมวลผลระหว่างโปรแกรม


รับมา แล้ว ส่งเครดิตไปให้ปลายทาง


# Web Service for Sending Messages
เป็น Web Service ที่สามารถส่งข้อความระหว่างผู้ใช้ได้ โดยประกอบไปด้วย 2 ส่วนหลัก:


## 1. *สคริปต์ฝั่งผู้ใช้* [`call_web_service.py`](https://github.com/Ratchanontt/AIPrototype24/blob/main/call_web_service.py): 
ช่วยให้ผู้ใช้ป้อนข้อความและเลือกผู้รับเพื่อส่งข้อความ

สคริปต์ฝั่งผู้ใช้จะติดต่อกับ API ฝั่งเซิร์ฟเวอร์เพื่อส่งข้อความ โดยมีขั้นตอนดังนี้:
- ผู้ใช้จะป้อนข้อความที่ต้องการส่ง
- ผู้ใช้สามารถเลือกผู้รับได้จาก IP Address
- ส่งข้อความที่เลือกไปยังเซิร์ฟเวอร์ผ่านคำขอ HTTP POST

สคริปต์จะส่งข้อมูลต่อไปนี้ไปยังเซิร์ฟเวอร์:
- msg: ข้อความที่ผู้ใช้ป้อน
- ผู้รับ: ชื่อของผู้รับข้อความ
- ip: ที่อยู่ IP ของผู้รับ
- ผู้ส่ง: ชื่อของผู้ส่งข้อความ

*Code*:
import requests
import json

url = 'http://40.81.22.119:5006/simpleAPI'
myobj = {'msg':'Ratchanont'}

x = requests.post(url, data = json.dumps(myobj))

## 2. *API ฝั่งเซิร์ฟเวอร์* [`firstflask.py`](https://github.com/Ratchanontt/AIPrototype24/blob/main/firstflask.py): 
รับข้อความจากผู้ใช้ บันทึกรายละเอียด และส่งคำตอบกลับไปยืนยันการรับข้อความ


*Code*:
  @app.route('/simpleAPI',methods=['POST'])
  def web_service_API():

     payload = request.data.decode("utf-8")
     inmessage = json.loads(payload)

     print(inmessage)
    
     json_data = json.dumps({'y': 'received!'})
     return json_data
</details>

<details> 
  <summary> Deep Learning </summary>

</details>

# 🏡 Homework
<details> 
  <summary> HW1 Calculate how many days you have lived since birth. </summary> 
👉 สามารถหาได้ด้วยว่าอีกกี่วันจะถึงวันเกิดของคุณ!

[myfirstpy.py](https://github.com/Ratchanontt/AIPrototype24/blob/main/myfirstpy.py)
  
import argparse
from datetime import datetime

def parse_input():
    parser = argparse.ArgumentParser()

    def parse_date(date_str):
        return datetime.strptime(date_str, '%d/%m/%Y')

    parser.add_argument(
        '--bd',
        type=parse_date,
        required=True,
        help='Birthday of the user in format DD/MM/YYYY'
    )
    parser.add_argument(
        '--name',
        type=str,
        default='Ratchanont',
        help='Input the name of the person using the app'
    )

    args = parser.parse_args()
    return args

def printHello(who):
    print(f"Hello World, {who}!!")

def cal_todayVbd(bd):
    today = datetime.today()
    delta = bd - today
    return delta.days

if __name__ == "__main__":
    input_v = parse_input()
    print('This is my first .py file.')
    printHello(input_v.name)
    
    days_to_birthday = cal_todayVbd(input_v.bd)
    if days_to_birthday > 0:
        print(f'Your birthday is in {days_to_birthday} day(s) from today.')
    elif days_to_birthday == 0:
        print("Happy Birthday!")
    else:
        print(f'You have lived for {-days_to_birthday} day(s).')
  
</details>

<details> 
  <summary> HW2 Send messages to friends using the server. </summary> 
👉 สามารถเลือกส่งหาเพื่อนที่เคยบันทึก IP Address ไว้ได้ หรือเพิ่มเพื่อน และส่งข้อความหาคนที่ไม่มีในรายชื่อ
  
[`firstflask.py`](https://github.com/Ratchanontt/AIPrototype24/blob/main/firstflask.py) 
from flask import Flask, render_template, request, render_template_string
import random
import json, jsonify

@app.route('/simpleAPI', methods=['POST'])
def simpleAPI():
    try:
        # รับข้อมูลจาก request
        payload = request.data.decode("utf-8")
        inmessage = json.loads(payload)

        # แสดงข้อมูลที่ได้รับใน log
        print("\n[INFO] ข้อมูลที่ได้รับจากผู้ใช้:")
        print(f"----------------------------")
        print(f"ข้อความที่ได้รับ: {inmessage.get('msg')}")
        print(f"ผู้ส่ง: {inmessage.get('ผู้ส่ง')}")
        print(f"ผู้รับ: {inmessage.get('ผู้รับ')}")
        print(f"IP ของผู้รับ: {inmessage.get('ip')}")
        print(f"----------------------------\n")

        # สร้างข้อมูลที่ต้องการส่งกลับ
        json_data = json.dumps({'y': 'received!'})

        # ส่งข้อมูลกลับไป
        return json_data, 200  # คืนค่า HTTP Status 200 เพื่อบอกว่า request สำเร็จ

    except Exception as e:
        # ในกรณีเกิดข้อผิดพลาด
        error_message = f"[ERROR] ข้อผิดพลาด: {str(e)}"
        print(error_message)

        # ส่งข้อผิดพลาดกลับไป
        return jsonify({'error': 'เกิดข้อผิดพลาดในการประมวลผลข้อมูล'}), 400

if __name__ == "__main__":  # run code
    app.run(host='0.0.0.0',debug=True,port=5006)
[`call_web_service.py`](https://github.com/Ratchanontt/AIPrototype24/blob/main/call_web_service.py)
import requests
import json
import sqlite3

# สร้างหรือเชื่อมต่อกับฐานข้อมูล SQLite
# เพื่อเพิ่มเพื่อนและส่งข้อความหาคนที่ไม่มีในรายชื่อ
conn = sqlite3.connect('message_records.db')
cur = conn.cursor()

# สร้างตารางถ้ายังไม่มี
cur.execute('''
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sender TEXT,
    recipient TEXT,
    recipient_ip TEXT,
    message TEXT,
    status_code INTEGER,
    response_text TEXT
)
''')
conn.commit()

# URL ของ API
url = 'http://40.81.22.119:5006/simpleAPI'

# ป้อนข้อความจากผู้ใช้
msg = input("ป้อนข้อความที่คุณต้องการส่ง: ")

# เลือกคนที่ต้องการส่งข้อความ
print("\nคุณต้องการส่งข้อความหาใคร?:")
print("1. Guitar (IP: 104.43.58.161)")
print("2. Ploy (IP: 13.75.95.136)")
print("3. Nont (IP: 40.81.22.119)")
print("4. Moo (IP: 57.155.113.7)")
print("5. ระบุผู้รับใหม่")

choice = input("กรุณาระบุคนที่ต้องการส่ง: ")

# กำหนด IP และชื่อผู้รับตามตัวเลือก
if choice == '1':
    recipient = "Guitar"
    ip = "104.43.58.161"
elif choice == '2':
    recipient = "Ploy"
    ip = "13.75.95.136"
elif choice == '3':
    recipient = "Nont"
    ip = "40.81.22.119"
elif choice == '4':
    recipient = "Moo"
    ip = "57.155.113.7"
elif choice == '0':
    recipient = input("กรุณาป้อนชื่อผู้รับใหม่: ")
    ip = input("กรุณาป้อน IP Address ของผู้รับใหม่: ")
else:
    print("\n[ERROR] ตัวเลือกไม่ถูกต้อง! กรุณาเลือกตัวเลือกที่ถูกต้อง.")
    exit()

# ชื่อผู้ส่ง
sender = "nnnt" # ชื่อของเรา

# สร้าง dictionary สำหรับข้อมูลที่จะส่งไป
myobj = {
    'message_key': 'message_val',
    'msg': msg,  # ใช้ข้อความที่ผู้ใช้ป้อน
    'ผู้รับ': recipient,  # ชื่อผู้รับ
    'ip': ip,  # IP ของผู้รับ
    'ผู้ส่ง': sender  # ชื่อผู้ส่ง
}

# แสดงข้อมูลก่อนส่ง
print("\nกำลังส่งข้อความ... \n")
print(f"ข้อมูลที่ส่งไป: ")
print(f"----------------------------")
print(f"ผู้ส่ง: {sender}")
print(f"ผู้รับ: {recipient}")
print(f"IP ของผู้รับ: {ip}")
print(f"ข้อความที่ส่ง: {msg}")
print(f"----------------------------\n")

# ส่งคำขอ POST
try:
    response = requests.post(url, data=json.dumps(myobj), timeout=90)
    response.raise_for_status()
    print(f"การส่งข้อความสำเร็จ! คำตอบจาก API: {response.text}")
    status_code = response.status_code
    response_text = response.text
except requests.exceptions.HTTPError as errh:
    print("ข้อผิดพลาด HTTP:", errh)
    status_code = response.status_code if response else None
    response_text = str(errh)
except requests.exceptions.ConnectionError as errc:
    print("ข้อผิดพลาดการเชื่อมต่อ:", errc)
    status_code = None
    response_text = str(errc)
except requests.exceptions.Timeout as errt:
    print("ข้อผิดพลาด Timeout:", errt)
    status_code = None
    response_text = str(errt)
except requests.exceptions.RequestException as err:
    print("Oops: เกิดข้อผิดพลาดบางอย่าง", err)
    status_code = None
    response_text = str(err)

# บันทึกข้อมูลในฐานข้อมูล
cur.execute('''
INSERT INTO messages (sender, recipient, recipient_ip, message, status_code, response_text)
VALUES (?, ?, ?, ?, ?, ?)
''', (sender, recipient, ip, msg, status_code, response_text))
conn.commit()

# ปิดการเชื่อมต่อกับฐานข้อมูล
conn.close()
