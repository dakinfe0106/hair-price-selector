# Overview

## What is the purpose of this program?
The purpose of this program is to create a business-style application that helps calculate the price of hairstyling services. It allows users to select a hairstyle, add optional services, apply discounts, and receive a detailed receipt. The goal is to simulate a real-world salon pricing tool while practicing Python programming and GUI development.

## Why did I choose this topic?
I chose this topic because it connects programming to a real-life business scenario. Many salons have different pricing depending on style, length, and extra services, and this project allowed me to model that logic in code. It also gave me a chance to build something practical and interactive instead of just a basic console program.

## What language and tools did I use?
- Python (main programming language)
- tkinter (for building the graphical user interface)
- JSON (for storing price data)

## How is tkinter used in my project?
In my project, `tkinter` is used to build the full interface of the Hair Price Selector application. The program includes:
- a dropdown menu for hairstyle selection
- a dropdown menu for length selection when needed
- a text entry field for custom Cornrows descriptions
- checkboxes for add-ons
- checkboxes for discount type
- entry boxes for student ID and membership phone number
- buttons for calculating the total and clearing the form
- a receipt area using a `Text` widget

This allows the user to interact with the application visually and receive a full price breakdown. It also shows conditional behavior in the GUI, because some hairstyles need different inputs than others.

## How does the program work?
The program loads pricing data from a JSON file, which includes hairstyles, lengths, and add-ons. The user interacts with the GUI by selecting options and entering any required information. When the "Calculate Total" button is pressed, the program:
- validates user input
- applies special rules depending on the hairstyle
- calculates subtotal, discounts, and tax
- displays a detailed receipt

Some hairstyles require different inputs. For example:
- Box Braids requires a length selection
- Sew-In and Silk Press do not require length
- Cornrows requires a custom description

## Reflection
Working with `tkinter` helped me understand how event-driven GUI programs differ from regular console programs. In a console program, the user usually types input step by step in order. In this project, the user interacts with visual controls, and the program responds when buttons are clicked.

One thing I learned is that GUI programming takes more planning than I expected. I had to think about layout, input validation, and how the widgets connect to the program logic. For example, different hairstyles do not all need the same inputs. Box Braids needs a length selection, while Sew-In and Silk Press do not. Cornrows needed a special case where the customer can type a description. Adding these rules made the program feel more realistic.

I also added discount proof fields so the application would feel more like a real business tool. However, instead of building a full customer database, I kept the scope reasonable by validating that the proof fields were entered correctly. I think this was a good design decision because it made the program more realistic without becoming too complicated.

A future improvement I identified would be allowing users to upload inspiration pictures for styles such as Cornrows. I did not implement that in this version because it would require additional file handling and interface design, but it would make the application even more useful in a real salon setting.

Overall, `tkinter` was a good choice for this project because it let me make a useful and interactive business application while still keeping the code understandable.
