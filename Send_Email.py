import smtplib , ssl

host = "smtp.gmail.com"
port = 465
context = ssl.create_default_context()


username = "amirmoradisa1381@gmail.com"
password = "iumhbbrzsdtomyto"
receiver = "amir1381ssss@gmail.com"
message = """\
Subject:Hi!
How are you?
bye!"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)