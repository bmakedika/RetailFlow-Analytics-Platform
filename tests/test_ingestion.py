from ingestion.pipeline import process_table
from unittest.mock import MagicMock

def test_process_table():

    client = MagicMock()
    logger = MagicMock()

    result = process_table(
        client=client,
        project_id="test",
        dataset="test",
        table="orders",
        file_name="olist_orders_dataset.csv",
        job_config=None,
        logger=logger
    )

    assert result is None
