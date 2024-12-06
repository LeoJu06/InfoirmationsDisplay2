
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import yaml

def send_email(sender_email, sender_password, recipient_email, subject, body, smtp_server="smtp.gmail.com", smtp_port=587):
    """
    Versendet eine E-Mail mit den angegebenen Parametern.

    :param sender_email: Absender-E-Mail-Adresse
    :param sender_password: Passwort für das E-Mail-Konto des Absenders
    :param recipient_email: Empfänger-E-Mail-Adresse
    :param subject: Betreff der E-Mail
    :param body: Inhalt der E-Mail
    :param smtp_server: SMTP-Server-Adresse (Standard: smtp.gmail.com)
    :param smtp_port: SMTP-Server-Port (Standard: 587)
    """
    try:
        # Erstellen der E-Mail
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Textinhalt hinzufügen
        msg.attach(MIMEText(body, 'plain'))

        # Verbindung zum SMTP-Server herstellen
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Verbindung mit TLS verschlüsseln

        # Anmelden
        server.login(sender_email, sender_password)

        # E-Mail senden
        server.sendmail(sender_email, recipient_email, msg.as_string())

        print("E-Mail wurde erfolgreich gesendet!")

    except Exception as e:
        print(f"Fehler beim Senden der E-Mail: {e}")

    finally:
        # Verbindung zum Server trennen
        server.quit()

# Beispielaufruf der Funktion
# send_email(
#     sender_email="deine.email@gmail.com",
#     sender_password="dein_passwort",
#     recipient_email="empfaenger.email@example.com",
#     subject="Test-E-Mail",
#     body="Das ist eine Testnachricht."
# )

if __name__ == "__main__":


    # Lade die YAML-Datei
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)

    # Hole die Zugangsdaten
    email_credentials = config["email_credentials"]
    leo_mail = email_credentials["email"]
    leos_password = email_credentials["password"]

    # Versende die E-Mail
    recipient_email = leo_mail
    subject = "Mail send from my Raspby"
    body = "Second mail from my raspby"

    send_email(leo_mail, leos_password, recipient_email, subject, body)
