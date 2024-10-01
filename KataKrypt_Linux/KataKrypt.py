import os
import random
import tkinter as tk
from tkinter import filedialog
import re
import sys
import webbrowser

def generate_keyfile():
    # Generates random 256-bit key
    key = os.urandom(32)  # 32 bytes * 8 bits/byte = 256 bits

    # Prompts user to select where to save the keyfile
    keyfile_path = filedialog.asksaveasfilename(
        title="Save Keyfile As",
        defaultextension=".key",
        filetypes=[("Key Files", "*.key"), ("All Files", "*.*")]
    )
    if not keyfile_path:
        themed_message_box("Error", "No save location selected for keyfile.", "error")
        return None

    # Saves the key to the specified file
    try:
        with open(keyfile_path, 'wb') as keyfile:
            keyfile.write(key)
        themed_message_box("Success", f"Keyfile saved to '{keyfile_path}'.", "info")
        return keyfile_path
    except Exception as e:
        themed_message_box("Error", f"Failed to save keyfile: {e}", "error")
        return None

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and PyInstaller"""
    try:
        # PyInstaller creates a temporary folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Custom themed message box
def themed_message_box(title, message, msg_type="info"):
    # Creates a custom dialog window
    msg_dialog = tk.Toplevel()
    msg_dialog.title(title)
    msg_dialog.geometry("400x200")
    msg_dialog.configure(bg='#2b2b2b')
    msg_dialog.resizable(False, False)

    # Centers the dialog on the screen
    window_width = 400
    window_height = 200
    screen_width = msg_dialog.winfo_screenwidth()
    screen_height = msg_dialog.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    msg_dialog.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    # Icons based on message type
    if msg_type == "info":
        icon = "🛈"  # Information symbol
    elif msg_type == "warning":
        icon = "⚠️"  # Warning symbol
    elif msg_type == "error":
        icon = "❌"  # Error symbol
    else:
        icon = ""

    # Label with the message
    label = tk.Label(msg_dialog, text=f"{icon} {message}", font=('Arial', 12), bg='#2b2b2b', fg='red', wraplength=350)
    label.pack(pady=40)

    # OK button to close the dialog
    ok_button = tk.Button(msg_dialog, text="OK", width=10, command=msg_dialog.destroy, bg='#2b2b2b', fg='red')
    ok_button.pack(pady=10)

    # Make the dialog modal
    msg_dialog.transient(app)
    msg_dialog.grab_set()
    app.wait_window(msg_dialog)

# Ensures the user is using a strong password
def check_password_strength(password):
    strength = 'Strong'
    suggestions = []

    if len(password) < 8:
        strength = 'Weak'
        suggestions.append('Password should be at least 8 characters long.')
    if not re.search(r'[A-Z]', password):
        strength = 'Weak'
        suggestions.append('Include at least one uppercase letter.')
    if not re.search(r'[a-z]', password):
        strength = 'Weak'
        suggestions.append('Include at least one lowercase letter.')
    if not re.search(r'[0-9]', password):
        strength = 'Weak'
        suggestions.append('Include at least one digit.')
    if not re.search(r'[\W_]', password):
        if strength != 'Weak':
            strength = 'Moderate'
        suggestions.append('Include at least one special character.')

    return strength, suggestions

# Custom password input dialog
def get_password():
    # Creates a custom dialog window
    pwd_dialog = tk.Toplevel()
    pwd_dialog.title("Password Input")
    pwd_dialog.geometry("400x200")
    pwd_dialog.configure(bg='#2b2b2b')
    pwd_dialog.resizable(False, False)

    # Centers the dialog on the screen
    window_width = 400
    window_height = 200
    screen_width = pwd_dialog.winfo_screenwidth()
    screen_height = pwd_dialog.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    pwd_dialog.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    # Label and Entry for password
    label = tk.Label(pwd_dialog, text="Enter password:", font=('Arial', 12), bg='#2b2b2b', fg='red')
    label.pack(pady=10)
    password_entry = tk.Entry(pwd_dialog, show='*', width=30, bg='#3b3b3b', fg='red', insertbackground='red')
    password_entry.pack(pady=10)

    # Function to handle password and keyfile submission
def get_password_and_keyfile():
    # Create a custom dialog window
    pwd_dialog = tk.Toplevel()
    pwd_dialog.title("Authentication Input")
    pwd_dialog.geometry("450x400")
    pwd_dialog.configure(bg='#2b2b2b')
    pwd_dialog.resizable(False, False)

    # Center the dialog on the screen
    window_width = 450
    window_height = 400
    screen_width = pwd_dialog.winfo_screenwidth()
    screen_height = pwd_dialog.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    pwd_dialog.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

    # Variables to store user inputs
    use_password = tk.BooleanVar(value=True)
    use_keyfile = tk.BooleanVar(value=False)
    password = tk.StringVar()
    keyfile_path = tk.StringVar()

    # Function to toggle password entry
    def toggle_password():
        if use_password.get():
            password_entry.config(state='normal')
        else:
            password_entry.config(state='disabled')

    # Function to toggle keyfile entry
    def toggle_keyfile():
        if use_keyfile.get():
            keyfile_entry.config(state='normal')
            browse_button.config(state='normal')
            generate_button.config(state='normal')
        else:
            keyfile_entry.config(state='disabled')
            browse_button.config(state='disabled')
            generate_button.config(state='disabled')

    # Password Checkbox
    password_checkbox = tk.Checkbutton(
        pwd_dialog, text="Use Password", variable=use_password, command=toggle_password,
        bg='#2b2b2b', fg='red', activebackground='#2b2b2b', activeforeground='red',
        selectcolor='#2b2b2b'
    )
    password_checkbox.pack(pady=5)

    # Password Entry
    password_entry = tk.Entry(pwd_dialog, show='*', textvariable=password,
                              width=30, bg='#3b3b3b', fg='red', insertbackground='red')
    password_entry.pack(pady=5)

    # Keyfile Checkbox
    keyfile_checkbox = tk.Checkbutton(
        pwd_dialog, text="Use Keyfile", variable=use_keyfile, command=toggle_keyfile,
        bg='#2b2b2b', fg='red', activebackground='#2b2b2b', activeforeground='red',
        selectcolor='#2b2b2b'
    )
    keyfile_checkbox.pack(pady=5)

    # Keyfile Entry Frame
    keyfile_frame = tk.Frame(pwd_dialog, bg='#2b2b2b')
    keyfile_frame.pack(pady=5)

    # Keyfile Entry
    keyfile_entry = tk.Entry(keyfile_frame, textvariable=keyfile_path,
                             width=30, bg='#3b3b3b', fg='red', insertbackground='red', state='disabled')
    keyfile_entry.grid(row=0, column=0, padx=5)

    # Browse Button
    def browse_keyfile():
        path = filedialog.askopenfilename(
            title="Select Keyfile",
            filetypes=[("Key Files", "*.key"), ("All Files", "*.*")]
        )
        if path:
            keyfile_path.set(path)

    browse_button = tk.Button(keyfile_frame, text="Browse", command=browse_keyfile,
                              bg='#2b2b2b', fg='red', state='disabled')
    browse_button.grid(row=0, column=1, padx=5)

    # Generate Keyfile Button
    def generate_and_set_keyfile():
        path = generate_keyfile()
        if path:
            keyfile_path.set(path)
            use_keyfile.set(True)
            toggle_keyfile()

    generate_button = tk.Button(pwd_dialog, text="Generate Keyfile", command=generate_and_set_keyfile,
                                bg='#2b2b2b', fg='red', state='disabled')
    generate_button.pack(pady=5)

    # Function to handle submission
    def submit():
        auth_data = {}
        if use_password.get():
            pwd = password.get()
            if not pwd:
                themed_message_box("Error", "Password is required.", "error")
                return
            else:
                # Checks password strength
                strength, suggestions = check_password_strength(pwd)
                if strength == 'Strong' or strength == 'Moderate':
                    auth_data['password'] = pwd
                else:
                    message = f"Password Strength: {strength}\n"
                    message += "\n".join(suggestions)
                    themed_message_box("Weak Password", message, "warning")
                    return
        if use_keyfile.get():
            kf_path = keyfile_path.get()
            if not kf_path or not os.path.exists(kf_path):
                themed_message_box("Error", "Valid keyfile is required.", "error")
                return
            else:
                with open(kf_path, 'rb') as kf:
                    auth_data['keyfile'] = kf.read()
        if not auth_data:
            themed_message_box("Error", "Please select at least one authentication method.", "error")
            return
        pwd_dialog.destroy()
        get_password_and_keyfile.auth_data = auth_data

    # Submit Button
    submit_button = tk.Button(pwd_dialog, text="Submit", width=10, command=submit,
                              bg='#2b2b2b', fg='red')
    submit_button.pack(pady=10)

    # Cancel Button
    cancel_button = tk.Button(pwd_dialog, text="Cancel", width=10, command=pwd_dialog.destroy,
                              bg='#2b2b2b', fg='red')
    cancel_button.pack()

    # Initialize auth_data
    get_password_and_keyfile.auth_data = None

    # Make the dialog modal
    pwd_dialog.transient(app)
    pwd_dialog.grab_set()
    app.wait_window(pwd_dialog)

    return get_password_and_keyfile.auth_data

# Functions for key generation and encryption
import hashlib

# Generates master key based on sha256 hash of password and/or keyfile
def derive_master_key(password=None, keyfile_data=None):
    hasher = hashlib.sha256()
    if password:
        hasher.update(password.encode('utf-8'))
    if keyfile_data:
        hasher.update(keyfile_data)
    master_key = hasher.digest()
    return master_key

# Linear Congruential Generator to generate a pseudorandom sequence from the master key
def generate_lcg_sequence_from_key(key, length):
    modulus = 256
    multiplier = 1103515245
    increment = 12345
    # Use the key to derive an initial seed
    seed = int.from_bytes(key[:4], byteorder='big')
    sequence = []
    current = seed
    for _ in range(length):
        current = (multiplier * current + increment) % modulus
        sequence.append(current)
    return sequence

# Custom hybrid encryption function with fixed-pattern dynamic key updates
def hybrid_encrypt(data, master_key):
    # Generate keystream from master key
    keystream = generate_lcg_sequence_from_key(master_key, len(data))

    # Step 1: Stream Cipher XOR
    xor_data = bytearray(data[i] ^ keystream[i] for i in range(len(data)))

    # Step 2: Block Cipher Transformation
    block_size = 16
    encrypted_data = bytearray()
    num_blocks = (len(xor_data) + block_size - 1) // block_size

    # Generate subkeys from master key
    subkeys = generate_lcg_sequence_from_key(master_key, block_size)

    for block_num in range(num_blocks):
        block_start = block_num * block_size
        block_end = min(block_start + block_size, len(xor_data))
        block = xor_data[block_start:block_end]

        # Substitution
        substituted_block = bytearray()
        for i in range(len(block)):
            s_box = (subkeys[i % len(subkeys)] + i) % 256
            substituted_byte = block[i] ^ s_box
            substituted_block.append(substituted_byte)

        # Permutation
        permutation_pattern = sorted(range(len(substituted_block)), key=lambda k: subkeys[k % len(subkeys)])
        permuted_block = bytearray(substituted_block[i] for i in permutation_pattern)

        encrypted_data.extend(permuted_block)

        # Dynamic Key Update based on fixed pattern
        for i in range(len(subkeys)):
            subkeys[i] = (subkeys[i] + block_num + 1) % 256  # Update subkeys

    return encrypted_data

# Custom hybrid decryption function with fixed-pattern dynamic key updates
def hybrid_decrypt(data, master_key):
    # Generate keystream from master key
    keystream = generate_lcg_sequence_from_key(master_key, len(data))

    # Step 1: Inverse Block Cipher Transformation
    block_size = 16
    decrypted_data = bytearray()
    num_blocks = (len(data) + block_size - 1) // block_size

    subkeys = generate_lcg_sequence_from_key(master_key, block_size)

    for block_num in range(num_blocks):
        block_start = block_num * block_size
        block_end = min(block_start + block_size, len(data))
        block = data[block_start:block_end]

        # Inverse Permutation
        permutation_pattern = sorted(range(len(block)), key=lambda k: subkeys[k % len(subkeys)])
        inverse_permutation = [0] * len(block)
        for i, p in enumerate(permutation_pattern):
            inverse_permutation[p] = i

        permuted_block = bytearray(block[inverse_permutation[i]] for i in range(len(block)))

        # Inverse Substitution
        substituted_block = bytearray()
        for i in range(len(permuted_block)):
            s_box = (subkeys[i % len(subkeys)] + i) % 256
            substituted_byte = permuted_block[i] ^ s_box
            substituted_block.append(substituted_byte)

        decrypted_data.extend(substituted_block)

        # Dynamic Key Update based on fixed pattern
        for i in range(len(subkeys)):
            subkeys[i] = (subkeys[i] + block_num + 1) % 256  # Update subkeys

    # Step 2: Stream Cipher XOR
    original_data = bytearray(decrypted_data[i] ^ keystream[i] for i in range(len(decrypted_data)))

    return original_data

# Function to embed data into a BMP image using LSB steganography
def embed_data_in_bmp(cover_image_path, data, output_image_path):
    with open(cover_image_path, 'rb') as f:
        bmp_data = bytearray(f.read())

    # Verifies BMP format
    if bmp_data[0:2] != b'BM':
        themed_message_box("Error", "Unsupported file format.")
        return False

    # Gets pixel data offset from the header
    pixel_data_offset = int.from_bytes(bmp_data[10:14], byteorder='little')
    max_data_length = (len(bmp_data) - pixel_data_offset) // 8 - 4  # Subtract 4 bytes for data length

    if len(data) > max_data_length:
        themed_message_box("Error", "Data too large to embed in the provided image.")
        return False

    # Embeds data length first (4 bytes)
    data_length = len(data)
    length_bytes = data_length.to_bytes(4, byteorder='big')
    data_to_embed = length_bytes + data

    data_index = 0
    for i in range(pixel_data_offset, len(bmp_data)):
        if data_index >= len(data_to_embed) * 8:
            break
        # Gets the current bit from data_to_embed
        byte_index = data_index // 8
        bit_index = 7 - (data_index % 8)
        current_bit = (data_to_embed[byte_index] >> bit_index) & 1

        # Modifies the LSB of the pixel byte
        bmp_data[i] = (bmp_data[i] & 0xFE) | current_bit

        data_index += 1

    with open(output_image_path, 'wb') as f:
        f.write(bmp_data)
    return True

# Function to extract data from a BMP image
def extract_data_from_bmp(stego_image_path):
    with open(stego_image_path, 'rb') as f:
        bmp_data = bytearray(f.read())

    if bmp_data[0:2] != b'BM':
        themed_message_box("Error", "Unsupported file format.")
        return None

    pixel_data_offset = int.from_bytes(bmp_data[10:14], byteorder='little')

    # Extracts data length first (4 bytes)
    data_index = 0
    length_bytes = bytearray(4)
    for _ in range(4 * 8):  # 4 bytes * 8 bits
        byte_index = data_index // 8
        bit_index = 7 - (data_index % 8)
        bit = bmp_data[pixel_data_offset + data_index] & 1
        length_bytes[byte_index] |= bit << bit_index
        data_index += 1

    data_length = int.from_bytes(length_bytes, byteorder='big')

    # Extracts the actual data
    data = bytearray(data_length)
    for _ in range(data_length * 8):
        byte_index = (data_index - 32) // 8  # Subtract 32 bits (4 bytes) used for length
        bit_index = 7 - ((data_index - 32) % 8)
        bit = bmp_data[pixel_data_offset + data_index] & 1
        data[byte_index] |= bit << bit_index
        data_index += 1

    return data

# Encryption function with steganography
def encrypt_file_with_steganography(input_file, auth_data):
    bmp_folder = resource_path('bmp_images')

    if not os.path.exists(bmp_folder):
        themed_message_box("Error", f"BMP folder '{bmp_folder}' not found.", "error")
        return

    bmp_files = [f for f in os.listdir(bmp_folder) if f.lower().endswith('.bmp')]

    if not bmp_files:
        themed_message_box("Error", f"No BMP files found in the folder '{bmp_folder}'.", "error")
        return

    cover_image = os.path.join(bmp_folder, random.choice(bmp_files))

    output_image = filedialog.asksaveasfilename(
        title="Save encrypted BMP image as",
        defaultextension=".bmp",
        filetypes=[("BMP Files", "*.bmp"), ("All Files", "*.*")]
    )
    if not output_image:
        themed_message_box("Error", "No save location selected.", "error")
        return

    with open(input_file, 'rb') as f_in:
        data = f_in.read()

    master_key = derive_master_key(
        password=auth_data.get('password'),
        keyfile_data=auth_data.get('keyfile')
    )

    encrypted_data = hybrid_encrypt(data, master_key)

    success = embed_data_in_bmp(cover_image, encrypted_data, output_image)
    if success:
        themed_message_box("Success", f"Data embedded successfully into '{output_image}'.\nCover image used: '{os.path.basename(cover_image)}'", "info")
    else:
        themed_message_box("Error", "Failed to embed data.", "error")

# Decryption function with file selection and password prompt after file selection
def decrypt_file_from_steganography(stego_image, auth_data):
    output_file = filedialog.asksaveasfilename(
        title="Save decrypted file as",
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not output_file:
        themed_message_box("Error", "No save location selected.", "error")
        return

    extracted_data = extract_data_from_bmp(stego_image)
    if extracted_data is None:
        themed_message_box("Error", "Failed to extract data.", "error")
        return
    
    master_key = derive_master_key(
        password=auth_data.get('password'),
        keyfile_data=auth_data.get('keyfile')
    )

    decrypted_data = hybrid_decrypt(extracted_data, master_key)

    with open(output_file, 'wb') as f_out:
        f_out.write(decrypted_data)

    themed_message_box("Success", f"Data extracted and decrypted successfully into '{output_file}'.", "info")

# Function to handle encryption action
def encrypt_action():
    input_file = filedialog.askopenfilename(title="Select the text file to encrypt")
    if not input_file:
        themed_message_box("Error", "No file selected.", "error")
        return

    auth_data = get_password_and_keyfile()
    if auth_data is None:
        return

    encrypt_file_with_steganography(input_file, auth_data)

# Function to handle decryption action
def decrypt_action():
    stego_image = filedialog.askopenfilename(title="Select the BMP image to decrypt", filetypes=[("BMP Files", "*.bmp")])
    if not stego_image:
        themed_message_box("Error", "No file selected.", "error")
        return

    auth_data = get_password_and_keyfile()
    if auth_data is None:
        return

    decrypt_file_from_steganography(stego_image, auth_data)

# Function to show the About information
def show_about_info():
    themed_message_box("About", "KataKrypt\nVersion 1.0\n© 2024")

# Function to open the Help file
def open_help_file():
    help_file_path = resource_path('help.html')
    if not os.path.exists(help_file_path):
        themed_message_box("Error", "Help file not found.")
        return

    # Convert the file path to a file URI
    help_uri = 'file://' + os.path.abspath(help_file_path)

    # Open the help file in the default web browser
    webbrowser.open(help_uri)

def confirm_exit():
    # Create a custom dialog window
    exit_dialog = tk.Toplevel()
    exit_dialog.title("Pls don't go :(")
    exit_dialog.geometry("300x150")
    exit_dialog.configure(bg='#2b2b2b')
    exit_dialog.resizable(False, False)

    # Center the dialog on the screen
    window_width = 300
    window_height = 150
    screen_width = exit_dialog.winfo_screenwidth()
    screen_height = exit_dialog.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    exit_dialog.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    # Label with the confirmation message
    label = tk.Label(exit_dialog, text="Meow to exit KataKombs...MUAHAHA", font=('Arial', 12), bg='#2b2b2b', fg='red')
    label.pack(pady=20)

    # Frame for the buttons
    button_frame = tk.Frame(exit_dialog, bg='#2b2b2b')
    button_frame.pack(pady=10)

    # "Meow" button
    yes_button = tk.Button(button_frame, text="MEOW", width=10, command=lambda: exit_program(exit_dialog), bg='#2b2b2b', fg='red')
    yes_button.grid(row=0, column=0, padx=10)

    # "No" button
    no_button = tk.Button(button_frame, text="Errrm No", width=10, command=exit_dialog.destroy, bg='#2b2b2b', fg='red')
    no_button.grid(row=0, column=1, padx=10)

    # Disable the main window while the dialog is open
    exit_dialog.transient(app)
    exit_dialog.grab_set()
    app.wait_window(exit_dialog)

# Function to handle exiting the program after confirmation
def exit_program(dialog):
    dialog.destroy()
    # Second dialog to say bye to the user
    thank_you_dialog = tk.Toplevel()
    thank_you_dialog.title("Toodles")
    thank_you_dialog.geometry("300x150")
    thank_you_dialog.configure(bg='#2b2b2b')
    thank_you_dialog.resizable(False, False)

    # Center the dialog on the screen
    window_width = 300
    window_height = 150
    screen_width = thank_you_dialog.winfo_screenwidth()
    screen_height = thank_you_dialog.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    thank_you_dialog.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    # Label with the goodbye message
    label = tk.Label(thank_you_dialog, text="You meow'd at your PC", font=('Arial', 12), bg='#2b2b2b', fg='red')
    label.pack(pady=40)

    # Function to close the application after the dialog is closed
    def close_app():
        thank_you_dialog.destroy()
        app.quit()

    # Button to close the program
    ok_button = tk.Button(thank_you_dialog, text="I have no shame", width=15, command=close_app, bg='#2b2b2b', fg='red')
    ok_button.pack(pady=10)

    # Disable the main window while the dialog is open
    thank_you_dialog.transient(app)
    thank_you_dialog.grab_set()
    app.wait_window(thank_you_dialog)

# Main function to run the program
def main():
    global app  # Declare app as global so it can be accessed in other functions
    app = tk.Tk()
    app.title("KataKrypt")
    app.geometry("400x200")
    app.resizable(False, False)
    app.configure(bg='#2b2b2b')  # Dark gray background

    # Set the font and colors
    font_style = ('Fixedsys', 30)
    fg_color = 'red'  # Red text color

    # Create the menu bar
    menu_bar = tk.Menu(app, bg='#2b2b2b', fg=fg_color)

    # File menu
    file_menu = tk.Menu(menu_bar, tearoff=0, bg='#2b2b2b', fg=fg_color)
    file_menu.add_command(label="Encrypt", command=encrypt_action)
    file_menu.add_command(label="Decrypt", command=decrypt_action)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=confirm_exit)
    menu_bar.add_cascade(label="File", menu=file_menu)

    # Help menu
    help_menu = tk.Menu(menu_bar, tearoff=0, bg='#2b2b2b', fg=fg_color)
    help_menu.add_command(label="Help", command=open_help_file)
    help_menu.add_command(label="About", command=show_about_info)
    menu_bar.add_cascade(label="Help", menu=help_menu)

    app.config(menu=menu_bar)

    # Create a title label
    title_label = tk.Label(app, text="KataKrypt", font=font_style, bg='#2b2b2b', fg=fg_color)
    title_label.pack(pady=20)

    # Create a frame for buttons
    button_frame = tk.Frame(app, bg='#2b2b2b')
    button_frame.pack(pady=10)

    # Create Encrypt button
    encrypt_button = tk.Button(button_frame, text="Encrypt", width=15, command=encrypt_action, bg='#2b2b2b', fg=fg_color)
    encrypt_button.grid(row=0, column=0, padx=10)

    # Create Decrypt button
    decrypt_button = tk.Button(button_frame, text="Decrypt", width=15, command=decrypt_action, bg='#2b2b2b', fg=fg_color)
    decrypt_button.grid(row=0, column=1, padx=10)

    # Create Exit button
    exit_button = tk.Button(app, text="Exit", width=10, command=confirm_exit, bg='#2b2b2b', fg=fg_color)
    exit_button.pack(pady=10)

    app.mainloop()

if __name__ == "__main__":
    main()
