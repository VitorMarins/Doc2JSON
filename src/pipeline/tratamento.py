import cv2
import numpy as np
from PIL import Image

def redimensionar_imagem(imagem_pil, largura_maxima=1200):
    """
    Reduz o tamanho de imagens gigantescas para economizar memória RAM e processamento,
    mantendo a proporção original do documento.
    """
    largura_original, altura_original = imagem_pil.size
    if largura_original <= largura_maxima:
        return imagem_pil
    proporcao = largura_maxima / float(largura_original)
    altura_nova = int((float(altura_original) * float(proporcao)))
    imagem_redimensionada = imagem_pil.resize((largura_maxima, altura_nova), Image.Resampling.LANCZOS)
    print(f"📐 Imagem redimensionada de {largura_original}px para {largura_maxima}px de largura.")
    return imagem_redimensionada

def melhorar_contraste_e_brilho(imagem_pil):
    """
    Converte para o OpenCV para aplicar filtros que removem sombras 
    e deixam o texto preto bem destacado contra o fundo branco.
    """
    img_cv = cv2.cvtColor(np.array(imagem_pil), cv2.COLOR_RGB2BGR)
    img_gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    img_tratada = cv2.adaptiveThreshold(
        img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
    )
    img_final = Image.fromarray(cv2.cvtColor(img_tratada, cv2.COLOR_GRAY2RGB))
    print("✨ Contraste aprimorado e sombras removidas.")
    return img_final

def preparar_documento(caminho_imagem):
    """
    Função principal que junta todos os tratamentos necessários.
    """
    imagem = Image.open(caminho_imagem).convert("RGB")
    imagem = redimensionar_imagem(imagem)
    #imagem = melhorar_contraste_e_brilho(imagem)
    return imagem
