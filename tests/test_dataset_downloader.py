import json
from typing import Dict, List
from unittest import TestCase

from llm_code_generation_eval import dataset_downloader


class TestDataSetDownloader(TestCase):
    def test_download_dataset(self):
        dataset_downloader.download_dataset()
        # Check to see if the file exists in that location
        file_location = dataset_downloader.DATA_FILE_PATH
        self.assertTrue(file_location.exists(), "File Exists")
        # Check to see if the content in the file has correct structure
        valid_keys: List[str] = [
            "task_id",
            "prompt",
            "canonical_solution",
            "test",
            "entry_point",
        ]
        with open(file_location, "r") as csv_file:
            read_line: Dict[str, str] = json.loads(csv_file.readline())
            is_keys: bool = all(key in read_line.keys() for key in valid_keys)
            self.assertTrue(is_keys, "All keys are valid")
