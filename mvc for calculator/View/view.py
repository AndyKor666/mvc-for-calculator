import tkinter as tk

class CalculatorView:
    def bind_add(self, handler): self.btn_add.configure(command=handler)
    def bind_sub(self, handler): self.btn_sub.configure(command=handler)
    def bind_mult(self, handler): self.btn_mult.configure(command=handler)
    def bind_div(self, handler): self.btn_div.configure(command=handler)

    def get_inputs(self) -> tuple[str, str]:
        return self.entry_a.get().strip(), self.entry_b.get().strip()

    def show_result(self, value: float):
        self.result_label.config(text=f"Result: {value:.3f}", fg="darkgreen")

    def show_error(self, message: str):
        self.result_label.config(text=f"ERROR!\n{message}", fg="darkred")

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("MVC Calculator")
        self.root.geometry("420x360+400+120")
        self.root.wm_attributes('-alpha', 0.92)
        self.root.resizable(False, False)
        self.root.configure(bg="#f2f2f2")

        self.title_label = tk.Label(
            self.root, text="CALCULATOR",
            font=("Times New Roman", 12, "bold"), bg="#f2f2f2"
        )
        self.title_label.pack(pady=(16, 8))

        frame=tk.Frame(self.root, bg="#f2f2f2")
        frame.pack(pady=8)

        tk.Label(frame, 
                 text="Input 1st number:", 
                 font=("Times New Roman", 11, "italic"), 
                 bg="#f2f2f2").grid(row=0, 
                                     column=0, 
                                     sticky="e", 
                                     padx=6, 
                                     pady=4
                                     )
        self.entry_a = tk.Entry(frame, 
                                font=("Times New Roman", 12), 
                                width=16, 
                                justify="center"
                                )
        self.entry_a.grid(row=0, column=1, padx=6, pady=4)

        tk.Label(frame, 
                 text="Input 2nd number:", 
                 font=("Times New Roman", 11, "italic"), 
                 bg="#f2f2f2").grid(row=1, 
                                    column=0, 
                                    sticky="e", 
                                    padx=6, 
                                    pady=4
                                    )
        self.entry_b = tk.Entry(frame, 
                                font=("Times New Roman", 12), 
                                width=16, 
                                justify="center"
                                )
        self.entry_b.grid(row=1, column=1, padx=6, pady=4)

        btns=tk.Frame(self.root, bg="#f2f2f2")
        btns.pack(pady=10)

        self.btn_add=tk.Button(btns, 
                               text="+", 
                               font=("Times New Roman", 14, "bold"),
                               width=5
                               )
        self.btn_sub=tk.Button(btns, text="-", 
                               font=("Times New Roman", 14, "bold"), width=5)
        self.btn_mult=tk.Button(btns, 
                                text="*", 
                                font=("Times New Roman", 14, "bold"), 
                                width=5
                                )
        self.btn_div=tk.Button(btns, 
                               text="/", 
                               font=("Times New Roman", 14, "bold"), 
                               width=5
                               )
        self.btn_add.grid(row=0, column=0, padx=6, pady=6)
        self.btn_sub.grid(row=0, column=1, padx=6, pady=6)
        self.btn_mult.grid(row=1, column=0, padx=6, pady=6)
        self.btn_div.grid(row=1, column=1, padx=6, pady=6)
        self.result_label = tk.Label(
            self.root, text="Please, input numbers first.",
            font=("Times New Roman", 12, "bold", "italic"), bg="#f2f2f2", fg="lightgray"
        )
        self.result_label.pack(pady=12)

    def run(self):
        self.root.mainloop()
