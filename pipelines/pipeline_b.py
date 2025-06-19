"""
Module for data transformation pipeline.
"""

def run_pipeline_b(data: list) -> list:
    """Transforms raw data.

    Args:
        data (list): Raw data rows.

    Returns:
        list: Transformed data.
    """
    transformed = [d.upper() for d in data]
    return transformed
