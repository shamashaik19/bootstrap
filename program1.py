# Generate a 6-digit OTP
import random
otp = ''.join(random.choice('0123456789') 
              for _ in range(6))
print("OTP is:", otp)
