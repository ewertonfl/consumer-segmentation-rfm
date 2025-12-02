import pandas as pd
import pytest
from src.preprocessing import clean_data

@pytest.fixture
def sample_raw_data():
    """Cria um dataframe falso para teste"""
    data = {
        'InvoiceNo': ['1', '2', '3', '4'],
        'StockCode': ['A', 'B', 'C', 'D'],
        'Description': ['Desc1', 'Desc2', 'Desc3', 'Desc4'],
        'Quantity': [10, -5, 10, 5],       # -5 deve ser removido
        'InvoiceDate': ['2023-01-01', '2023-01-01', '2023-01-01', '2023-01-01'],
        'UnitPrice': [5.0, 5.0, 0.0, 2.0], # 0.0 deve ser removido
        'CustomerID': ['100', '100', '101', None], # None deve ser removido
        'Country': ['UK', 'UK', 'UK', 'UK']
    }
    return pd.DataFrame(data)

def test_clean_data_removes_invalid_rows(sample_raw_data):
    """Testa se remove nulos, quantidades negativas e preco zero"""
    df_silver = clean_data(sample_raw_data)
    
    # Só a linha 0 deve sobrar (InvoiceNo '1')
    # Linha 1: Qtd negativa
    # Linha 2: Preço zero
    # Linha 3: CustomerID nulo
    assert len(df_silver) == 1
    assert df_silver.iloc[0]['InvoiceNo'] == '1'

def test_total_price_calculation(sample_raw_data):
    """Testa se a coluna TotalPrice foi criada corretamente"""
    df_silver = clean_data(sample_raw_data)
    expected_total = 10 * 5.0 # Qtd * UnitPrice da linha 0
    assert 'TotalPrice' in df_silver.columns
    assert df_silver.iloc[0]['TotalPrice'] == expected_total