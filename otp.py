import pyotp

# create a new OTP instance
otp = pyotp.TOTP('JBSWY3DPEHPK3PXP')

import random
# print the current OTP
print("Current OTP:", otp.now())

# Function to generate OTP
def generateOTP():
    # Declare a string variable to store the OTP
    otp = ""
    
    # Generate a 6-digit OTP
    for i in range(6):
        otp += str(random.randint(0, 9))
    
    # Return the OTP
    return otp

# Function to verify OTP
def verifyOTP(otp, entered_otp):
    if otp == entered_otp:
        return True
    else:
        return False

# Get the mobile number from the user
mobile_number = input("Enter your mobile number: ")

# Generate the OTP
otp = generateOTP()

# Send the OTP to the user's mobile number (You can use any SMS gateway for this)

# Get the OTP entered by the user
entered_otp = input("Enter the OTP sent to your mobile number: ")

# Verify the OTP
if verifyOTP(otp, entered_otp):
    print("OTP verified successfully!")
else:
    print("Invalid OTP, please try again.")
