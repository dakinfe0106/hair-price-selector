import tkinter as tk
from tkinter import ttk
import json
from datetime import datetime

# load prices from json file
with open("prices.json", "r") as file:
    prices = json.load(file)

# split data into sections
hairstyles = prices["hairstyles"]
lengths = prices["lengths"]
addons = prices["addons"]

TAX_RATE = 0.15
STUDENT_DISCOUNT_RATE = 0.10
MEMBERSHIP_DISCOUNT_RATE = 0.15

# styles that do not need a length selection
NO_LENGTH_STYLES = ["Sew-In", "Silk Press", "Cornrows"]

# create main window
window = tk.Tk()
window.title("Hair Price Selector")
window.geometry("720x800")

# title
title_label = tk.Label(window, text="Hair Price Selector", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

# main frame
main_frame = tk.Frame(window)
main_frame.pack(pady=10, padx=15, fill="both", expand=True)

# left frame for inputs
left_frame = tk.Frame(main_frame)
left_frame.pack(side="left", padx=20, fill="y")

# right frame for receipt
right_frame = tk.Frame(main_frame)
right_frame.pack(side="right", padx=20, fill="both", expand=True)

# hairstyle
style_label = tk.Label(left_frame, text="Select a hairstyle:")
style_label.pack(anchor="w")

selected_style = tk.StringVar()
style_dropdown = ttk.Combobox(left_frame, textvariable=selected_style, state="readonly", width=25)
style_dropdown["values"] = list(hairstyles.keys())
style_dropdown.pack(pady=5)

# length
length_label = tk.Label(left_frame, text="Select hair length:")
length_label.pack(anchor="w", pady=(10, 0))

selected_length = tk.StringVar()
length_dropdown = ttk.Combobox(left_frame, textvariable=selected_length, state="readonly", width=25)
length_dropdown["values"] = list(lengths.keys())
length_dropdown.pack(pady=5)

# cornrows description
cornrows_desc_label = tk.Label(left_frame, text="Cornrows Description:")
cornrows_desc_label.pack(anchor="w", pady=(10, 0))

cornrows_desc_entry = tk.Entry(left_frame, width=28)
cornrows_desc_entry.pack(pady=3)

# add-ons
addons_label = tk.Label(left_frame, text="Select add-ons:")
addons_label.pack(anchor="w", pady=(10, 0))

addon_vars = {}
for addon in addons:
    addon_vars[addon] = tk.BooleanVar()
    checkbox = tk.Checkbutton(
        left_frame,
        text=f"{addon} (+${addons[addon]})",
        variable=addon_vars[addon]
    )
    checkbox.pack(anchor="w")

# discounts section
discounts_label = tk.Label(left_frame, text="Discount Options:")
discounts_label.pack(anchor="w", pady=(15, 0))

student_discount_var = tk.BooleanVar()
membership_discount_var = tk.BooleanVar()

student_discount_checkbox = tk.Checkbutton(
    left_frame,
    text="Student Discount (10% off subtotal)",
    variable=student_discount_var
)
student_discount_checkbox.pack(anchor="w")

student_id_label = tk.Label(left_frame, text="Student ID:")
student_id_label.pack(anchor="w", pady=(5, 0))

student_id_entry = tk.Entry(left_frame, width=28)
student_id_entry.pack(pady=3)

membership_discount_checkbox = tk.Checkbutton(
    left_frame,
    text="Membership Discount (15% off subtotal)",
    variable=membership_discount_var
)
membership_discount_checkbox.pack(anchor="w", pady=(10, 0))

member_phone_label = tk.Label(left_frame, text="Member Phone Number:")
member_phone_label.pack(anchor="w", pady=(5, 0))

member_phone_entry = tk.Entry(left_frame, width=28)
member_phone_entry.pack(pady=3)

# receipt area
receipt_title = tk.Label(right_frame, text="Receipt", font=("Arial", 14, "bold"))
receipt_title.pack()

receipt_text = tk.Text(right_frame, width=42, height=30)
receipt_text.pack(pady=10)
receipt_text.insert("1.0", "Your receipt will appear here.")
receipt_text.config(state="disabled")

# helper to show message in receipt box
def display_receipt(message):
    receipt_text.config(state="normal")
    receipt_text.delete("1.0", tk.END)
    receipt_text.insert("1.0", message)
    receipt_text.config(state="disabled")

# update fields depending on hairstyle
def update_style_fields(event=None):
    style = selected_style.get()

    if style in NO_LENGTH_STYLES:
        selected_length.set("")
        length_dropdown.config(state="disabled")
    else:
        length_dropdown.config(state="readonly")

    if style == "Cornrows":
        cornrows_desc_entry.config(state="normal")
    else:
        cornrows_desc_entry.delete(0, tk.END)
        cornrows_desc_entry.config(state="disabled")

# connect hairstyle selection to update function
style_dropdown.bind("<<ComboboxSelected>>", update_style_fields)

# start with cornrows field disabled
cornrows_desc_entry.config(state="disabled")

# function to calculate and display receipt
def show_price():
    style = selected_style.get()
    length = selected_length.get()
    cornrows_description = cornrows_desc_entry.get().strip()
    student_id = student_id_entry.get().strip()
    member_phone = member_phone_entry.get().strip()

    if style not in hairstyles:
        display_receipt("Please select a hairstyle.")
        return

    # validate length only when needed
    if style not in NO_LENGTH_STYLES and length not in lengths:
        display_receipt("Please select a hair length for this hairstyle.")
        return

    # validate cornrows description
    if style == "Cornrows" and cornrows_description == "":
        display_receipt("Please enter a description for the cornrows style.")
        return

    # prevent both discounts at the same time
    if student_discount_var.get() and membership_discount_var.get():
        display_receipt("Please select only one discount type.")
        return

    # validate student discount
    if student_discount_var.get() and student_id == "":
        display_receipt("Please enter a student ID to use the student discount.")
        return

    # validate membership discount
    if membership_discount_var.get():
        cleaned_phone = "".join(char for char in member_phone if char.isdigit())
        if member_phone == "":
            display_receipt("Please enter a phone number to use the membership discount.")
            return
        if len(cleaned_phone) != 10:
            display_receipt("Please enter a valid 10-digit phone number for membership discount.")
            return

    base_price = hairstyles[style]

    if style in NO_LENGTH_STYLES:
        length_used = "Not Required"
        length_price = 0
    else:
        length_used = length
        length_price = lengths[length]

    selected_addons = []
    addons_total = 0

    for addon in addon_vars:
        if addon_vars[addon].get():
            selected_addons.append((addon, addons[addon]))
            addons_total += addons[addon]

    subtotal = base_price + length_price + addons_total

    discount_type = "None"
    proof_used = "N/A"
    discount_rate = 0

    if student_discount_var.get():
        discount_type = "Student Discount"
        proof_used = student_id
        discount_rate = STUDENT_DISCOUNT_RATE
    elif membership_discount_var.get():
        discount_type = "Membership Discount"
        proof_used = member_phone
        discount_rate = MEMBERSHIP_DISCOUNT_RATE

    discount_amount = subtotal * discount_rate
    discounted_subtotal = subtotal - discount_amount
    tax_amount = discounted_subtotal * TAX_RATE
    final_total = discounted_subtotal + tax_amount

    if selected_addons:
        addons_lines = "\n".join([f"- {addon}: ${price:.2f}" for addon, price in selected_addons])
    else:
        addons_lines = "None"

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cornrows_section = ""
    if style == "Cornrows":
        cornrows_section = f"\nCornrows Description: {cornrows_description}\n"

    receipt_output = (
        "Hair Price Receipt\n"
        "----------------------------------\n"
        f"Date/Time: {current_time}\n\n"
        f"Hairstyle: {style}\n"
        f"Base Price: ${base_price:.2f}\n"
        f"{cornrows_section}\n"
        f"Length: {length_used}\n"
        f"Length Extra: ${length_price:.2f}\n\n"
        f"Add-ons:\n{addons_lines}\n\n"
        f"Add-ons Total: ${addons_total:.2f}\n"
        f"Subtotal: ${subtotal:.2f}\n"
        f"Discount Type: {discount_type}\n"
        f"Proof Provided: {proof_used}\n"
        f"Discount Amount: -${discount_amount:.2f}\n"
        f"Tax (15%): ${tax_amount:.2f}\n"
        f"Final Total: ${final_total:.2f}\n"
    )

    display_receipt(receipt_output)

# function to save receipt to txt file
def save_receipt():
    receipt_content = receipt_text.get("1.0", tk.END).strip()

    if receipt_content == "" or receipt_content == "Your receipt will appear here.":
        display_receipt("Please calculate a receipt before saving.")
        return

    filename = f"receipt_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w") as file:
        file.write(receipt_content)

    display_receipt(receipt_content + f"\n\nReceipt saved as: {filename}")

# function to clear everything
def clear_all():
    selected_style.set("")
    selected_length.set("")
    length_dropdown.config(state="readonly")

    cornrows_desc_entry.config(state="normal")
    cornrows_desc_entry.delete(0, tk.END)
    cornrows_desc_entry.config(state="disabled")

    student_discount_var.set(False)
    membership_discount_var.set(False)
    student_id_entry.delete(0, tk.END)
    member_phone_entry.delete(0, tk.END)

    for addon in addon_vars:
        addon_vars[addon].set(False)

    display_receipt("Your receipt will appear here.")

# buttons
button_frame = tk.Frame(left_frame)
button_frame.pack(pady=15)

price_button = tk.Button(button_frame, text="Calculate Total", command=show_price, width=15)
price_button.pack(side="left", padx=5)

clear_button = tk.Button(button_frame, text="Clear", command=clear_all, width=10)
clear_button.pack(side="left", padx=5)

save_button = tk.Button(left_frame, text="Save Receipt", command=save_receipt, width=15)
save_button.pack(pady=5)

window.mainloop()
