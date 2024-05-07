import tkinter as tk

# Get the Tcl/Tk version from the Tcl interpreter
tcl_version = tk.Tk().eval('info patchlevel')

print("Tcl/Tk version:", tcl_version)

