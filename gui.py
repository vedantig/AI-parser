#!/usr/bin/env python3
import json
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

from main import process_file

class DocParserApp(tk.Tk):
    """GUI for selecting a PDF/DOCX file and displaying parsed output."""

    def __init__(self):
        super().__init__()
        self.title("AI Document Parser")
        self.geometry("600x400")

        tk.Button(self, text="Select PDF/DOCX", command=self.load_file).pack(pady=20)
        self.text_box = tk.Text(self, wrap="word")
        self.text_box.pack(expand=True, fill="both", padx=10, pady=10)

    def load_file(self):
        """Handle file selection, parsing, and displaying output."""
        file_path = filedialog.askopenfilename(
            title="Select a PDF or DOCX file",
            filetypes=[
                ("Supported files", "*.pdf *.docx"),
                ("PDF files", "*.pdf"),
                ("Word files", "*.docx"),
                ("All files", "*.*"),
            ]
        )
        if not file_path:
            return

        try:
            output = process_file(Path(file_path), to_csv=True)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return

        self.text_box.delete("1.0", tk.END)
        self.text_box.insert(tk.END, json.dumps(output, indent=2))

        messagebox.showinfo(
            "Done",
            f"Saved JSON & CSV next to:\n{Path(file_path).name}"
        )

if __name__ == "__main__":
    app = DocParserApp()
    app.mainloop()
