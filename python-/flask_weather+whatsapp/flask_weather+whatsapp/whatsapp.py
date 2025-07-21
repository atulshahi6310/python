import pywhatkit as kit
import datetime

# Enter recipient's WhatsApp number (with country code, e.g., +91 for India)
phone_number = '+919335510790'  # <-- Replace with actual number

# Enter the message you want to send
message = 'you have to pay 10k as fine of coming late to class.'

# Get current time
now = datetime.datetime.now()

# Set time to send message (2 minutes later)
hour = now.hour
minute = now.minute + 2

# Send the message
kit.sendwhatmsg(phone_number, message, hour, minute)
