import pytest
import pandas as pd
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from analytics.kpi_calculator import calculate_kpis

def test_calculate_kpis():
    # Sample data
    data = pd.DataFrame({
        'employee_id': [1, 2, 3],
        'performance_score': [80, 90, 85],
        'kpi_value': [100, 110, 105]
    })
    result = calculate_kpis(data)
    assert 'average_performance' in result
    assert 'total_kpi' in result
    assert result['average_performance'] == pytest.approx(85.0)
    assert result['total_kpi'] == 315
