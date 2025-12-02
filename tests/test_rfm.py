import pandas as pd
import pytest
from src.feature_engineering import compute_rfm_metrics

@pytest.fixture
def sample_silver_data():
    """Dados limpos simulados para testar o calculo de RFM"""
    data = {
        'CustomerID': ['1', '1', '2'],
        'InvoiceNo': ['A', 'B', 'C'], # Cliente 1 tem 2 compras, Cliente 2 tem 1
        'InvoiceDate': pd.to_datetime(['2023-01-01', '2023-01-10', '2023-01-20']),
        'TotalPrice': [100.0, 200.0, 50.0] # Cliente 1 gastou 300, Cliente 2 gastou 50
    }
    return pd.DataFrame(data)

def test_rfm_structure(sample_silver_data):
    """Valida se retorna as colunas corretas"""
    rfm = compute_rfm_metrics(sample_silver_data)
    assert 'Recency' in rfm.columns
    assert 'Frequency' in rfm.columns
    assert 'Monetary' in rfm.columns

def test_rfm_calculation_logic(sample_silver_data):
    """Valida a matematica do RFM"""
    rfm = compute_rfm_metrics(sample_silver_data)
    
    # Cliente 1
    # Frequency: deve ser 2 (Invoices A e B)
    # Monetary: deve ser 300 (100 + 200)
    assert rfm.loc['1', 'Frequency'] == 2
    assert rfm.loc['1', 'Monetary'] == 300.0
    
    # Cliente 2
    # Frequency: 1
    # Monetary: 50
    assert rfm.loc['2', 'Frequency'] == 1
    assert rfm.loc['2', 'Monetary'] == 50.0