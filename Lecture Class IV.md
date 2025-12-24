# Managing Conda Environment  
Lecture: Environment & Version Control

---

## Installing Conda
Conda สามารถติดตั้งได้จาก 2 แหล่งหลัก

### Miniconda  
ขนาดเล็ก เหมาะสำหรับใช้งานบน Server  
https://docs.conda.io/en/latest/miniconda.html

### Anaconda  
มาพร้อมเครื่องมือครบถ้วนและ GUI  
https://www.anaconda.com/products/distribution

### ตรวจสอบการติดตั้ง
```bash
conda --version
```

---

## Create Conda Environment
เมื่อเปิด Terminal ใหม่ ค่าเริ่มต้นจะอยู่ที่ environment ชื่อ `base`

### สร้าง Environment ใหม่
```bash
conda create --name <env_name> python=<version>
```

ตัวอย่าง
```bash
conda create --name testpy38 python=3.8
```

### เข้าใช้งาน Environment
```bash
conda activate <env_name>
```

### ออกจาก Environment
```bash
conda deactivate
```

### ลบ Environment
```bash
conda remove --name <env_name> --all
```

### ดูรายการ Environment ทั้งหมด
```bash
conda env list
```

---

## Install Packages
ต้อง Activate Environment ก่อนติดตั้ง Package ทุกครั้ง

### ติดตั้ง Package
```bash
conda install <package_name>
```

ตัวอย่าง
```bash
conda install pandas
```

### ดูรายการ Package ที่ติดตั้งอยู่
```bash
conda list
```

---

## GitHub Command Line

### Git Configuration (ตั้งค่าเพียงครั้งเดียว)
```bash
git config --global user.name "username"
git config --global user.email "email@example.com"
```

หมายเหตุ: การ push ขึ้น GitHub ต้องใช้ Personal Access Token แทน password

---

## Clone Repository
```bash
git clone <repository_url>
```

---

## Save Code to GitHub
ขั้นตอนเมื่อมีการแก้ไขไฟล์

### 1. ดึงเวอร์ชันล่าสุด
```bash
git pull
```

### 2. เพิ่มไฟล์เข้า staging
```bash
git add <file_name>
```

### 3. Commit การเปลี่ยนแปลง
```bash
git commit -m "commit message"
```

### 4. Push ขึ้น GitHub
```bash
git push
```

ลำดับคำสั่งที่ต้องจำ  
**add → commit → push**

---

## Check Status
```bash
git status
```

ความหมายของสถานะไฟล์  
- สีแดง: ไฟล์ยังไม่ถูก track  
- สีเขียว: ไฟล์อยู่ใน staging  
- ไม่แสดงสถานะ: ทุกอย่างเรียบร้อยแล้ว

---

## GitHub Token
สร้าง Token ได้ที่  
GitHub → Settings → Developer Settings → Personal Access Tokens  

หมายเหตุ: Token จะแสดงเพียงครั้งเดียว ควรเก็บไว้ให้ดี

---

## Useful Command Line Tips
ค้นหาคำสั่งที่เคยใช้ใน Terminal
```text
Ctrl + R
```
พิมพ์ keyword เพื่อค้นหาคำสั่งที่เคยใช้ย้อนหลัง
