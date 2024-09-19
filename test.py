# Initialize the dictionary with keys but all values set to None
thisdict = {
    "0001": '0000',
    "0002": '0000',
    "0003": '0000'
}

# Display the dictionary with keys and current (None) values
print("Initial dictionary with all values set to None:")
print(thisdict)

# Ask the user to select which key to update
while True:
    print("\nKeys available:", "  ".join(thisdict.keys()))
    key = input("Select a key to update or type 'done' to finish: ")

    if key.lower() == 'done':
        break
    
    if key in thisdict:
        # Ask for the value to update the selected key
        value = input(f"Enter value for '{key}': ")
        thisdict[key] = value
    else:
        print(f"'{key}' is not a valid key.")

# Display the updated dictionary
print("\nUpdated dictionary:")
print(thisdict)
