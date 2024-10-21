#PythonOCRProject
Explicação:

Captura de texto com OCR: A função capturar_texto_da_tela() usa a webcam ou a tela para capturar imagens e extrair o texto em português.
Tradução para Libras: O texto capturado é enviado para a API VLibras usando o endpoint /translate.
Geração de vídeo: Após obter a glosa (tradução em Libras), o código envia o conteúdo para o endpoint /video para gerar o vídeo de tradução em Libras.

Pré-requisitos:

Tesseract OCR: Certifique-se de ter o Tesseract OCR instalado no sistema.

Bibliotecas Python: Instale as bibliotecas necessárias com o comando:

pip install pytesseract opencv-python requests
