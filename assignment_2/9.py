#Hack a OTP authentication system using brute force methodology, where OTP is of 4 digits long.

def Hack(Find_OTP):
    num = 1000 #setting to 1000 so it doesn't take value below it
    while num >=1000 and num <= 9999:
        if num == Find_OTP:
            print(f"Match Found:\nOTP: {num}")
            return True
        num += 1 #adding plus one and checking till we find the match
    return False
User_OTP = int(input("Enter A 4 Digit Otp That You Want The Program To Hack: "))
Hack(User_OTP)
