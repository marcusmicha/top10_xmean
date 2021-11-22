import pandas as pd
from citi_ex import get_means, apply_means, get_by_name, get_top10, DF

def test_get_means():
    test_df = pd.DataFrame({
        'name': ['Artur', 'Michael', 'Artur', 'Artur'],
        'x': [5, 2, 10, 15]
        })
    res = get_means(test_df)
    assert res['Artur'] == 10
    assert res['Michael'] == 2




test_get_means()
