"""
Module for data ingestion pipeline.
"""

def run_pipeline_a(source: str) -> bool:
    """Ingest data from a source.

    Args:
        source (str): Path or connection string.

    Returns:
        bool: True if ingestion succeeds.
    """
    print(f"Ingesting data from {source}")
    return True
