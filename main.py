import pytesseract
import cv2
import requests
import time
"""
Configuração para o pytesseract (assumindo que está instalado no Windows)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
"""

# Função para capturar a tela e reconhecer texto usando OCR
def capturar_texto_da_tela():
# Captura a tela inteira
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) # Para uma webcam ou fonte de vídeo

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Converte a imagem para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Extrai texto da imagem
    texto = pytesseract.image_to_string(gray, lang='por')
    print("Texto capturado:", texto)

    if texto:
        traduzir_para_libras(texto)

    # Aguarda 2 segundos antes de capturar novamente
    time.sleep(2)

    # Pressione 'q' para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
# Função para traduzir o texto usando a API VLibras
def traduzir_para_libras(texto):
url = 'https://api.gov.br/vlibras/v1/translate' # URL do endpoint de tradução
params = {'text': texto}

try:
    response = requests.get(url, params=params)
    if response.status_code == 200:
        glosa = response.json()  # Recebe a glosa de Libras
        print("Tradução para Libras (Glosa):", glosa)
        gerar_video(glosa)
    else:
        print("Erro ao traduzir para Libras:", response.status_code)
except Exception as e:
    print("Erro:", str(e))
# Função para gerar o vídeo com o avatar da Libras
def gerar_video(glosa):
url = 'https://api.gov.br/vlibras/v1/video'
data = {'gloss': glosa}

try:
    response = requests.post(url, data=data)
    if response.status_code == 200:
        video_id = response.json().get('id')
        print("ID do vídeo gerado:", video_id)
        # Aqui você pode fazer o download do vídeo ou verificar o status
    else:
        print("Erro ao gerar vídeo:", response.status_code)
except Exception as e:
    print("Erro:", str(e))

capturar_texto_da_tela()
