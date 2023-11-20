import smtplib
from faker import Faker
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def generate_fake_data():
    fake = Faker()
    return {
        'name': fake.name(),
        'email': fake.email(),
        'address': fake.address()
    }

def send_email(receiver_email, subject, body):
    sender_email = "your_email@gmail.com"
    password = "your_password"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.send_message(message)
    server.quit()

def register_client():
    client_data = generate_fake_data()
    send_email(client_data['email'], "Welcome!", "Thanks for registering, " + client_data['name'])
    return client_data
# Genera los datos falsos y envía el correo electrónico
client_data = register_client()

# Imprime los datos del cliente
print(client_data)