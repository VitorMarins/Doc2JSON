import easyocr

def carregar_easyocr():
    print("⏳ Carregando o EasyOCR (Modelos de Português)...")
    reader = easyocr.Reader(['pt'], gpu=True)
    print("🤖 EasyOCR carregado com sucesso!")
    return reader