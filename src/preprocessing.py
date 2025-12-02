import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica regras da camada Silver:
    1. Remove CustomerID nulos.
    2. Remove registros com quantidade ou preco unitario <= 0.
    3. Remove duplicatas.
    4. Converte tipos de dados.
    5. Cria coluna TotalPrice.
    """
    
    # Evita Warning de SettingWithCopy
    df = df.copy()
    
    initial_rows = len(df)
    print(f"Iniciando limpeza. Total de registros iniciais: {initial_rows}")

    # 1. Remover CustomerID nulos (essencial para RFM)
    df = df.dropna(subset=['CustomerID'])
    
    # 2. Tipagem de dados
    # Converter CustomerID para inteiro e depois para string (remove .0)
    df['CustomerID'] = df['CustomerID'].astype(int).astype(str)
    
    # Converter InvoiceDate para datetime
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

    # 3. Remover valores numericos invalidos
    # Regra de negocio: Apenas vendas validas (Quantity > 0 e UnitPrice > 0)
    df = df[ (df['Quantity'] > 0) & (df['UnitPrice'] > 0) ]
    
    # 4. Remover duplicatas
    df = df.drop_duplicates()
    
    # 5. Criar coluna TotalPrice
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
    
    final_rows = len(df)
    removed_rows = initial_rows - final_rows
    
    print(f"Limpeza concluida. Registros removidos: {removed_rows}")
    print(f"Total de registros finais: {final_rows}")
    
    return df

if __name__ == "__main__":
    # Teste isolado
    from src.data_loader import load_raw_data
    
    try:
        df_raw = load_raw_data()
        df_silver = clean_data(df_raw)
        print(df_silver.head())
        print(df_silver.info())
    except Exception as e:
        print(f"Erro na execucao: {e}")