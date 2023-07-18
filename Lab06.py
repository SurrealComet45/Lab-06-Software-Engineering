#------------------------------------------------------------------------------------------------------------
# Student: Orlando A. Gonzalez Pollo
# Course: COP3502C
# Assignment: Lab 06
#-----------------------------------------------------------------------------------------------------------

def encode(password_):
    encode_password = ""
    for num in password_:
        if num.isdigit():
            encoding = str((int(num) + 3) % 10)
            encode_password = encode_password + encoding
    return encode_password

'''<---- EDIT HERE
def decode(enc_digit):
    decoding_output = ""
    for num in str(enc_digit):
        if num.isdigit():
            decoding = str((int(num) - 3) % 10)
            decoding_output = decoding_output + decoding
    return print(f"The encoded password is {enc_digit}, and the original password is {decoding_output}.")
'''

def main():
    function_on = True
    while function_on:
        print("Menu\n-------------\n1. Encode \n2. Decode \n3. Quit\n")
        Menu = int(input("Please enter an option: "))
        if Menu == 1:
            enc = str(input("Please enter your password to encode: "))
            last_password = encode(enc)
            print("Your password has been encoded and stored!\n")
        elif Menu == 2:
            if last_password:
                decode_password = decode(last_password)
            else:
                print("No previous password saved. Please press one to input your password.")
        if Menu == 3:
            break
    function_on = False


try:
    if __name__ == "__main__":
        main()
except:
    raise SystemExit
