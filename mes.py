import pandas as pd
from twilio.rest import Client
import time

# Twilio credentials
account_sid = "AC2190a0e21a964a6b5aaf9c2eb8be8e3"
auth_token = "9f40db790d4e7f36b5c3b838c1cd85a8"

client = Client(account_sid, auth_token)

# Read Excel file
df = pd.read_excel("stu.xlsx")

# Message templates
messages = {
    'me': "Good morning ",
    'frd': "Hi da.. how ru",
    'pisasu': "Study Well",
}

# Loop through data
for i in range(len(df)):
    name = df.loc[i, "name"]
    designation = df.loc[i, "designation"]
    number = str(df.loc[i, "number"])

    msg = messages.get(designation.lower(), "Hello!")
    final_message = f"Dear {name}, {msg}"

    client.messages.create(
        from_='whatsapp:+14155238886',
        body=final_message,
        to=f'whatsapp:{number}'
    )

    print(f"Sent to {name} -> {number}")

    time.sleep(1)