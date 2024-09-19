# src/notifications/sistema_alerta.py

import smtplib
from email.mime.text import MIMEText

def enviar_alerta_estoque(codigo_produto, quantidade_atual):
    mensagem = MIMEText(f"O estoque do produto {codigo_produto} está baixo. Quantidade atual: {quantidade_atual}")
    mensagem['Subject'] = f"Alerta de Estoque - {codigo_produto}"
    mensagem['From'] = 'estoque@marizardomotopecas.com'
    mensagem['To'] = 'gerente@marizardomotopecas.com'

    try:
        with smtplib.SMTP('smtp.exemplo.com') as servidor:
            servidor.login('estoque@marizardomotopecas.com', 'senha')
            servidor.send_message(mensagem)
        print(f"Alerta de estoque enviado para o produto {codigo_produto}.")
    except Exception as e:
        print(f"Erro ao enviar alerta de estoque: {e}")
