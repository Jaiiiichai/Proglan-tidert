memoryAddress= [
    {"0000": "+0000", "0001": "+0000", "0002": "+0000","0003": "+0000","0004": "+0000","0005": "+0000","0006": "+0000","0007": "+0000","0008": "+0000","0009": "+0000"},
    {"0010": "+0000", "0011": "+0000", "0012": "+0000","0013": "+0000","0014": "+0000","0015": "+0000","0016": "+0000","0017": "+0000","0018": "+0000","0019": "+0000"},
    {"0020": "+0000", "0021": "+0000", "0022": "+0000","0023": "+0000","0024": "+0000","0025": "+0000","0026": "+0000","0027": "+0000","0028": "+0000","0029": "+0000"},
    {"0030": "+0000", "0031": "+0000", "0032": "+0000","0033": "+0000","0034": "+0000","0035": "+0000","0036": "+0000","0037": "+0000","0038": "+0000","0039": "+0000"},
    {"0040": "+0000", "0041": "+0000", "0042": "+0000","0043": "+0000","0044": "+0000","0045": "+0000","0046": "+0000","0047": "+0000","0048": "+0000","0049": "+0000"},
    {"0050": "+0000", "0051": "+0000", "0052": "+0000","0053": "+0000","0054": "+0000","0055": "+0000","0056": "+0000","0057": "+0000","0058": "+0000","0059": "+0000"},
    {"0060": "+0000", "0061": "+0000", "0062": "+0000","0063": "+0000","0064": "+0000","0065": "+0000","0066": "+0000","0067": "+0000","0068": "+0000","0069": "+0000"},
    {"0070": "+0000", "0071": "+0000", "0072": "+0000","0073": "+0000","0074": "+0000","0075": "+0000","0076": "+0000","0077": "+0000","0078": "+0000","0079": "+0000"},
    {"0080": "+0000", "0081": "+0000", "0082": "+0000","0083": "+0000","0084": "+0000","0085": "+0000","0086": "+0000","0087": "+0000","0088": "+0000","0089": "+0000"},
    {"0090": "+0000", "0091": "+0000", "0092": "+0000","0093": "+0000","0094": "+0000","0095": "+0000","0096": "+0000","0097": "+0000","0098": "+0000","0099": "+0000"},

]

def print_memory_addresses():
    counter = 0 
    print(' ',end=" ")
    # Print numbers from 1 to 9 on the same line    
    # Print numbers from 0 to 9 with the first number having 15 characters of space to the left
    for i in range(10):
        print(f"", end="") 
            # Print the number 0 with 15 characters of space to the left
        print(f"{i:>11}", end="")

    print()
   
    for d in memoryAddress:
        print(f"{counter:02}    ", end=" ") 
        values = [str(value) for value in d.values()]
        print("      ".join(values))
        
        counter += 10
    counter = 0
    
def update_address():
    # Ask the user for the address and new value
    address = input("Enter the address to update (e.g., '0001'): ")
    new_value = input("Enter the new value (e.g., '+1234'): ")
    
    # Flag to check if the address was found and updated
    address_updated = False
    
    # Iterate over each dictionary in the list
    for dictionary in memoryAddress:
        if address in dictionary:
            dictionary[address] = new_value  # Update the value for the given address
            address_updated = True
            break  # Exit the loop once the address is found and updated

    if address_updated:
        print("\nAddress updated successfully.")
    else:
        print("\nAddress not found.")

    # Print the updated list of dictionaries
    print("\nUpdated memory address list:")
    print_memory_addresses()



print_memory_addresses()
update_address()

