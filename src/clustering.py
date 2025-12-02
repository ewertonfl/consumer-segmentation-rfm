import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def preprocess_for_clustering(rfm_df: pd.DataFrame) -> pd.DataFrame:
    """
    Prepara os dados para o K-Means:
    1. Remove assimetria (Log Transformation).
    2. Normaliza a escala (StandardScaler).
    """
    # Copia para nao alterar o original
    df_log = rfm_df.copy()
    
    # Log transformation para lidar com skewness (assimetria)
    # Adicionamos +1 para evitar log(0) ou log(numeros negativos)
    cols = ['Recency', 'Frequency', 'Monetary']
    for col in cols:
        df_log[col] = np.log1p(df_log[col])
        
    # Scaling (Média 0, Desvio Padrão 1)
    scaler = StandardScaler()
    scaler.fit(df_log)
    
    # Cria dataframe normalizado mantendo indices e colunas
    df_normalized = pd.DataFrame(
        scaler.transform(df_log),
        index=df_log.index,
        columns=df_log.columns
    )
    
    return df_normalized

def train_kmeans(rfm_scaled_df: pd.DataFrame, k: int = 4) -> pd.DataFrame:
    """
    Treina o K-Means e retorna os clusters.
    k=4 e um padrao de mercado inicial (Diamante, Ouro, Prata, Bronze).
    """
    print(f"Treinando K-Means com k={k}...")
    
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(rfm_scaled_df)
    
    # Retorna apenas os labels (0, 1, 2, 3...)
    cluster_labels = kmeans.labels_
    
    return cluster_labels

if __name__ == "__main__":
    # Teste isolado
    from src.data_loader import load_raw_data
    from src.preprocessing import clean_data
    from src.feature_engineering import compute_rfm_metrics
    
    try:
        # Pipeline de preparacao
        df_raw = load_raw_data()
        df_silver = clean_data(df_raw)
        df_rfm = compute_rfm_metrics(df_silver)
        
        # 1. Pre-processamento para ML
        df_scaled = preprocess_for_clustering(df_rfm)
        print("\n--- Dados Normalizados (Head) ---")
        print(df_scaled.head())
        
        # 2. Treinamento
        clusters = train_kmeans(df_scaled, k=4)
        
        # 3. Atribuicao ao DataFrame original
        df_rfm['Cluster'] = clusters
        
        print("\n--- Resultado Final com Clusters ---")
        print(df_rfm.head())
        print("\n--- Contagem por Cluster ---")
        print(df_rfm['Cluster'].value_counts())
        
    except Exception as e:
        print(f"Erro no Clustering: {e}")