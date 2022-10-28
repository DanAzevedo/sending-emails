import smtplib
import ssl
from email.message import EmailMessage
import mimetypes

pass_email = open('pass.txt', 'r').read()
origin_email = 'daniel.danilove@gmail.com'
destiny_email = 'n6_daniel@yahoo.com.br'

assunto = 'Teste de envio de email'
# body = open('corpo_email.txt', 'r').read()
body = open('corpo_email_html.txt', 'r').read()

mensagem = EmailMessage()
mensagem['From'] = origin_email
mensagem['To'] = destiny_email
mensagem['Subject'] = assunto

anexo_path = 'imagem.png'
mime_type, mime_subtype = mimetypes.guess_type(anexo_path)[0].split('/')

mensagem.set_content(body, subtype='html')
# Garantir criptografia SSL
safe = ssl.create_default_context()

with open(anexo_path, 'rb') as ap:
    mensagem.add_attachment(ap.read(), maintype=mime_type,
                            subtype=mime_subtype, filename=anexo_path)

# with Abre e fecha a conexão automaticamente
# Recebe como parâmetro o servidor smtp, a porta e o context=safe
# https://sites.google.com/a/k2automacao.com.br/intranet/suporte/banco-de-dados/outros/listadeservidoressmtp
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(origin_email, pass_email)
    smtp.sendmail(origin_email, destiny_email, mensagem.as_string())
