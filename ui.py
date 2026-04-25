import customtkinter as ctk
from scanner import scan_directory
from analyzer import analyze_files
from duplicate import find_duplicates
from malware_detector import detect_malware

from tkinter import filedialog
from ai_model.summarizer import summarize_text
from ai_model.extractor import extract_keywords, generate_questions
from recommender import generate_recommendations

import PyPDF2
import docx
import threading

import matplotlib.pyplot as plt
from collections import Counter

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Memory Vault AI")
        self.geometry("1000x600")

        # CACHE
        self.cached_files = None

        # Sidebar
        self.sidebar = ctk.CTkFrame(self, width=200)
        self.sidebar.pack(side="left", fill="y")

        ctk.CTkLabel(self.sidebar, text="Memory Vault AI",
                     font=("Arial", 18, "bold")).pack(pady=20)

        ctk.CTkButton(self.sidebar, text="Scan System",
                      command=self.scan).pack(pady=10)

        ctk.CTkButton(self.sidebar, text="Find Duplicates",
                      command=self.duplicates).pack(pady=10)

        ctk.CTkButton(self.sidebar, text="Detect Malware",
                      command=self.detect_harmful).pack(pady=10)

        ctk.CTkButton(self.sidebar, text="Analyze File (AI)",
                      command=self.analyze_file).pack(pady=10)

        ctk.CTkButton(self.sidebar, text="Smart Suggestions",
                      command=self.show_recommendations).pack(pady=10)

        ctk.CTkButton(self.sidebar, text="Dashboard Charts",
                      command=self.show_dashboard).pack(pady=10)

        # Output
        self.output = ctk.CTkTextbox(self)
        self.output.pack(fill="both", expand=True, padx=10, pady=10)

    # ---------------- AUTO SCAN ---------------- #
    def get_files(self):
        if not self.cached_files:
            self.output.delete("1.0", "end")
            self.output.insert("end", "🔍 Scanning system (auto)...\n")
            self.update()
            self.cached_files = scan_directory()
        return self.cached_files

    # ---------------- SYSTEM SCAN ---------------- #
    def scan(self):
        self.output.delete("1.0", "end")
        self.output.insert("end", "🔍 Scanning system...\n")
        self.update()

        self.cached_files = scan_directory()

        important, junk = analyze_files(self.cached_files)

        self.output.delete("1.0", "end")

        self.output.insert("end", f"📊 Total Important Files: {len(important)}\n")
        self.output.insert("end", f"🧹 Total Junk Files: {len(junk)}\n\n")

        self.output.insert("end", "=== IMPORTANT FILES (Top 10) ===\n\n")
        for f in important[:100]:
            self.output.insert("end", f"{f['name']} | Views: {f['view_score']}\n")

        self.output.insert("end", "\n=== JUNK FILES (Top 10) ===\n\n")
        for f in junk[:35]:
            self.output.insert("end", f"{f['name']} | Unused: {f['days_unused']} days\n")

    # ---------------- DUPLICATES ---------------- #
    def duplicates(self):

        def run():
            files = self.get_files()

             # ✅ LIMIT FILE COUNT (FAST FIX)
            files = files[:2000]

            dups = find_duplicates(files)

            self.after(0, lambda: show_result(dups, len(files)))

        def show_result(dups, total):
            self.output.delete("1.0", "end")

            self.output.insert("end", f"Scanned Files: {total}\n\n")

            if not dups:
                self.output.insert("end", "✅ No duplicate files found.\n")
                return

            self.output.insert("end", f"📁 Duplicates Found: {len(dups)}\n\n")

            for d in dups[:20]:
                self.output.insert("end", f"{d}\n")

        self.output.delete("1.0", "end")
        self.output.insert("end", "⚡ Finding duplicates (fast mode)...\n")

        threading.Thread(target=run, daemon=True).start()

    # ---------------- MALWARE ---------------- #
    def detect_harmful(self):
        files = self.get_files()

        self.output.delete("1.0", "end")
        self.output.insert("end", "🔍 Detecting harmful files...\n")
        self.update()

        harmful = detect_malware(files)

        self.output.delete("1.0", "end")
        self.output.insert("end", f"⚠️ Total Harmful Files: {len(harmful)}\n\n")

        for f in harmful[:30]:
            self.output.insert("end", f"{f['name']} | Size: {f['size']}\n")

    # ---------------- FILE READER ---------------- #
    def read_file(self, path):
        text = ""

        try:
            if path.endswith(".txt"):
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    text = f.read()

            elif path.endswith(".pdf"):
                reader = PyPDF2.PdfReader(path)
                for page in reader.pages:
                    content = page.extract_text()
                    if content:
                        text += content

            elif path.endswith(".docx"):
                doc = docx.Document(path)
                for para in doc.paragraphs:
                    text += para.text + "\n"

        except Exception as e:
            print("Read error:", e)

        return text

    # ---------------- AI ANALYSIS ---------------- #
    def analyze_file(self):
        try:
            file_path = filedialog.askopenfilename(
                filetypes=[("Documents", "*.txt *.pdf *.docx")]
            )

            if not file_path:
                return

            self.output.delete("1.0", "end")
            self.output.insert("end", "📄 Reading file...\n")
            self.update()

            text = self.read_file(file_path)

            if not text.strip():
                self.output.insert("end", "❌ No readable content found.")
                return

            self.output.insert("end", "🧠 Analyzing content...\n")
            self.update()

            summary = summarize_text(text)
            keywords = extract_keywords(text)
            questions = generate_questions(summary)

            self.output.delete("1.0", "end")

            self.output.insert("end", "=== SUMMARY ===\n\n")
            for s in summary:
                self.output.insert("end", f"- {s}\n")

            self.output.insert("end", "\n=== KEYWORDS ===\n\n")
            self.output.insert("end", ", ".join(keywords) + "\n")

            self.output.insert("end", "\n=== QUESTIONS ===\n\n")
            for q in questions:
                self.output.insert("end", f"- {q}\n")

        except Exception as e:
            print("ERROR:", e)
            self.output.insert("end", f"\nError: {str(e)}")

    # ---------------- SMART SUGGESTIONS ---------------- #
    def show_recommendations(self):
        files = self.get_files()

        important, junk = analyze_files(files)
        harmful = detect_malware(files)

        suggestions = generate_recommendations(important, junk, harmful)

        self.output.delete("1.0", "end")
        self.output.insert("end", "=== SMART SUGGESTIONS ===\n\n")

        for s in suggestions:
            self.output.insert("end", f"- {s}\n")

    # ---------------- DASHBOARD ---------------- #
    def show_dashboard(self):
        files = self.get_files()

        important, junk = analyze_files(files)

        plt.figure()
        plt.pie([len(important), len(junk)],
                labels=['Important', 'Junk'],
                autopct='%1.1f%%')
        plt.title("File Importance Distribution")

        extensions = [f['name'].split('.')[-1]
                      for f in files if '.' in f['name']]

        ext_count = Counter(extensions)
        top_ext = dict(ext_count.most_common(5))

        plt.figure()
        plt.bar(top_ext.keys(), top_ext.values())
        plt.title("Top File Types")

        plt.show()

        self.output.insert("end", "✅ Dashboard displayed!")