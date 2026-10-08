import configparser
import tkinter as tk
import sys
import subprocess
from tkinter import messagebox

config = configparser.ConfigParser()
# Preserve capital letters in key names if present
config.optionxform = str
config.read("config/config.ini")


# Function to validate integer input
def validate_integer(P):
    return P.isdigit() or P == ""


def load_config_to_entries():
    """Populates the entry boxes with existing values from config/config.ini."""
    # [DIRECTORIES] section
    entry1.insert(0, config.get("DIRECTORIES", "BaseDirectory", fallback=""))
    entry2.insert(0, config.get("DIRECTORIES", "SecondDirectory", fallback=""))
    entry3.insert(0, config.get("DIRECTORIES", "ContentDirectory", fallback=""))

    # [INFORMATION] section
    entry5.insert(0, config.get("INFORMATION", "Title", fallback=""))
    entry6.insert(0, config.get("INFORMATION", "Pages", fallback=""))
    entry7.insert(0, config.get("INFORMATION", "Height", fallback=""))
    entry8.insert(0, config.get("INFORMATION", "Width", fallback=""))
    entry9.insert(0, config.get("INFORMATION", "Base", fallback=""))


def save_entry_values():
    """Reads all GUI entries and writes them back to config/config.ini."""
    # Ensure sections exist before writing
    if not config.has_section("DIRECTORIES"):
        config.add_section("DIRECTORIES")
    if not config.has_section("INFORMATION"):
        config.add_section("INFORMATION")

    # Update DIRECTORIES
    config["DIRECTORIES"]["BaseDirectory"] = entry1.get()
    config["DIRECTORIES"]["SecondDirectory"] = entry2.get()
    config["DIRECTORIES"]["ContentDirectory"] = entry3.get()

    # Update INFORMATION
    config["INFORMATION"]["Title"] = entry5.get()
    config["INFORMATION"]["Pages"] = entry6.get()
    config["INFORMATION"]["Height"] = entry7.get()
    config["INFORMATION"]["Width"] = entry8.get()
    config["INFORMATION"]["Base"] = entry9.get()

    # Save changes to config/config.ini
    with open("config/config.ini", "w") as configfile:
        config.write(configfile)

    target_script = "Generator/FileGen.py"

    try:
        # sys.executable uses the same Python interpreter currently running the GUI
        subprocess.run([sys.executable, target_script], check=True)
        messagebox.showinfo("Success", f"Script '{target_script}' executed successfully!""\n""You may now close this window.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Script execution failed with return code {e.returncode}.")
    except FileNotFoundError:
        messagebox.showerror("Error", f"Could not find script file: '{target_script}'")


# ---------------------- Create Main Window ----------------------
root = tk.Tk()
root.title("Configuration Data")
root.minsize(350, 300)

vcmd = root.register(validate_integer)

# Directory Information Section
dLabel = tk.Label(root, text="Directory Information", font=("Arial", 10, "bold"))
bDirect = tk.Label(root, text="Base Directory:")
sDirect = tk.Label(root, text="Second Directory:")
cDirect = tk.Label(root, text="Content Directory:")

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry3 = tk.Entry(root)

# Document Information Section
infoLabel = tk.Label(root, text="Document Information", font=("Arial", 10, "bold"))
titleLabel = tk.Label(root, text="Title of Work:")
pagesLabel = tk.Label(root, text="Number of Pages:")
heightLabel = tk.Label(root, text="Height of Scans:")
widthLabel = tk.Label(root, text="Width of Scans:")
baseLabel = tk.Label(root, text="Base Filename:")

entry5 = tk.Entry(root)
entry6 = tk.Entry(root, validate="key", validatecommand=(vcmd, "%P"))
entry7 = tk.Entry(root, validate="key", validatecommand=(vcmd, "%P"))
entry8 = tk.Entry(root, validate="key", validatecommand=(vcmd, "%P"))
entry9 = tk.Entry(root)

# Save Button
save_button = tk.Button(
    root, text="Save Configuration", width=20, command=save_entry_values
)


# Layout / Grid
dLabel.grid(row=0, column=1, pady=(10, 5))

bDirect.grid(row=1, column=0, sticky="e", padx=5)
sDirect.grid(row=2, column=0, sticky="e", padx=5)
cDirect.grid(row=3, column=0, sticky="e", padx=5)

entry1.grid(row=1, column=1, padx=5, pady=2)
entry2.grid(row=2, column=1, padx=5, pady=2)
entry3.grid(row=3, column=1, padx=5, pady=2)

infoLabel.grid(row=4, column=1, pady=(15, 5))

titleLabel.grid(row=5, column=0, sticky="e", padx=5)
pagesLabel.grid(row=6, column=0, sticky="e", padx=5)
heightLabel.grid(row=7, column=0, sticky="e", padx=5)
widthLabel.grid(row=8, column=0, sticky="e", padx=5)
baseLabel.grid(row=9, column=0, sticky="e", padx=5)

entry5.grid(row=5, column=1, padx=5, pady=2)
entry6.grid(row=6, column=1, padx=5, pady=2)
entry7.grid(row=7, column=1, padx=5, pady=2)
entry8.grid(row=8, column=1, padx=5, pady=2)
entry9.grid(row=9, column=1, padx=5, pady=2)

save_button.grid(row=10, column=1, pady=15)

# Load existing values when app starts
load_config_to_entries()

root.mainloop()