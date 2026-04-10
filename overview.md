# Package/Library Overview: tkinter

## 1. Which package/library did I select?

For this exploration activity, I selected **`tkinter`**, which is Python’s standard interface for building graphical user interfaces (GUIs). In my project, I also used **`tkinter.ttk`** for styled widgets such as dropdown menus. `tkinter` allowed me to build an interactive business application instead of a text-only console program. [1][2]

---

## 2. What is the package/library?

`tkinter` is the standard Python interface to the **Tk GUI toolkit**. It is used to create desktop applications with windows, buttons, labels, text boxes, menus, and other interface elements. Python’s documentation describes it as the standard way to access Tk from Python, and it is available on Windows, macOS, and most Unix platforms. [1]

The purpose of `tkinter` is to let programmers create programs that users can interact with visually instead of only through typed console input. This makes it useful for forms, simple desktop tools, calculators, data-entry programs, and small business applications. In my project, I used it to create a salon pricing tool where the user selects hairstyles, lengths, add-ons, and discounts through a GUI.

### How do you use it?

To use `tkinter`, you first import it into a Python program, create a main window, add widgets, and then start the event loop. The event loop keeps the window open and listens for actions such as button clicks or dropdown selections. [1][3]

A very small example looks like this:

```python
import tkinter as tk

window = tk.Tk()
window.title("Example App")

label = tk.Label(window, text="Hello, world!")
label.pack()

window.mainloop()
```

In addition to the base `tkinter` widgets, I used `ttk` widgets in my program. The `tkinter.ttk` module provides themed widgets, which help make the interface look more modern and separate widget behavior from appearance. [2]

---

## 3. What are the functionalities of the package/library?

`tkinter` includes many useful features for GUI development. In my project, I explored several of them.

### a) Creating a main application window

The first thing a `tkinter` program needs is a main window. This is the base container for the whole application.

```python
window = tk.Tk()
window.title("Hair Price Selector")
window.geometry("720x800")
```

This creates the main program window and sets its title and size.

---

### b) Using labels, entry boxes, and buttons

I used labels to describe each part of the form, entry boxes for text input, and buttons for actions like calculating the total, clearing the form, and saving the receipt.

```python
title_label = tk.Label(window, text="Hair Price Selector", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

student_id_entry = tk.Entry(left_frame, width=28)
student_id_entry.pack(pady=3)

price_button = tk.Button(button_frame, text="Calculate Total", command=show_price, width=15)
price_button.pack(side="left", padx=5)
```

These widgets helped turn the program into a real form-based application.

---

### c) Using dropdown menus with `ttk.Combobox`

One of the most useful parts of my project was the dropdown menu for selecting hairstyles and lengths.

```python
selected_style = tk.StringVar()
style_dropdown = ttk.Combobox(left_frame, textvariable=selected_style, state="readonly", width=25)
style_dropdown["values"] = list(hairstyles.keys())
style_dropdown.pack(pady=5)
```

This allowed the user to choose from existing options instead of typing them manually, which reduces errors and makes the interface easier to use.

---

### d) Checkboxes for add-ons and discounts

I used checkboxes so the user could select optional services and discount types.

```python
student_discount_var = tk.BooleanVar()

student_discount_checkbox = tk.Checkbutton(
    left_frame,
    text="Student Discount (10% off subtotal)",
    variable=student_discount_var
)
student_discount_checkbox.pack(anchor="w")
```

This made the application more interactive and helped simulate how a real salon tool might work.

---

### e) Event-driven programming

One important part of `tkinter` is that it is **event-driven**. This means the program reacts to user actions, such as clicking a button or choosing an item from a dropdown. [3]

In my project, when the hairstyle changes, the program updates which fields should be enabled or disabled.

```python
style_dropdown.bind("<<ComboboxSelected>>", update_style_fields)
```

This helped me create special cases:
- **Box Braids** requires a length
- **Sew-In** and **Silk Press** do not require a length
- **Cornrows** does not require a length, but it does require a description

This feature made the program feel more realistic and showed how GUI programs can adapt based on user choices.

---

### f) Displaying output in a `Text` widget

I used a `Text` widget to display the receipt. This was useful because the final output is multiple lines long.

