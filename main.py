import tkinter as tk


root = tk.Tk()
root.title("rekenmachine")  # Hier kun je je naam gebruiken


first_number = None
second_number = None
math_operation = None

# Functie om de cijfers op het invoerveld te plaatsen
def button_click(number):
    current = ingave.get()
    ingave.delete(0, tk.END)  # Verwijder het huidige cijfer
    ingave.insert(0, current + str(number))

# Functie om een bewerking toe te voegen
def set_operation(operation):
    global first_number, math_operation
    first_number = int(ingave.get())  # Het eerste getal wordt opgeslagen
    math_operation = operation
    ingave.delete(0, tk.END)  # Het invoerveld wordt leeggemaakt

# Functie om het resultaat te berekenen
def calculate():
    global first_number, second_number, math_operation
    second_number = int(ingave.get())  # Het tweede getal wordt opgeslagen
    ingave.delete(0, tk.END)  # Het invoerveld wordt leeggemaakt

    # Resultaat afhankelijk van de bewerking
    if math_operation == "addition":
        ingave.insert(0, first_number + second_number)
    elif math_operation == "subtraction":
        ingave.insert(0, first_number - second_number)
    elif math_operation == "multiplication":
        ingave.insert(0, first_number * second_number)
    elif math_operation == "division":
        if second_number != 0:
            ingave.insert(0, first_number / second_number)
        else:
            ingave.insert(0, "Error")

# Functie om het invoerveld te wissen
def clear():
    ingave.delete(0, tk.END)
