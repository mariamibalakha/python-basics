
import tkinter as tk
from tkinter import messagebox


class VendingMachineFSM:
    PRICE = 50
    ACCEPTED_COINS = (10, 20)

    def __init__(self, root):
        self.root = root
        self.root.title("Vending Machine - FSM Simulator")
        self.root.geometry("450x480")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f3f5")

        # Current balance and machine state
        self.current_state = 0

        self.create_widgets()
        self.update_ui()

    def create_widgets(self):
        # Title
        self.title_label = tk.Label(
            self.root,
            text="Vending Machine (FSM)",
            font=("Helvetica", 17, "bold"),
            bg="#f0f3f5",
            fg="#2c3e50"
        )
        self.title_label.pack(pady=(20, 10))

        # Instructions
        self.info_label = tk.Label(
            self.root,
            text=(
                f"Drink price: {self.PRICE} tetri\n"
                "Accepted coins: 10 and 20 tetri"
            ),
            font=("Helvetica", 11),
            bg="#f0f3f5",
            fg="#7f8c8d"
        )
        self.info_label.pack(pady=5)

        # Status panel
        self.status_frame = tk.Frame(
            self.root,
            bg="white",
            highlightbackground="#bdc3c7",
            highlightthickness=1
        )
        self.status_frame.pack(fill="x", padx=35, pady=20)

        self.state_label = tk.Label(
            self.status_frame,
            font=("Helvetica", 14, "bold"),
            bg="white",
            fg="#2980b9"
        )
        self.state_label.pack(pady=(15, 8))

        self.msg_label = tk.Label(
            self.status_frame,
            font=("Helvetica", 10),
            bg="white",
            fg="#7f8c8d",
            wraplength=340
        )
        self.msg_label.pack(pady=(0, 15))

        # Coin buttons
        self.btn_frame = tk.Frame(self.root, bg="#f0f3f5")
        self.btn_frame.pack(pady=5)

        self.btn_10 = tk.Button(
            self.btn_frame,
            text="+10 tetri",
            font=("Helvetica", 12, "bold"),
            bg="#3498db",
            fg="white",
            activebackground="#2980b9",
            width=12,
            height=2,
            command=lambda: self.insert_coin(10)
        )
        self.btn_10.grid(row=0, column=0, padx=8)

        self.btn_20 = tk.Button(
            self.btn_frame,
            text="+20 tetri",
            font=("Helvetica", 12, "bold"),
            bg="#2ecc71",
            fg="white",
            activebackground="#27ae60",
            width=12,
            height=2,
            command=lambda: self.insert_coin(20)
        )
        self.btn_20.grid(row=0, column=1, padx=8)

        # Reset button
        self.btn_reset = tk.Button(
            self.root,
            text="Cancel / Return Balance",
            font=("Helvetica", 10),
            bg="#95a5a6",
            fg="white",
            width=24,
            command=self.reset_machine
        )
        self.btn_reset.pack(pady=18)

        # Footer
        self.footer_label = tk.Label(
            self.root,
            text="Python GUI Project | Finite State Machine",
            font=("Helvetica", 9),
            bg="#f0f3f5",
            fg="#7f8c8d"
        )
        self.footer_label.pack(side="bottom", pady=10)

    def insert_coin(self, coin):
        # Validate the coin
        if coin not in self.ACCEPTED_COINS:
            return

        old_state = self.current_state
        self.current_state += coin

        # Check whether the target amount has been reached
        if self.current_state >= self.PRICE:
            change = self.current_state - self.PRICE

            self.update_ui(
                message="Drink dispensed successfully!",
                color="#27ae60"
            )

            messagebox.showinfo(
                "Transaction Complete",
                f"Your drink is ready!\n"
                f"Price: {self.PRICE} tetri\n"
                f"Change: {change} tetri"
            )

            # Start a new transaction
            self.current_state = 0
            self.update_ui(
                message="Ready for the next transaction.",
                color="#2980b9"
            )

        else:
            self.update_ui(
                message=(
                    f"State transition: {old_state} -> "
                    f"{self.current_state}"
                ),
                color="#2980b9"
            )

    def update_ui(self, message=None, color="#2980b9"):
        self.state_label.config(
            text=f"Current balance: {self.current_state} tetri",
            fg=color
        )

        if message is None:
            message = "Please insert a coin."

        self.msg_label.config(text=message)

    def reset_machine(self):
        # Return the inserted balance in the simulation
        refund = self.current_state
        self.current_state = 0

        self.update_ui(
            message="Transaction cancelled. Machine is ready.",
            color="#e67e22"
        )

        if refund > 0:
            messagebox.showinfo(
                "Transaction Cancelled",
                f"Transaction cancelled.\n"
                f"Refund amount: {refund} tetri"
            )
        else:
            messagebox.showinfo(
                "Vending Machine",
                "The machine has been reset."
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = VendingMachineFSM(root)
    root.mainloop()
