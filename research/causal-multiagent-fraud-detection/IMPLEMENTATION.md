# Research implementation update

The implementation bundle adds a reproducible Python pipeline, unit tests, dependencies, dataset instructions, a detailed experimental protocol and a literature-review plan.

## Run it

1. Download `implementation_bundle.tar.gz` from this directory.
2. Extract it inside `research/causal-multiagent-fraud-detection/`.
3. From that project directory run:

```bash
python -m pip install -r requirements.txt
python -m pytest -q
python -m src.pipeline --data data/creditcard.csv --output outputs
```

Alternatively omit `--data` to fetch OpenML data ID 1597 (internet required). The raw dataset is not included.

**Research status:** implementation and synthetic smoke test completed; empirical execution on the full ULB/Worldline dataset is still pending. Synthetic smoke-test outputs are not research findings. No empirical performance claims are made.