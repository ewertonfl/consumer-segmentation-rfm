import pandas as pd
import shutil
import warnings
from pathlib import Path
from src.config import PROJECT_ROOT, GOLD_DATA_DIR
from src.data_loader import load_raw_data
from src.preprocessing import clean_data
from src.feature_engineering import compute_rfm_metrics
from src.clustering import preprocess_for_clustering, train_kmeans
from src.visualization import plot_rfm_clusters
import sys

def run_full_pipeline():
    """
    Executa o pipeline completo:
    Raw -> Silver (Limpeza) -> Gold (RFM) -> Modelo (K-Means) -> Relatorios
    """
    print("--- INICIANDO PIPELINE COMPLETO ---")
    
    # 1. Ingestão
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
    df_rfm['Cluster'] = clusters
    
    # 5. Persistência (Salvar Dados Finais)
    output_file = GOLD_DATA_DIR / "rfm_clusters.csv"
    print(f"Salvando dados finais em: {output_file}...")
    df_rfm.to_csv(output_file, index=False)
    
    # 6. Visualização (Gráficos)
    docs_dir = PROJECT_ROOT / "docs" / "img"
    _plot_rfm_safe(df_rfm, docs_dir)
    
    print("--- PIPELINE COMPLETO CONCLUÍDO ---")
    print("Verifique 'data/gold' para CSV e 'docs/img' para gráficos.")

def run_plot_only():
    """
    Carrega apenas os dados da camada Gold e gera os gráficos.
    Muito mais rápido.
    """
    gold_file = GOLD_DATA_DIR / "rfm_clusters.csv"
    if not gold_file.exists():
        print(f"Erro: CSV da Gold não encontrado em {gold_file}. Rode o pipeline completo primeiro.")
        return

    print(f"Lendo Gold direto de {gold_file}...")
    df_rfm = pd.read_csv(gold_file)

    docs_dir = PROJECT_ROOT / "docs" / "img"

    # Limpa a pasta antes de gerar os gráficos
    if docs_dir.exists():
        shutil.rmtree(docs_dir)
    docs_dir.mkdir(parents=True, exist_ok=True)

    print("Gerando gráficos diretamente da Gold...")
    _plot_rfm_safe(df_rfm, docs_dir)
    print("Pronto! Gráficos atualizados.")

def _plot_rfm_safe(df_rfm, docs_dir):
    """
    Wrapper que suprime warnings durante a plotagem
    """
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=FutureWarning)
        plot_rfm_clusters(df_rfm, docs_dir)

if __name__ == "__main__":
    # Permite chamar modos via argumento: --full ou --plot-only
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg == "--plot-only":
            run_plot_only()
        elif arg == "--full":
            run_full_pipeline()
        else:
            print("Argumento inválido. Use --full ou --plot-only")
    else:
        # Padrão: full pipeline
        run_full_pipeline()
