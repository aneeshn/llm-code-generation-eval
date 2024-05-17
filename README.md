This project is to track how to use some common evaluation data set to benchmark LLMs that are available to you.

## Data Set
- HumanEval dataset from OpenAI


## Evaluation Metric
- Pass@k

## LLM Benchmarked
- Anthropic Claude 3 Sonnet hosted on AWS Bedrock


## Development Setup

Install pre-commit and generate a pre-commit-config.yaml file
```commandline
pip install pre-commit

pre-commit install

pre-commit sample-config >.pre-commit-config.yaml
```

The output of the generated pre-commit config file will look as follows:
```commandline
# See https://pre-commit.com for more information
# See https://pre-commit.com/hooks.html for more hooks
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v3.2.0
    hooks:
    -   id: trailing-whitespace
    -   id: end-of-file-fixer
    -   id: check-yaml
    -   id: check-added-large-files
```

Now add the following to the pre-commit files:
- Lint: Flake-8
