def calculate_kpis(data):
    """
    Calculate KPIs from the given data DataFrame.
    Expects columns: 'performance_score', 'kpi_value'
    Returns a dictionary with average performance and total KPI.
    """
    average_performance = data['performance_score'].mean()
    total_kpi = data['kpi_value'].sum()
    return {
        'average_performance': average_performance,
        'total_kpi': total_kpi
    }
