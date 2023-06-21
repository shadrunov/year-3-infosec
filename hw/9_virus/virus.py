import smtplib as smtp
import socket
import urllib.request

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

public_ip = urllib.request.urlopen("https://ident.me").read().decode("utf8")

email = "shadrunovas@yandex.ru"
password = ""
dest_email = "shadrunovas@gmail.com"
subject = "IP"
email_text = f"Host: {hostname}\nLocal IP: {local_ip}\nPublic IP: {public_ip}"
message = "From: {}\nTo: {}\nSubject: {}\n\n{}".format(
    email, dest_email, subject, email_text
)
server = smtp.SMTP_SSL("smtp.yandex.com")

server.ehlo(email)
server.login(email, password)
server.auth_plain()
server.sendmail(email, dest_email, message)
server.quit()
