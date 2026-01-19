# Enviador de E-mails Automatizado
# Autor: Luiz Augusto Elias Souza Sacramento
# Data: Janeiro/2026

import smtplib
from email.mime.text import MIMEText

def enviar_email(destinatario, assunto, corpo, remetente, senha):
    msg = MIMEText(corpo)
    msg['Subject'] = assunto
    msg['From'] = remetente
    msg['To'] = destinatario
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(remetente, senha)
        server.sendmail(remetente, destinatario, msg.as_string())
        server.quit()
        print("Email enviado!")
    except Exception as e:
        print(f"Erro: {e}")

# Uso real (substitua):
# enviar_email('teste@email.com', 'Teste', 'Olá!', 'seu@gmail.com', 'senha-app')