import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

def plot_rfm_clusters(df: pd.DataFrame, output_dir: Path):
    """
    Gera boxplots para analisar a distribuicao de Recency, Frequency e Monetary
    por Cluster e salva os arquivos na pasta de saida.
    """
    # Garante que a pasta existe
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Configura estilo visual simples
    sns.set_theme(style="whitegrid")
    
    # Lista de metricas para plotar
    metrics = ['Recency', 'Frequency', 'Monetary']
    
    print(f"Gerando graficos em: {output_dir}...")
    
    for metric in metrics:
        plt.figure(figsize=(10, 6))
        
        # Boxplot ajuda a ver a mediana e os outliers de cada grupo
        sns.boxplot(data=df, x='Cluster', y=metric, palette='viridis')
        
        plt.title(f'Distribuicao de {metric} por Cluster')
        plt.xlabel('Cluster')
        plt.ylabel(metric)
        
        # Salva o arquivo
        filename = output_dir / f"boxplot_{metric.lower()}.png"
        plt.savefig(filename)
        plt.close() # Fecha para liberar memoria
        
        print(f"Grafico salvo: {filename.name}")

if __name__ == "__main__":
    # Teste isolado nao e necessario aqui pois depende do dataframe com cluster
    # Sera testado via pipeline
    pass