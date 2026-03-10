# ==========================================
# PROJECT: Personal Information Manager
# AUTHOR: [Your Name]
# DESCRIPTION: A simple Python script to store,
#              calculate, and display user data.
# ==========================================

# --- STEP 1: WELCOME MESSAGE ---
print("=" * 40)
print("    PERSONAL INFORMATION MANAGER")
print("=" * 40)

# --- STEP 2: STATIC VARIABLES ---
# These are "hard-coded" pieces of information
name = "Vidya S"
age = 21
city = "karnataka"
hobby = "spending time at the beach"

# --- STEP 3: DYNAMIC USER INPUT ---
print("\nPlease tell me a bit more about yourself:")
print("-" * 30)

# Get favorite food and ensure it's not empty
favorite_food = input("What's your favorite food? ").strip()
while not favorite_food:
    print("Oops! This field cannot be empty.")
    favorite_food = input("What's your favorite food? ").strip()

# Get favorite color and ensure it's not empty
favorite_color = input("What's your favorite color? ").strip()
while not favorite_color:
    print("Oops! This field cannot be empty.")
    favorite_color = input("What's your favorite color? ").strip()

# --- STEP 4: MATH LOGIC ---
# Calculate age in months (Basic math operation)
age_in_months = age * 12

# --- STEP 5: FORMATTED OUTPUT ---
# Using f-strings to inject variables into text
print("\n" + "=" * 40)
print("        USER PROFILE SUMMARY")
print("=" * 40)

print(f"NAME          : {name}")
print(f"LOCATION      : {city}")
print(f"AGE           : {age} years old ({age_in_months} months)")
print(f"HOBBY         : {hobby}")
print(f"FAVORITE FOOD : {favorite_food}")
print(f"FAVORITE COLOR: {favorite_color}")

# --- STEP 6: GOODBYE MESSAGE ---
print("\n" + "=" * 40)
print("   Data saved successfully. Goodbye!")
print("=" * 40)
