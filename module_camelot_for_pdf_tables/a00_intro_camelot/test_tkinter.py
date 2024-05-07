import tkinter as tk

def on_button_click():
    label.config(text="Button clicked!")

# Create the main window
root = tk.Tk()
root.title("Tkinter Test App")

# Create a label
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=20)

# Create a button
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()

# Start the Tkinter event loop
root.mainloop()

