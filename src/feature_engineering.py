import pandas as pd
import datetime as dt

def compute_rfm_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula as metricas RFM (Recency, Frequency, Monetary) a partir dos dados transacionais.
    
    Retorna um DataFrame indexado por CustomerID.
    """
    print("Iniciando calculo de RFM...")

    # Define a data de referencia (Snapshot date)
    # Pegamos a ultima data do dataset + 1 dia para simular o dia seguinte a analise
    snapshot_date = df['InvoiceDate'].max() + dt.timedelta(days=1)
    
    # Agrupamento por CustomerID
    rfm = df.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (snapshot_date - x.max()).days, # Recency
        'InvoiceNo': 'nunique',                                  # Frequency (pedidos unicos)
        'TotalPrice': 'sum'                                      # Monetary
    })
    
    # Renomear colunas para padrao de mercado
    rfm.rename(columns={
        'InvoiceDate': 'Recency',
        'InvoiceNo': 'Frequency',
        'TotalPrice': 'Monetary'
    }, inplace=True)
    
    print(f"RFM calculado com sucesso. Total de clientes unicos: {len(rfm)}")
    
    return rfm

if __name__ == "__main__":
    # Teste isolado do modulo
    from src.data_loader import load_raw_data
    from src.preprocessing import clean_data
    
    try:
        # Pipeline manual para teste
        df_raw = load_raw_data()
        df_silver = clean_data(df_raw)
        df_gold = compute_rfm_metrics(df_silver)
        
        print("\n--- Amostra do RFM (Gold Layer) ---")
        print(df_gold.head())
        print(df_gold.describe())
        
    except Exception as e:
        print(f"Erro no calculo RFM: {e}")