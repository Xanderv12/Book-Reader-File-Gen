import configparser
import sys
import subprocess
import argparse
import os
import tkinter as tk
from tkinter import messagebox

config = configparser.ConfigParser()

configFolder = "config"
configFile = "config.ini"
configPath = os.path.join(configFolder, configFile)
config.optionxform = str

# This function reads the configuration from config.ini, updates it with new values, and then runs the FileGen.py script to generate the necessary files.

def process_config(base_dir, second_dir, content_dir, title, pages, height, width, base):
    """Reads, updates config.ini, and triggers the generator script."""
  
    if os.path.exists(configPath):
        config.read(configPath)

    if not config.has_section("DIRECTORIES"):
        config.add_section("DIRECTORIES")
    if not config.has_section("INFORMATION"):
        config.add_section("INFORMATION")

    # Update DIRECTORIES
    config["DIRECTORIES"]["BaseDirectory"] = base_dir
    config["DIRECTORIES"]["SecondDirectory"] = second_dir
    config["DIRECTORIES"]["ContentDirectory"] = content_dir

    # Update INFORMATION
    config["INFORMATION"]["Title"] = title
    config["INFORMATION"]["Pages"] = pages
    config["INFORMATION"]["Height"] = height
    config["INFORMATION"]["Width"] = width
    config["INFORMATION"]["Base"] = base

    # Save changes
    with open(configPath, "w") as configfile:
        config.write(configfile)

    target_script = "FileGen.py"
    try:
        result = subprocess.run([sys.executable, target_script], check=True, capture_output=True, text=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, f"Script failed with return code {e.returncode}.\nStderr: {e.stderr}"
    except FileNotFoundError:
        return False, f"Could not find script file: '{target_script}'"

# Check if arguments were passed via Command Line (from PHP)
if __name__ == "__main__":
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser(description="CLI Config Updater")
        parser.add_argument("base_dir")
        parser.add_argument("second_dir")
        parser.add_argument("content_dir")
        parser.add_argument("title")
        parser.add_argument("pages")
        parser.add_argument("height")
        parser.add_argument("width")
        parser.add_argument("base")
        
        args = parser.parse_args()
        success, message = process_config(
            args.base_dir, args.second_dir, args.content_dir,
            args.title, args.pages, args.height, args.width, args.base
        )
        print(message)
        sys.exit(0 if success else 1)

# This section is for running the GUI locally on desktop using Tkinter
    else:

        if os.path.exists(configPath):
            config.read(configPath)

        def validate_integer(P):
            return P.isdigit() or P == ""

        def save_entry_values():
            success, message = process_config(
                entry1.get(), entry2.get(), entry3.get(),
                entry5.get(), entry6.get(), entry7.get(), entry8.get(), entry9.get()
            )
            if success:
                messagebox.showinfo("Success", f"Done!\n\n{message}")
            else:
                messagebox.showerror("Error", message)

        root = tk.Tk()
        root.title("Configuration Data")
        root.minsize(350, 300)

        vcmd = root.register(validate_integer)

        # UI layout elements
        dLabel = tk.Label(root, text="Directory Information", font=("Arial", 10, "bold"))
        bDirect = tk.Label(root, text="Base Directory:")
        sDirect = tk.Label(root, text="Second Directory:")
        cDirect = tk.Label(root, text="Content Directory:")

        entry1 = tk.Entry(root)
        entry2 = tk.Entry(root)
        entry3 = tk.Entry(root)

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

        save_button = tk.Button(root, text="Save Configuration", width=20, command=save_entry_values)

        # Grid placement
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
        root.mainloop()