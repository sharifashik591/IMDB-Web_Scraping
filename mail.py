import smtplib
import pandas as pd
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Create a DataFrame

def send_email(receaver_mail,df):

        csv_file = df.to_csv(index=False)
        # Set up the email message
        msg = MIMEMultipart()
        msg['From'] = 'sharif16-247@diu.edu.bd'
        msg['To'] = receaver_mail
        msg['Subject'] = 'Subject of the email'
        body = 'Dataframe is attached below'
        msg.attach(MIMEText(body, 'plain'))

        # Attach the CSV file
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((csv_file).encode())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename=example.csv")
        msg.attach(part)

        # Log in to your Gmail account
        email_user = 'sharif16-247@diu.edu.bd'
        email_password = '1234#$'
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_user, email_password)

        # Send the email
        text = msg.as_string()
        server.sendmail(email_user, receaver_mail, text)
        server.quit()

        print('Email sent successfully.')

