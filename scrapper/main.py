import cv2
import numpy as np
from difflib import SequenceMatcher
import easyocr
import pytesseract

# Carregar a imagem
image = cv2.imread('image4.png')

# Pré-processamento
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.equalizeHist(gray)
gray = cv2.medianBlur(gray, 3)

# Threshold adaptativo
thresh = cv2.adaptiveThreshold(
    gray, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY, 11, 2
)

# Operações morfológicas
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))
thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# ROI
altura, largura = thresh.shape
roi = thresh[int(altura*0.7):altura, 0:largura]

cv2.imwrite('imagem_pre_processada.png', roi)

# Usando EasyOCR
reader = easyocr.Reader(['pt'])
resultados = reader.readtext(roi)

texto_extraido = ' '.join([res[1] for res in resultados])

# Aplicar OCR usando Pytesseract
# config = '--oem 3 --psm 6'  # Ajuste conforme necessário
# texto_extraido = pytesseract.image_to_string(roi, config=config, lang='por')

# Limpar o texto extraído
texto_extraido = texto_extraido.strip().lower()

print("Texto extraido: ", texto_extraido)

# Filtrar o texto
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

tecnicas_conhecidas = [
    'Esgrima por Dentro',
    'Elevação de Quadril',
    'Reposição da Guarda',
    'Levantada Técnica',
    'Bloqueio do soco e chutes traseiros',
    'Pedaladas nos Joelhos',
    'Puxar o Quadril do Oponente'
]

texto_extraido = texto_extraido.strip().lower()

melhor_tecnica = ''
maior_similaridade = 0

for tecnica in tecnicas_conhecidas:
    sim = similar(texto_extraido, tecnica.lower())
    if sim > maior_similaridade:
        maior_similaridade = sim
        melhor_tecnica = tecnica
        
print("Similaridade: ", maior_similaridade)

if maior_similaridade > 0.5:
    print(f'Técnica detectada: {melhor_tecnica}')
else:
    print('Não foi possível detectar a técnica.')
