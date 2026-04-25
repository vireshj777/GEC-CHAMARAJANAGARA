<img width="1514" height="956" alt="Screenshot 2026-04-25 111058" src="https://github.com/user-attachments/assets/d7ef5e17-d2d3-4a2d-acf0-45abc843bdf6" />
<img width="1497" height="942" alt="Screenshot 2026-04-25 111025" src="https://github.com/user-attachments/assets/42225f28-2d60-40f0-b293-f42bb80e6ba3" />
<img width="1502" height="947" alt="Screenshot 2026-04-25 111007" src="https://github.com/user-attachments/assets/fd42bf7b-4725-4e33-b32d-c192c964084e" />
<img width="1495" height="937" alt="Screenshot 2026-04-25 110934" src="https://github.com/user-attachments/assets/20e4f4c9-3eb4-401a-b442-7f43396a2a62" />
<img width="1500" height="944" alt="Screenshot 2026-04-25 110917" src="https://github.com/user-attachments/assets/5ab7c330-5d9b-4b0d-8242-290d14f3ec66" />
<img width="1506" height="895" alt="Screenshot 2026-04-25 110850" src="https://github.com/user-attachments/assets/da66c5fd-bdc2-4600-a501-f65fe898d85b" />
<img width="1502" height="942" alt="Screenshot 2026-04-25 110744" src="https://github.com/user-attachments/assets/04ea054b-6397-4047-b17e-9f20c94d140a" />
# GEC-CHAMARAJANAGARA
# 🧠 Memory Vault AI

Memory Vault AI is an intelligent system application designed to analyze, organize, and optimize files across a computer system. It helps users identify important files, remove unnecessary clutter, detect duplicates, and gain insights using AI-powered analysis.

---

## 🚀 Features

### 📁 Smart File Analysis

* Identifies **important files** based on usage patterns
* Detects **junk/unnecessary files** using last accessed time

### 🔁 Duplicate File Detection

* Finds duplicate files using hashing
* Helps free up storage space

### ⚠️ Malware Detection

* Flags suspicious or harmful files
* Enhances system security awareness

### 🤖 AI File Analysis

* Supports `.txt`, `.pdf`, `.docx`
* Generates:

  * Summary
  * Keywords
  * Possible questions

### 💡 Smart Recommendations

* Suggests actions like:

  * Delete unused files
  * Backup important files
  * Review suspicious files

### 📊 Dashboard Visualization

* Pie chart → Important vs Junk files
* Bar chart → File type distribution

### ⚡ Automated System Scan

* Scans entire system or drives
* Uses caching for faster performance

---

## 🛠️ Technologies Used

* **Python**
* **CustomTkinter** – Modern UI
* **OS & File Handling** (`os`, `stat`)
* **Hashlib (MD5)** – Duplicate detection
* **NLTK** – Text processing
* **PyPDF2** – PDF reading
* **python-docx** – Word file handling
* **Matplotlib** – Data visualization
* **Threading** – Performance optimization

---

## 📂 Project Structure

```
MemoryVaultAI/
│
├── main.py
├── ui.py
├── scanner.py
├── analyzer.py
├── duplicate.py
├── malware_detector.py
├── recommender.py
│
├── ai_model/
│   ├── summarizer.py
│   ├── extractor.py
│
└── requirements.txt
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/MemoryVaultAI.git
cd MemoryVaultAI
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Download NLTK Data

```
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

---

## ▶️ Usage

Run the application:

```
python main.py
```

### Available Options:

* Scan System
* Find Duplicates
* Detect Malware
* Analyze File (AI)
* Smart Suggestions
* Dashboard Charts

---

## 🎯 Use Cases

* System cleanup and storage optimization
* Duplicate file removal
* File content understanding using AI
* Personal file management assistant
* Security awareness for suspicious files

---

## 🌍 Impact

* Saves storage space
* Improves system performance
* Reduces manual effort
* Enhances user productivity
* Provides intelligent file insights

---

## 🚀 Future Scope

* Cloud integration for backup
* Mobile & web versions
* Advanced AI models for deeper analysis
* Personalized recommendations
* Real-time monitoring system

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and submit a pull request.

---

## 📄 License

This project is for educational purposes.

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
