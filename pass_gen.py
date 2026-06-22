import streamlit as cb
import random
import string

# Set up page configuration
cb.set_page_config(page_title="Strong Password Generator", page_icon="🔐", layout="centered")

# Title and description
cb.title("🔐 Strong Password Generator")
cb.write("Customize and generate a secure password instantly.")

cb.markdown("---")

# User Inputs (Sidebar or Main Page)
cb.subheader("Configure your password")

length = cb.slider("Password Length", min_value=6, max_value=32, value=12, step=1)

# Checkboxes for character sets
include_uppercase = cb.checkbox("Include Uppercase Letters (A-Z)", value=True)
include_lowercase = cb.checkbox("Include Lowercase Letters (a-z)", value=True)
include_numbers = cb.checkbox("Include Numbers (0-9)", value=True)
include_symbols = cb.checkbox("Include Symbols (@, #, $, etc.)", value=True)

# Function to generate password
def generate_password(length, use_upper, use_lower, use_nums, use_syms):
    char_pool = ""
    
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_nums:
        char_pool += string.digits
    if use_syms:
        char_pool += string.punctuation

    # Edge case: If no checkboxes are selected
    if not char_pool:
        return None

    # Generate a random password from the pool
    return "".join(random.choice(char_pool) for _ in range(length))

cb.markdown("---")

# Generate Button
if cb.button("Generate Password", type="primary"):
    password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_symbols)
    
    if password:
        cb.success("Password Generated Successfully!")
        
        # Display the password in a code block so users can easily click the built-in copy button
        cb.code(password, language="text")
        cb.info("💡 You can copy the password using the copy icon in the top-right corner of the box above.")
    else:
        cb.error("Please select at least one character set option to generate a password.")
