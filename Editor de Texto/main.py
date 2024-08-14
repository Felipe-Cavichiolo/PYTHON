import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import sys
import io

def get_filetypes():
    types = [
        ["Text Files", "*.txt"],
        ["Python Files", "*.py"],
        ["HTML Files", "*.html"],
        ["JS Files", "*.js"],
        ["CSS Files", "*.css"],
    ]
    ext_list = []
    for i in types:
        ext_list.append(i[1])
    filetypes_ = [("All Files", ext_list)]
    for i in range(len(types)):
        filetypes_.append((types[i][0], types[i][1]))
    return filetypes_

def open_file(window, text):
    filetypes_ = get_filetypes()
    filepath = askopenfilename(filetypes=filetypes_)

    if not filepath:
        return

    text.delete(1.0, tk.END)
    with open(filepath, "r") as file:
        content = file.read()
        text.insert(tk.END, content)
    
    window.title(f"Editor TOPZERA: {filepath}")

def save_file(window, text):
    filetypes_ = get_filetypes()
    filepath = asksaveasfilename(filetypes=filetypes_)

    if not filepath:
        return
    
    with open(filepath, "w") as file:
        content = text.get(1.0, tk.END)
        file.write(content)
    window.title(f"Editor TOPZERA: {filepath}")

def run_code(output_text, code_text):
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()

    try:
        exec(code_text.get(1.0, tk.END), {})
        output = sys.stdout.getvalue()
    except Exception as e:
        output = str(e)
    
    sys.stdout = old_stdout
    
    output_text.insert(tk.END, output)

def create_output_window():
    output_window = tk.Toplevel()
    output_window.title("Output do Código")
    output_window.geometry("800x400")

    output_text = tk.Text(output_window, font="Roboto 14")
    output_text.pack(fill=tk.BOTH, expand=True)

    return output_text

def main():
    window = tk.Tk()
    window.title("Editor TOPZERA do Felóipe")
    window.geometry("1000x700")

    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)

    text_frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    text_frame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

    text_frame.grid_rowconfigure(0, weight=1)
    text_frame.grid_columnconfigure(0, weight=1)

    scrollbar = tk.Scrollbar(text_frame)
    scrollbar.grid(row=0, column=1, sticky="ns")

    text = tk.Text(text_frame, font="Roboto 18 italic", yscrollcommand=scrollbar.set)
    text.grid(row=0, column=0, sticky="nsew")

    scrollbar.config(command=text.yview)

    frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    save_button = tk.Button(frame, text="Salvar", command=lambda: save_file(window, text))
    open_button = tk.Button(frame, text="Abrir", command=lambda: open_file(window, text))
    run_button = tk.Button(frame, text="Rodar Código", command=lambda: run_code(create_output_window(), text))

    save_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    open_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
    run_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
    frame.grid(row=0, column=0, sticky="ns")

    window.bind("<Control-s>", lambda x: save_file(window, text))
    window.bind("<Control-o>", lambda x: open_file(window, text))
    window.bind("<F5>", lambda x: run_code(create_output_window(), text))

    window.mainloop()

main()
