import os

def create_structure():
    # 1. Definição das pastas
    dirs = [
        "data/raw",
        "data/silver",
        "data/gold",
        "docs",
        "notebooks",
        "src",
        "tests",
        ".github/workflows"
    ]

    # 2. Definição dos arquivos (serão criados vazios ou com conteúdo mínimo seguro)
    files = {
        "src/__init__.py": "",
        "src/config.py": "",
        "src/data_loader.py": "",
        "src/preprocessing.py": "",
        "src/feature_engineering.py": "",
        "src/clustering.py": "",
        "src/visualization.py": "",
        "tests/__init__.py": "",
        "tests/test_preprocessing.py": "",
        "tests/test_rfm.py": "",
        "data/.gitkeep": "",
        "README.md": "",  # Você colará seu texto aqui manualment
        
        # Conteúdo simples para o .gitignore
        ".gitignore": "venv/\n.env\ndata/\n__pycache__/\n.ipynb_checkpoints/\n.vscode/\n",
        
        # Conteúdo simples para requirements.txt
        "requirements.txt": "pandas==2.2.0\nnumpy==1.26.3\nscikit-learn==1.4.0\nmatplotlib==3.8.2\nseaborn==0.13.1\nopenpyxl==3.1.2\npytest==8.0.0\nflake8==7.0.0\nblack==24.1.1\n",
        
        # Conteúdo simples para Makefile (tabulação é importante, usei espaços seguros)
        "Makefile": "setup:\n\tpip install -r requirements.txt\n\ntest:\n\tpytest tests/\n\nrun:\n\tpython src/main.py\n"
    }

    print("Criando estrutura de pastas...")
    
    for d in dirs:
        os.makedirs(d, exist_ok=True)
        print(f"Pasta: {d}")

    for filepath, content in files.items():
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Arquivo: {filepath}")

    print("\nEstrutura criada. Apague este script e siga os próximos passos.")

if __name__ == "__main__":
    create_structure()