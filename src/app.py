import os
import json
from pipeline.modelo import carregar_easyocr
from pipeline.tratamento import preparar_documento

def extrair_texto_com_easyocr(caminho_da_imagem, reader):
    print(f"\n[1/2] Tratando e lendo imagem com EasyOCR...")
    resultado = reader.readtext(caminho_da_imagem, detail=0)
    print(f"Texto bruto extraído: {resultado}")
    texto_completo = " ".join(resultado)
    return texto_completo

if __name__ == "__main__":
    reader = carregar_easyocr()
    imagem = "input/imagem-1.jpg"
    
    if os.path.exists(imagem):
        texto_extraido = extrair_texto_com_easyocr(imagem, reader)
        
        print("\n" + "="*20 + " TEXTO EXTRAÍDO " + "="*20)
        print(texto_extraido)
        print("="*56)
        
        print("\n[2/2] Processando texto para JSON...")
        with open("output/resultados.json", "w", encoding="utf-8") as arquivo:
            json.dump({"texto_extraido": texto_extraido}, arquivo, indent=4, ensure_ascii=False)
        
    else:
        print(f"Coloque a imagem '{imagem}' aqui para testar.")
