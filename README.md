# Doc2JSON Projeto de Visão Computacional 

Doc2JSON é um pipeline de Inteligência Artificial e Visão Computacional de baixo custo projetado para extrair texto de imagens de documentos e transformá-los em dados estruturados no formato JSON, operando de forma 100% local e gratuita.

## 📁 Estrutura do Projeto

```
.
├── src/
│   ├── app.py              # Ponto de entrada da aplicação
│   └── pipeline/           # Módulo central encapsulado
│       ├── __init__.py     # Fachada que expõe as funções do pipeline
│       ├── tratamento.py   # Funções de pré-processamento
│       └── modelo.py       # Inferência e lógica do modelo
├── input/                  # Imagens de entrada
├── output/                 # Resultados processados e JSON de saída
└── requirements.txt        # Lista de dependências
```

## 🚀 Como usar

### Requisitos
- Python 3.8 ou superior

### Instalação

1. Clone o repositório:
   ```powershell
   git clone <URL-do-repositório>
   cd AnaliseDados
   ```

2. Crie e ative o ambiente virtual:
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. Instale as dependências:
   ```powershell
   pip install -r requirements.txt
   ```

### Execução

Execute a aplicação principal:

```powershell
python src/app.py
```

## 🧩 O que o projeto faz

- Carrega imagens da pasta `input/`
- Aplica pré-processamento nos dados
- Executa a inferência do modelo
- Gera resultados estruturados em `output/`

## 📦 Dependências principais

- `numpy` - Operações numéricas
- `opencv-python` - Processamento de imagens
- `torch` - Framework de deep learning
- `easyocr` - Reconhecimento óptico de caracteres

## 📌 Observações

- Ajuste os caminhos de entrada e saída no `src/app.py` se necessário.
- Verifique o `requirements.txt` para versões específicas das bibliotecas.
