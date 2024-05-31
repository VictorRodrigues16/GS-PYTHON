import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_email(email):

    corpo = f'''
A preservação do oceano é crucial para a manutenção da vida na Terra. Os oceanos cobrem cerca de 71% da superfície do planeta e são responsáveis por produzir mais de metade do oxigênio que respiramos. Além disso, eles desempenham um papel fundamental na regulação do clima, absorvendo grandes quantidades de dióxido de carbono e calor. A biodiversidade marinha, que inclui milhões de espécies, muitas ainda desconhecidas, depende de ambientes oceânicos saudáveis para prosperar. Sem uma ação consciente para proteger esses ecossistemas, corremos o risco de perder não apenas espécies valiosas, mas também os benefícios ecológicos e econômicos que os oceanos proporcionam.

A poluição marinha é um dos maiores desafios ambientais que enfrentamos hoje. Plásticos, produtos químicos, resíduos industriais e esgoto doméstico são apenas alguns dos poluentes que contaminam nossos mares. Estes resíduos não apenas prejudicam a vida marinha, causando a morte de peixes, tartarugas e aves marinhas, mas também afetam diretamente a saúde humana. Microplásticos, por exemplo, entraram na cadeia alimentar, com potenciais efeitos adversos ainda não totalmente compreendidos. É essencial que governos, indústrias e indivíduos adotem práticas sustentáveis para reduzir a entrada de poluentes nos oceanos.

Adotar medidas para proteger o oceano não é apenas uma questão ambiental, mas também econômica. Economias inteiras dependem dos recursos marinhos, seja através da pesca, do turismo ou do transporte marítimo. A degradação dos oceanos compromete esses setores, ameaçando a subsistência de milhões de pessoas ao redor do mundo. Investir em práticas de pesca sustentável, controlar a poluição e promover o turismo responsável são passos fundamentais para assegurar que os oceanos continuem a ser uma fonte vital de riqueza e emprego.

A conscientização pública e a educação são ferramentas poderosas na luta pela preservação dos oceanos. Campanhas educativas podem informar as pessoas sobre o impacto de suas ações diárias e incentivar comportamentos mais responsáveis. Reduzir o uso de plásticos descartáveis, optar por produtos sustentáveis e apoiar políticas públicas que visam a proteção do ambiente marinho são atitudes que cada um pode adotar para contribuir com a causa. Apenas através de um esforço coletivo e contínuo podemos garantir que os oceanos permaneçam saudáveis para as gerações futuras.

'''


    smtp_host = 'smtp-mail.outlook.com'
    smtp_porta = 587
    usuario = 'oceanguard20@hotmail.com'
    senha = 'ocean2024'

    remetente = 'oceanguard20@hotmail.com'
    destinatario = email
    assunto = 'Para um Futuro mais Azul'

    mensagem = MIMEMultipart()
    mensagem['From'] = remetente
    mensagem['To'] = destinatario
    mensagem['Subject'] = assunto

    mensagem.attach(MIMEText(corpo, 'plain'))

    with smtplib.SMTP(smtp_host, smtp_porta) as servidor_smtp:
        servidor_smtp.starttls()
        servidor_smtp.login(usuario, senha)
        servidor_smtp.sendmail(remetente, destinatario, mensagem.as_string())

    print('E-mail enviado com sucesso!')


