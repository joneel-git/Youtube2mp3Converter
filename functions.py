import customtkinter as ctk

def checkbox_event(x):
    # Access the value of the associated variable directly
    current_value = x.get()  # Assuming check_var is accessible here
    if current_value == 1:
        print("Checkbox toggled, current value: ", current_value)
    else:
        print("Checkbox is off, current value: ", current_value)

def entry_input(my_entry, listbox):
    value = my_entry.get()
    collect_data = [value]
    # listbox.insert(END, value)
    for x in collect_data:
        listbox.insert(END, x)
