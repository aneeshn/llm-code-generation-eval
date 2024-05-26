import json
import logging
import os
from pathlib import Path

from datasets import load_dataset

HUMAN_EVAL_DATASET = "openai_humaneval"
PATH = Path("data/humanEval.jsonl")
CURRENT_DIRECTORY = os.getcwd()
DATA_FILE_PATH = CURRENT_DIRECTORY / PATH

LOG_HANDLERS = [
    logging.FileHandler("llm_code_generation_eval.log"),
    logging.StreamHandler(),
]

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=LOG_HANDLERS,
)


def download_dataset():
    logger = logging.getLogger(__name__)
    dataset = load_dataset(HUMAN_EVAL_DATASET)
    with open(DATA_FILE_PATH, "wb") as csv_file:
        for row in dataset["test"]:
            json_row = (json.dumps(row) + "\n").encode("utf-8")
            csv_file.write(json_row)
    logger.info("Complete downloading the dataset")
