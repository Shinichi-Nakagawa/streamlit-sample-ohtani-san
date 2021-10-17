import pytest
import pandas as pd

from interfaces.ml import DataFrame


@pytest.fixture
def df() -> DataFrame:
    return pd.read_csv('./tests/dataset/test_dataset.csv')
