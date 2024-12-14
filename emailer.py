import smtplib

email = input("SENDER EMAIL: ")
receiver_email = input("RECEIVER EMAIL: ")
subject = input("Subject: ")
message = input("Message: ")

text = f"Subject: {subject}\n\n{message}"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, "here, enter you *apppassword* from google")

server.sendmail(email, receiver_email, text)

print("Your Email has been sent successfully!")
