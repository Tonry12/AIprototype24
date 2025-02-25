import requests
import json

# API URL
# server_ip = "192.168.10.75"
server_ip = "20.205.17.19"
# url = f'http://{server_ip}:5000/simpleAPI'
url = f'http://{server_ip}/simpleAPI'

# Get user input message
msg = input("Please enter your message: ")

# Predefined recipients and their IP addresses
recipients = {
    "Ploy": "13.75.95.136",
    "tonry": "192.168.10.75"
}

# Allow user to choose an existing recipient or enter a new one
print("\nSelect a recipient to send the message to:")
for i, name in enumerate(recipients.keys(), start=1):
    print(f"{i}. {name} (IP: {recipients[name]})")
print(f"{len(recipients) + 1}. Enter a new recipient and IP manually")

choice = input("Please select a number: ")

if choice.isdigit() and int(choice) in range(1, len(recipients) + 1):
    recipient = list(recipients.keys())[int(choice) - 1]
    ip = recipients[recipient]
else:
    recipient = input("Enter recipient name: ")
    ip = input("Enter recipient's IP: ")

    # Check if the IP already exists
    if ip in recipients.values():
        print("\nThis IP already exists in the system. Skipping to the next step...")
    else:
        recipients[recipient] = ip  # Add to the dictionary

# Sender's name
sender = "Tonnaw"  # You can change this to input() to allow user input

# Create a dictionary for the data to be sent
myobj = {
    'message_key': 'message_val',
    'msg': msg,  # User's message input
    'recipient': recipient,  # Recipient's name
    'ip': ip,  # Recipient's IP
    'sender': sender  # Sender's name
}

# Display the information before sending
print("\nSending message... \n")
print(f"Data to be sent: ")
print(f"----------------------------")
print(f"Sender: {sender}")
print(f"Recipient: {recipient}")
print(f"Recipient's IP: {ip}")
print(f"Message: {msg}")
print(f"----------------------------\n")

# Send POST request
# x = requests.post(url, data=json.dumps(myobj))
x = requests.post(url, json=myobj)

# Check the response and display the result
if x.status_code == 200:
    print(f"Message sent successfully! API response: {x.text}")
else:
    print(f"[ERROR] Message sending failed! Status code: {x.status_code}")
