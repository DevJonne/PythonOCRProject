import pytesseract
import cv2
import requests
import time
import numpy as np
import pyautogui

# Configuração do pytesseract (ajuste o caminho se necessário)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Função para traduzir o texto usando a API VLibras
def traduzir_para_libras(texto):
    url = 'https://api.gov.br/vlibras/v1/translate'  # URL do endpoint de tradução
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
        response = requests.post(url, json=data)  # Use json=data para enviar como JSON
        if response.status_code == 200:
            video_id = response.json().get('id')
            print("ID do vídeo gerado:", video_id)
        else:
            print("Erro ao gerar vídeo:", response.status_code)
    except Exception as e:
        print("Erro:", str(e))

# Função para capturar o texto sob o cursor do mouse
def capturar_texto_do_mouse():
    while True:
        # Obtém a posição do mouse
        x, y = pyautogui.position()

        # Captura uma imagem da tela
        screenshot = pyautogui.screenshot()

        # Converte a imagem para um array do OpenCV
        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # Define a região da captura ao redor do cursor (por exemplo, 100x30 pixels)
        width, height = 100, 30
        roi = frame[y:y+height, x:x+width]

        # Extrai texto da região de interesse
        texto = pytesseract.image_to_string(roi, lang='por')
        print("Texto capturado:", texto)

        if texto:
            traduzir_para_libras(texto)

        # Aguarda um segundo antes da próxima captura
        time.sleep(1)

        # Pressione 'q' para sair do loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Inicia a captura de texto
capturar_texto_do_mouse()
