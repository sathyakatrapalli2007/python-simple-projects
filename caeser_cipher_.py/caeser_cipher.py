msg=input("enter a string:")
key=int(input("enter a shift number:"))
choice=input("Encrypt/Decrypt:")
new_msg=""
for char in msg:
    if choice.lower()=="encrypt":
        if char.isalpha():
            if char.isupper():
                start_index=65
            else:
                start_index=97
            code=ord(char)
            temp_code=(code-start_index+key)%26
            new_code=temp_code+start_index
            new_msg+=chr(new_code)
    elif choice.lower()=="decrypt":
        if char.isalpha():
            if char.islower():
                start_index=65
            else:
                start_index=97
            code=ord(char)
            temp_code=(code-start_index-key)%26
            new_code=start_index+temp_code
            new_msg+=chr(temp_code)
    else:
        new_msg+=char

print(new_msg)
