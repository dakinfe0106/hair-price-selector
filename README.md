# Hair Price Selector

## Package/Library Demonstrated

This project demonstrates the Python **`tkinter`** library, including **`tkinter.ttk`**, to build a graphical user interface (GUI). The program also uses Python’s built-in `json` module to load pricing data from a file.

---

## Description

The Hair Price Selector is a Python application that calculates the total cost of hairstyling services for a salon-style business. It allows the user to choose a hairstyle, add optional services, apply a discount when eligible, and view a detailed receipt.

The program is designed to simulate a useful real-world business tool rather than just showing basic GUI widgets. It uses `tkinter` to make the application visual and interactive instead of relying on console input. The code includes GUI widgets, input validation, event-driven behavior, calculations, file handling, and receipt generation. :contentReference[oaicite:1]{index=1}

---

## Purpose

The purpose of this program is to help calculate hair service prices more quickly and consistently. Instead of manually adding service costs, add-ons, discounts, and tax, the program does the calculations automatically and displays a full breakdown for the user.

This could be useful for hairstylists or small salon businesses that want a simple pricing tool.

---

## Features

- Loads pricing data from a `prices.json` file
- Lets the user select a hairstyle from a dropdown menu
- Requires a length only for styles that need it
- Does not require a length for Sew-In, Silk Press, or Cornrows
- Requires a custom description when Cornrows is selected
- Lets the user select multiple add-ons using checkboxes
- Includes a student discount option
- Includes a membership discount option
- Requires proof for discounts:
  - student ID for student discount
  - phone number for membership discount
- Prevents both discounts from being selected at the same time
- Calculates subtotal, discount, tax, and final total
- Displays a receipt with the current date and time
- Includes a Clear button to reset the form
- Includes a Save Receipt button that exports the receipt to a `.txt` file

---

## Files Included

- `main.py` — contains the GUI and program logic
- `prices.json` — stores hairstyle, length, and add-on prices

---

## How to Run

1. Make sure Python 3 is installed on your computer.
2. Download or clone this repository.
3. Make sure `main.py` and `prices.json` are in the same folder.
4. Run the following command in that folder:

```text
python main.py
```

No extra package installation is required because `tkinter` and `json` are included with standard Python installations on most systems.

---

## Sample Input

Example user selections:

- Hairstyle: Cornrows
- Cornrows Description: Small straight-back cornrows with a middle part
- Add-ons: Wash
- Discount: Membership Discount
- Member Phone Number: 5061234567

---

## Sample Output

```text
Hair Price Receipt
----------------------------------
Date/Time: 2026-03-27 15:00:00

Hairstyle: Cornrows
Base Price: $60.00

Cornrows Description: Small straight-back cornrows with a middle part

Length: Not Required
Length Extra: $0.00

Add-ons:
- Wash: $25.00

Add-ons Total: $25.00
Subtotal: $85.00
Discount Type: Membership Discount
Proof Provided: 5061234567
Discount Amount: -$12.75
Tax (15%): $10.84
Final Total: $83.09
```

---

## Why This Program Is Useful

This program is useful because it helps make pricing more accurate and consistent. It reduces the chance of manual calculation mistakes and makes it faster to generate a final total for a customer.

It also includes more realistic business rules, such as:
- requiring proof for discounts
- handling different hairstyle rules
- allowing special descriptions for Cornrows
- saving receipts for later reference

Because of these features, the program goes beyond being just a simple demo and acts more like a small business application.

---

## Future Improvements

Possible future improvements include:

- adding screenshots to the README
- improving the GUI layout further
- adding an admin mode to edit prices
- connecting membership verification to stored customer records
- allowing users to upload inspiration pictures for styles such as Cornrows

---

## Notes

This project was created as a sample program for exploring GUI programming in Python with `tkinter`.
