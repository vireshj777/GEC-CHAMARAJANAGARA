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
