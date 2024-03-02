import customtkinter as ctk


class TaxCalculator:
    def __init__(self):
        
        # Initialize window for the calc
        self.window = ctk.CTk()
        self.window.title("Tax calculator")
        self.window.geometry('300x280')
        self.window.resizable(False, False)
        
        # Options
        self.padding: dict = {'padx': 20, 'pady': 10}

        # initialize labels
        self.income_label = ctk.CTkLabel(self.window, text='Your income: ')
        self.income_label.grid(column=0, row=0, **self.padding)

        self.percent_label = ctk.CTkLabel(self.window, text='Tax percent: ')
        self.percent_label.grid(column=0, row=1, **self.padding)

        self.outcome_label = ctk.CTkLabel(self.window, text='Your Tax: ')
        self.outcome_label. grid(column=0, row=2, **self.padding)

        # Initialize entry

        self.income_entry = ctk.CTkEntry(self.window)
        self.income_entry.grid(column=1, row=0, **self.padding)

        self.percent_entry = ctk.CTkEntry(self.window)
        self.percent_entry.grid(column=1, row=1, **self.padding)

        self.outcome_entry = ctk.CTkEntry(self.window)
        self.outcome_entry.insert(0, "0")
        self.outcome_entry.grid(column=1, row=2, **self.padding)

        # Initialize Button

        self.calculate_button = ctk.CTkButton(self.window, text="Calculate", command=self.calculate_tax)
        self.calculate_button.grid(column=1, row=3, **self.padding)

    def update_result(self, text):
        self.outcome_entry.delete(0, ctk.END)
        self.outcome_entry.insert(0, text)

    def calculate_tax(self):
        try:
            income: float = float(self.income_entry.get())
            percent: float = float(self.percent_entry.get())
            self.update_result(f'{income * percent / 100:,.2f}')
        except ValueError:
            self.update_result("Invalid input")

    def run(self):
        self.window.mainloop()


calculator = TaxCalculator()

calculator.run()