```python
receipt_text = tk.Text(right_frame, width=42, height=30)
receipt_text.pack(pady=10)
```

Then I updated it with the calculated receipt after the user clicked the button.

Example output from the program:

```text
Hair Price Receipt
----------------------------------
Date/Time: 2026-04-10 18:30:12

Hairstyle: Box Braids
Base Price: $120.00
Length: Medium
Length Extra: $30.00

Add-ons:
- Wash: $25.00
- Hair Included: $30.00

Add-ons Total: $55.00
Subtotal: $205.00
Discount Type: Student Discount
Proof Provided: 12345678
Discount Amount: -$20.50
Tax (15%): $27.68
Final Total: $212.18
```

This output is useful because it clearly shows the customer how the final total was calculated.

---

### g) Input validation

Another important functionality in my project was validating user input before calculating the result. For example, the program checks whether:
- a hairstyle was selected
- a length was selected when needed
- a cornrows description was entered
- only one discount was selected
- a student ID or phone number was entered when needed

A simplified example is:

```python
if student_discount_var.get() and membership_discount_var.get():
    display_receipt("Please select only one discount type.")
    return
```

This improved the program because it prevented invalid combinations and made the tool behave more like a real application.

---

### h) Saving output to a text file

My program also lets the user save the receipt to a `.txt` file.

```python
filename = f"receipt_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

with open(filename, "w") as file:
    file.write(receipt_content)
```

This was a useful feature because it gives the application a more practical business purpose.

---

## 4. When was it created?

`tkinter` is Python’s interface to Tk, and Tk itself was created by **John Ousterhout in the late 1980s**. Over time, Tk became widely used for GUI development across multiple programming languages, including Python. [4]

---

## 5. Why did I select this package/library?

I selected `tkinter` because I wanted to explore GUI programming in Python and build something that felt practical instead of only academic. A salon pricing calculator was a good fit because it naturally involves user interaction, selecting options, checking conditions, and displaying results clearly.

I also chose `tkinter` because it is included with Python in many installations, so I did not need to set up a complicated external framework. That made it a realistic package to explore within the time limits of this project. It also let me focus on learning GUI design, widget behavior, and event handling.

---

## 6. How did learning the package/library influence my learning of the language?

Learning `tkinter` changed how I think about Python programs. Before this project, I mostly thought of Python as something used for console input/output, calculations, and file handling. With `tkinter`, I learned that Python can also be used to build interactive desktop applications.

This project also helped me better understand:
- **event-driven programming**, because the program waits for user actions
- **state management**, because widget states change depending on selections
- **modular logic**, because the GUI and pricing rules need to work together
- **data-driven design**, because pricing information is loaded from JSON instead of being hard-coded everywhere

Overall, learning `tkinter` made Python feel more flexible to me. It showed me that the language can be used not only for scripts and console programs, but also for applications with real user interfaces.

---

## 7. How was my overall experience with the package/library?

My overall experience with `tkinter` was positive. It was easier to start with than I expected because creating a basic window and simple widgets is straightforward. At the same time, I also learned that GUI programming takes more planning than a console program because I had to think about layout, user flow, validation, and what should happen when specific events occur.

I would recommend `tkinter` to someone who:
- wants to build a small or medium-sized desktop application
- is learning GUI programming for the first time
- wants a Python-based solution without installing a large framework

I would especially recommend it for beginner-friendly tools such as calculators, data-entry forms, schedulers, and business utilities.

I would continue using `tkinter` for small desktop applications and prototypes. For larger or more advanced-looking applications, I might also explore other GUI frameworks in the future. Still, `tkinter` was a very good choice for this project because it let me create a useful, interactive application while keeping the code understandable.

---

## References

[1] Python Software Foundation. “`tkinter` — Python interface to Tcl/Tk.” Python Documentation. https://docs.python.org/3/library/tkinter.html

[2] Python Software Foundation. “`tkinter.ttk` — Tk themed widgets.” Python Documentation. https://docs.python.org/3/library/tkinter.ttk.html

[3] Mark Roseman. “TkDocs Tutorial.” TkDocs. https://tkdocs.com/tutorial/

[4] Tcl/Tk Wiki. “Tk Sets The Standard.” https://wiki.tcl.tk/36888
