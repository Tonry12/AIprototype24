# Command Line พื้นฐานบน Ubuntu
## 1. คำสั่งพื้นฐาน
* list ทุกๆ file/folder ที่อยู่ใน folder ปัจจุบัน
  ```
  $ls
  ```
  ```
  $ls -{option}
  #ex
  $ls -ltr # บอกรายบละเอียดไฟล์ โดยเรียงลำดับจากใหม่ไปเก่าตามเวลา
  ```
* ระบุตำแหน่งปัจจุบันที่เราอยู่ในระบบ
  ```
  $pwd
  คำสั่งนี้จะบอกตำแหน่งที่คุณอยู่ในระบบไฟล์
  ```  
  
## 2. การจัดการ Folder และ File
* create folder
  ```
  $mkdir {foldername}
  ใช้คำสั่งนี้ในการสร้างโฟลเดอร์ใหม่
  ```
* create file 
  ```
  $vi {filename}  # สร้างและเปิดไฟล์ขึ้นมาแก้ไข
  $vi {filename.py} # python file
  #กด i เพื่อแก้ไข
  #กด esc + :wq (ออกแบบ save สิ่งที่เราพิมพ์เข้าไป)
  #กด esc + :q! (ออกแบบไม่ save สิ่งที่อัปลงไป)
  ```
  เวลาจะพิมพ์ กด ***i*** แล้วมันจะขึ้นว่า ***INSERT*** แล้วถึงพิมพ์ได้
  หลังจากนั้นเมื่อพิมพ์เสร็จต้องการที่จะบันทึกให้กด ***esc*** แล้วพิมพ์ **:wq** (write and quit)
* เปิดไฟล์ขึ้นมาดูที่เขียนเฉยๆ
  ```
  $cat {filename}
  ```
* run code Python 
  ```
  $python {filename.py}
  ```
* delete folder
  ```
  $rm -R {foldername}
  ```
* delete file
  ```
  $rm {filename}
  ```
* เปลี่ยนชื่อ file
  ```
  $mv {file เดิม} {file ใหม่}
  $mv ./{file เดิม} ./{file ใหม่}
  # $mv file1 filex # เปลี่ยนชื่อจาก file1 เป็น filex
  ```
* change directory (เข้าไปในfolder)
  ```
  $cd {foldername}
  ```
* ออกจาก folder
  ```
  $cd # home
  $cd ~ # home
  $cd .. # ออกมา 1 step
  $cd ../.. # ออกมา 2 step
  $cd ../../test_lv3 # ออกมา 2 step แล้วมาที่ folfer test_lv3
  ```
## 3. การ copy และการย้าย file/folder
ที่อยู่ของ File/Folder ในตอนสุดท้าย
![image](https://github.com/nattntn/AIPrototype2023/blob/main/lecture/%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%88%E0%B8%B1%E0%B8%94%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%84%E0%B8%9F%E0%B8%A5%E0%B9%8C.jpg)
* หลักการ
  ```
  $cp {ที่อยู่ต้นทางของ file/folder ที่ต้องการคัดลอก} {ที่อยู่ปลายทางที่ต้องการที่จะคัดลอก file/folder ไป}
  $mv {ที่อยู่ต้นทางของ file/folder ที่ต้องการย้าย} {ที่อยู่ปลายทางที่ต้องการที่จะย้าย file/folder ไป}
  ```
* Copy file
  ```
  $cp ./filex ~/testfolder1/testfolder1_1/. # ~ กลับไปที่ home ก่อน
  ```
  ```
  # copy file1 in testfolder1 to testfolder1_1_1
  $cp ./file1 ./testfolder1_1/testfolder1_1_1/.
  # cp ที่นี่/ชื่อไฟล์ ที่นี่/เข้าไปที่1_1/เข้าไปที่1_1_1/เอาไว้ตรงนี้
  ```
* Copy and change the file name
  คัดลอกไฟล์ 1 ไปที่ testfolder1_1_1 โดยให้มีชื่อว่า file2
  ```
  $cp ./file1 ./testfolder1_1/testfolder1_1_1/file2
  ```
* Copy folder
  ```
  # copy folder + change folder name แต่เอาไว้ที่เดิม
  $cp -R ./testfolder1_1_1 ./testfolder1_1_2
  ```
* Move file
  ```
  $ mv ./filex ~/testfolder2/. # ~ home
  $ mv ./filex ../../../testfolder2/.
  ```
# ยกเลิกคำสั่ง
> ctrl+c
# Homework
copy filex in testfolder1_1 to testfolder1_1_2 and change file name to filey
```
cp ./filex ~/testfolder1/testfolder1_1/testfolder1_1_2/filey
```
## คำสั่ง: mv newfile.x ./test_lv3/test_lv4/.

คำสั่งนี้หมายถึงการย้ายไฟล์ "newfile.x" จากตำแหน่งปัจจุบันไปยังโฟลเดอร์ "test_lv4" ที่อยู่ภายใน "test_lv3" ซึ่งตั้งอยู่ภายในโฟลเดอร์ "test" ในโครงสร้างระบบไฟล์

รายละเอียด:
- **mv**: คำสั่งในการย้ายไฟล์
- **newfile.x**: ไฟล์ที่ต้องการย้าย
- **./test_lv3/test_lv4/.**: ตำแหน่งปลายทาง (โฟลเดอร์ "test_lv4" ที่อยู่ภายใน "test_lv3")
  
การใช้ `.` ที่ท้ายหมายถึงการย้ายไฟล์ "newfile.x" ไปยังโฟลเดอร์ "test_lv4" โดยไม่เปลี่ยนชื่อไฟล์

ตำแหน่งปัจจุบัน:
- โฟลเดอร์ที่คำสั่งนี้ถูกใช้คือ `~/test/test_lv2`

ผลลัพธ์:
- ไฟล์ "newfile.x" จะถูกย้ายไปที่ "test_lv4" ภายในโฟลเดอร์ "test_lv3"

## คำสั่ง: mv ./test_lv3/test_lv4/newfile.x ./test_lv3/test_lv4/newfile.z

คำสั่งนี้หมายถึงการเปลี่ยนชื่อไฟล์ "newfile.x" เป็น "newfile.z" ในโฟลเดอร์ "test_lv4" ซึ่งอยู่ภายในโฟลเดอร์ "test_lv3"

รายละเอียด:
- **mv**: คำสั่งในการย้ายหรือเปลี่ยนชื่อไฟล์
- **./test_lv3/test_lv4/newfile.x**: ไฟล์ต้นทาง (ไฟล์ที่ต้องการเปลี่ยนชื่อ)
- **./test_lv3/test_lv4/newfile.z**: ไฟล์ปลายทาง (ชื่อไฟล์ใหม่)

ผลลัพธ์:
- ไฟล์ "newfile.x" จะถูกเปลี่ยนชื่อเป็น "newfile.z" ในตำแหน่งเดียวกัน (ในโฟลเดอร์ "test_lv4")

  
