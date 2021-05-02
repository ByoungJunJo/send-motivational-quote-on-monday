import datetime as dt
import smtplib
import random

# Challenge 1: Send a motivational quote via email on the current weekday

# Use the datetime module to obtain the current day of the week
now = dt.datetime.now()
week_day = now.weekday()

# Send this to particular day (i.e 0 = 'Monday' to 6 = 'Sunday')
if week_day == 0:
    # ***WARNING***: Make sure you use a dummy email account to test this out!
    my_email = "YOUR_EMAIL"
    password = "YOUR_EMAIL_PASSWORD"

    with smtplib.SMTP("YOUR_SMTP_ADDRESS", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)

        # Open the quotes.txt file and obtain a list of quotes
        # Use the random module to pick a random quote from your list of quotes
        with open("quotes.txt") as file:
            quote = file.readlines()
            random_quote = random.choice(quote)

        # Write messages
        connection.sendmail(
            from_addr=my_email,
            to_addrs="SEND_TO_THIS_EMAIL",
            msg=f"Subject:Motivational Quote\n\n{random_quote}"
    )