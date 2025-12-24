# Install Miniconda (Linux)
## Lecture : Python Environment Setup

เอกสารนี้อธิบายขั้นตอนการติดตั้ง **Miniconda บนระบบ Linux**  
ซึ่งใช้สำหรับจัดการ Python environment และ package สำหรับงานพัฒนาและรัน Server


---

## 1. Download & Install Miniconda

ให้รันคำสั่งต่อไปนี้ **ทีละบรรทัด** เพื่อดาวน์โหลดและติดตั้ง Miniconda  
(สำหรับ Linux – x86_64)

```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
```

คำอธิบายโดยสรุป
- สร้างโฟลเดอร์สำหรับติดตั้ง Miniconda
- ดาวน์โหลดไฟล์ติดตั้งจากเว็บไซต์ทางการ
- ติดตั้ง Miniconda แบบไม่ต้องตอบคำถาม (batch mode)
- ลบไฟล์ติดตั้งเมื่อเสร็จสิ้น

---

## 2. Activate Miniconda

หลังจากติดตั้งเสร็จแล้ว  
ให้ **ปิดแล้วเปิด Terminal ใหม่**  
หรือใช้คำสั่งด้านล่างเพื่อ refresh environment

```bash
source ~/miniconda3/bin/activate
```

---

## 3. Initialize Conda

ตั้งค่า conda ให้สามารถใช้งานได้กับทุก shell

```bash
conda init --all
```

เมื่อดำเนินการเสร็จแล้ว  
จะเห็น `(base)` แสดงอยู่หน้าชื่อเครื่องใน Terminal

---

## Python Command Line

Python environment นี้ใช้สำหรับเขียนและรันโปรแกรมบน Server

เปิด VS Code ผ่าน Command Line

```bash
code
```

เปิดหรือสร้างไฟล์ใน VS Code

```bash
code <file_name>
```

---

## Screen Session

`screen` ใช้สำหรับรันโปรแกรมบน Server แบบต่อเนื่อง  
แม้จะปิด Terminal หรือหลุดจาก SSH โปรแกรมก็ยังทำงานอยู่

---

### สร้าง Screen ใหม่

```bash
screen -S <screen_name>
```

### กลับเข้า Screen ที่มีอยู่

```bash
screen -R
```

---

### คำสั่งควบคุม Screen

```
Ctrl + A + D   ออกจาก session (โปรแกรมยังทำงานอยู่)
Ctrl + A + K + Y   ออกจากและลบ session
Ctrl + A + [   Freeze หน้าจอ (สามารถเลื่อนดูได้)
q + Enter      ออกจากโหมด freeze
Ctrl + C       หยุดโปรแกรมที่กำลังรัน
```

---

### ตรวจสอบ Screen ที่มีอยู่

```bash
screen -R <screen_name>
```

สามารถกด `Tab` เพื่อดูรายการ screen ที่มีทั้งหมด

---

### ลบ Screen ที่ชื่อซ้ำ

ขั้นตอนที่ 1 เข้าไปยัง screen ด้วย ID

```bash
screen -R id.<screen_name>
```

ตัวอย่าง

```bash
screen -R 12107.testscreen1
```

ขั้นตอนที่ 2 ลบ screen

```
Ctrl + A + K + Y
```

---

## Notes

- `screen` เหมาะสำหรับรัน server หรือ process ระยะยาว
- ควรใช้ `screen` ควบคู่กับ `ssh` บน VM
- หลังติดตั้ง conda ให้ตรวจสอบว่า `(base)` แสดงใน Terminal ทุกครั้ง
