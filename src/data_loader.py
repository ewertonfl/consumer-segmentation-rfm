import pandas as pd
from src.config import RAW_DATA_FILE

def load_raw_data():
    """Carrega o dataset da pasta raw."""
    if not RAW_DATA_FILE:
        raise FileNotFoundError("Nenhum arquivo encontrado em data/raw/. Adicione o 'online_retail.xlsx'.")
    
    print(f"Lendo arquivo: {RAW_DATA_FILE.name}...")
    
    # Engine openpyxl é obrigatória para xlsx
    if RAW_DATA_FILE.suffix == '.xlsx':
        df = pd.read_excel(RAW_DATA_FILE, engine='openpyxl')
    else:
        df = pd.read_csv(RAW_DATA_FILE, encoding='ISO-8859-1')
        
    print(f"Sucesso! Linhas: {df.shape[0]}, Colunas: {df.shape[1]}")
    return df

if __name__ == "__main__":
    load_raw_data()