# Cloud Virtual Machines  


## Virtual Machine (VM) บน Azure

Virtual Machine คือ Server เสมือนที่ทำงานอยู่บนคลาวด์  
สามารถใช้งานได้เหมือนเครื่อง Linux จริง

### ขั้นตอนการสร้าง VM

```
Azure Portal → Education → Virtual Machines → Create a virtual machine
```

---

## 1. เข้าใช้งาน Server ด้วย SSH

SSH (Secure Shell) ใช้สำหรับเชื่อมต่อจากเครื่องของเราไปยัง VM

```bash
ssh username@IPaddress
```

- `username` คือชื่อผู้ใช้ที่ตั้งไว้ตอนสร้าง VM
- `IPaddress` คือ Public IP ของ VM

---

## 2. เพิ่ม User ให้ผู้อื่นเข้าใช้งาน Server

ใช้สำหรับให้เพื่อนหรือผู้ร่วมงานเข้าใช้งาน VM เดียวกัน

```bash
sudo adduser friendusername
```

---

## 3. ตรวจสอบการทำงานของ Server

ใช้ดูการใช้งาน CPU และ RAM ของ VM

```bash
htop
```

> ต้องติดตั้งโปรแกรมก่อนจึงจะใช้งานได้

---

## 4. จัดการ Group ของ User

ย้าย user ให้อยู่ใน group เดียวกัน

```bash
sudo usermod friendusername yourusername
```

ตรวจสอบว่า user อยู่ใน group ใดบ้าง

```bash
sudo groups yourusername
```

---

## 5. เพิ่มสิทธิ์ SuperUser (sudo)

ใช้สำหรับให้ user คนอื่นสามารถรันคำสั่งระดับผู้ดูแลระบบได้

```bash
sudo adduser friendusername sudo
```

---

## 6. SCP — การส่งไฟล์ระหว่างเครื่องกับ Cloud

SCP (Secure Copy) ใช้ส่งไฟล์ระหว่าง  
**เครื่องเรา ↔ Virtual Machine**

> ต้องรันคำสั่งนี้บนเครื่องของเรา ไม่ใช่ภายใน VM

### รูปแบบคำสั่งพื้นฐาน

```bash
scp <source_path> <destination_path>
```

### ส่งไฟล์จากเครื่อง → VM

```bash
scp <path_file>/<filename> username@IP:~<folder>/.
```

### ส่งไฟล์จาก VM → เครื่อง

```bash
scp username@IP:<path_file>/<filename> <destination_path>/.
```

### คัดลอกทั้งโฟลเดอร์

```bash
scp -r <folder_source> username@IP:~<folder>/.
```

---

## 7. ออกจาก Program (เช่น Python)

```bash
exit()
```

---

## 8. Log out ออกจาก Virtual Machine

```bash
exit
```

---

## Example Workflow

### ส่งไฟล์จากเครื่อง → VM
1. ใช้คำสั่ง `scp` บนเครื่องของเรา
2. เข้า VM ด้วย `ssh`
3. ตรวจสอบไฟล์ด้วย `ls`

### ส่งไฟล์จาก VM → เครื่อง
1. ออกจาก VM ก่อน
2. ใช้คำสั่ง `scp` บนเครื่องของเรา

---

## Python Environment

### Miniconda

Miniconda ใช้สำหรับจัดการ Python environment  
ช่วยแยก package และเวอร์ชันของ Python ได้อย่างเป็นระบบ

หากต้องการให้ `(base)` แสดงอัตโนมัติทุกครั้ง  
ให้ตั้งค่า environment ตามลำดับที่กำหนด

---

## Notes เพิ่มเติม

- `exit()` ต้องมีวงเล็บ
- `scp` ต้องรันจากเครื่องของเรา
- `ssh` ใช้ username ที่ตั้งตอนสร้าง VM
- ควรตรวจสอบไฟล์บน VM ด้วย `ls` ทุกครั้ง
