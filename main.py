import smtplib
from email.message import EmailMessage

try:
    
    servidor_email = smtplib.SMTP('smtp.office365.com', 587)
    servidor_email.starttls()

    servidor_email.login('seu_email', 'sua_senha')
    
    print('Coloque o e-mail destinatário:')
    x = input()
    print('Digite o login do usuário:')
    y = input()

    msg = EmailMessage()
    msg['Subject'] = 'assunto'
    msg['From'] = 'seu_email'
    msg['To'] = x
    msg.set_content('conteudo')

    servidor_email.send_message(msg)

except Exception as e:
    print(f"Erro ao enviar email: {e}")

finally:
    servidor_email.quit
