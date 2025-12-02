import pandas as pd
from src.config import PROJECT_ROOT, GOLD_DATA_DIR
from src.data_loader import load_raw_data
from src.preprocessing import clean_data
from src.feature_engineering import compute_rfm_metrics
from src.clustering import preprocess_for_clustering, train_kmeans
from src.visualization import plot_rfm_clusters

def run_pipeline():
    """
    Executa o pipeline completo:
    Raw -> Silver (Limpeza) -> Gold (RFM) -> Modelo (K-Means) -> Relatorios
    """
    print("--- INICIANDO PIPELINE DE DADOS ---")
    
    # 1. Ingestao
    df_raw = load_raw_data()
    
    # 2. Pre-processamento (Silver)
    df_silver = clean_data(df_raw)
    silver_file = PROJECT_ROOT / "data" / "silver" / "retail_clean.csv"
    print(f"Salvando camada Silver em: {silver_file}...")
    df_silver.to_csv(silver_file, index=False)
    
    # 3. Engenharia de Features (Gold)
    df_rfm = compute_rfm_metrics(df_silver)
    
    # 4. Modelagem (Clustering)
    print("Iniciando Clusterizacao...")
    df_scaled = preprocess_for_clustering(df_rfm)
    clusters = train_kmeans(df_scaled, k=4)
    
    # Atribui o resultado ao dataframe original (Gold)
    df_rfm['Cluster'] = clusters
    
    # 5. Persistencia (Salvar Dados Finais)
    output_file = GOLD_DATA_DIR / "rfm_clusters.csv"
    print(f"Salvando dados finais em: {output_file}...")
    df_rfm.to_csv(output_file)
    
    # 6. Visualizacao (Gerar Insights)
    docs_dir = PROJECT_ROOT / "docs" / "img"
    plot_rfm_clusters(df_rfm, docs_dir)
    
    print("--- PIPELINE CONCLUIDO COM SUCESSO ---")
    print("Verifique a pasta 'data/gold' para o CSV e 'docs/img' para os graficos.")

if __name__ == "__main__":
    run_pipeline()