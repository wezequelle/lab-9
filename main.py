#William Ezequelle
def encoder(password):
    encoding = ""
    for i in password:
        temp_encoding = int(i)
        temp_encoding += 3
        temp_encoding %= 10
        temp_encoding = str(temp_encoding)
        encoding += temp_encoding
    return encoding

def main():
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            pass_encode = encoder(password)
            print("Your password has been encoded and stored!")
        elif option == 2: #TODO:implement decode function into main
            #pass_decode = decoder(pass_encode)
            #print(f"The encoded password is {pass_encode}, and the original password is {pass_decode}.")
            pass
        elif option == 3:
            break


if __name__ == "__main__":
    main()