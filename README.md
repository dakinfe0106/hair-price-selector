# Hair Price Selector

## Description

The Hair Price Selector is a Python application that helps calculate the total cost of different hairstyles for a salon. The program allows users to select a hairstyle, choose add-ons, apply discounts, and view a detailed receipt. It uses a graphical user interface (GUI) built with tkinter, making it easy and interactive to use.

## Features

* Loads all pricing data from a JSON file
* Allows the user to select a hairstyle using a dropdown menu
* Requires a hair length only for styles that need it, such as Box Braids
* Does not require a length for Sew-In, Silk Press, or Cornrows
* Requires a custom description when Cornrows is selected
* Allows the user to choose multiple add-ons using checkboxes
* Includes a student discount option
* Includes a membership discount option
* Requires proof for discounts:

  * student ID for student discount
  * phone number for membership discount
* Prevents both discounts from being used at the same time
* Calculates subtotal, discount, tax, and final total
* Displays a receipt with date and time
* Includes a clear button to reset the program
* Includes a Save Receipt button that exports the receipt to a `.txt` file

## Installation

1. Make sure Python is installed on your computer
2. Download or clone this repository
3. Make sure the following files are in the same folder:

   * main.py
   * prices.json

## How to Run

Run the program using:

```text
python main.py
```

## Sample Input and Output

### Sample Input

* Hairstyle: Cornrows
* Cornrows Description: Small straight-back cornrows with a middle part
* Add-ons: Wash
* Discount: Membership Discount
* Member Phone Number: 5061234567

### Sample Output

## Hair Price Receipt

Date/Time: 2026-03-27 15:00:00

Hairstyle: Cornrows
Base Price: $60.00

Cornrows Description: Small straight-back cornrows with a middle part

Length: Not Required
Length Extra: $0.00

Add-ons:

* Wash: $25.00

Add-ons Total: $25.00
Subtotal: $85.00
Discount Type: Membership Discount
Proof Provided: 5061234567
Discount Amount: -$12.75
Tax (15%): $10.84
Final Total: $83.09

## Usefulness

This program can be useful for hairstylists or small salon businesses because it helps keep pricing more consistent and reduces manual errors. It also makes the process faster by automatically calculating totals, discounts, and tax. Requiring proof for discounts and allowing special handling for styles like Cornrows makes the application feel more realistic as a business tool.

## Program Structure

* `main.py` → contains the GUI and program logic
* `prices.json` → stores all pricing data (hairstyles, lengths, add-ons)
* Receipt saving → exports receipts as `.txt` files with timestamps

## Future Improvements

* Add screenshots to the README
* Improve the GUI layout further
* Add an admin mode to edit prices
* Connect membership verification to stored records
* Allow users to upload inspiration pictures for styles such as Cornrows

