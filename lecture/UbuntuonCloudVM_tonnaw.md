![VM](https://github.com/nattntn/AIPrototype2023/blob/main/lecture/VM.jpg)
 # 1.การสร้าง VM
เข้า Azure -> Education -> VM -> Create a virtual machine
> password: Nat{National ID}_
 # 2. login/logout  VM จาก PC
 ```
 $ssh username@IP #login
 $exit #logout //จบ section
 เช่น ssh tonty@20.21...
     exit
 ```

 # 3. Move file/folder in PC to Cloud and vice versa 
 __ตอนย้ายต้องอยู่ในเครื่องเท่านั้น!!__
* Format
  ```
  $scp {ที่อยู่ต้นทาง} {ที่อยู่ปลายทาง}
  ```
* ส่งไฟล์จากเครื่องเราไปบน Cloud
  ```
  $scp ./xxx nattntn@IP:/xxx/xxx/.
         ชื่อไฟล์ ชื่อล็อกอิน@IP:
  $scp -r testfolder1/ nattntn@IP:/home/nattntn/. # cp folder in PC to Cloud
  ```
* ตัวอย่าง ฉัน save file ที่ชื่อ testcode.py ในเครื่อง ในที่อยู่คือ c/Users/Administrator/Documents/Work/AIprototype__
 โดยใช้คำสั่ง 
  ```
  /mnt/c$ cd Users/Administrator/Documents/Work/AIprototype/
  จากนั้น จะดึงไฟล์ไปที่ปลายทางเรา คือ /home/tonnaw/code
  scp testcode.py tonnaw@20.2.154.196:/home/tonnaw/code/.
  scp ชื่อไฟล์ที่จะย้าย ชื่อuserเรา@IP:ปลายทาง/.
  ```
* ดึงไฟล์จาก cloud มาเครื่องเรา
 โดยที่เราต้องเริ่มจากเครื่องเรา เพราะว่าเราจะสามารถใส่ public ip ของ could ได้
 ถ้าเราอยู่ could แล้วจะย้ายมาเครื่องเรา มันทำไม่ได้ เพราะเครื่องเรามันไม่มี public ip
 เราเลยมาตั้งต้นที่ เครื่องเรา
  ```
  $scp username@IP:/xxx/xxx/yyy.py /home/tonnaw
  $scp username@IP:โฟลเดอร์ต่างๆ/yyy.py ที่อยู่คอมเรา
  $scp tonnaw@20.2.154.196:/home/tonnaw/code2/testcode.py /home/tonnaw
  ```
 # 4. Cloud Shell (ใช้ Terminal on Internet)
 > Shell.Azure.com
* ครั้งแรก ssh เข้า VM ก่อน
  ```
   $ssh username@IP #login
   $exit #logout //จบ section
  ```
* Upload file <ต้องอยู่บน shell แล้วค่อย scp to cloud >
  ```
  # 1. upload file on shell
  # 2. scp file to cloud
  $scp rog.png nattntn@IP:/~/. # ย้ายมาhome // ทำบนshell
  ```
  # 5. สร้างเครื่องที่ให้เพื่อนเข้ามาใช้บน Cloud เราร่วมกันได้
  * 1. สร้างเครื่องให้เพื่อน
    ```
    $sudo adduser {ชื่อเครื่อง} #sudo = super user (เจ้าของเครื่อง) do
    # password
    ```
  * 2. ให้เพื่อนลองเข้า Cloud ที่เราสร้าง บน เครื่องเพื่อน
    ```
    $ssh {ชื่อเครื่องที่สร้าง}@IP #IP super user
    $htop # ดูว่าเพื่อนเข้ามายัง
    ```
  * 3. แก้ไข Permission ของเครื่องที่สร้าง
    super user แก้ไขได้
    ```
    $sudo chmod 755 yoke # chmod = change mode // 7 = owner(r|w|x), 5 = group (r|-|x),5 =other (r|-|x)
    ```
    
    
  
  
 
 
