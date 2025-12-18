# Examples

This directory contains example scripts demonstrating how to use the Language Embedding Toolkit.

## Available Examples

### 1. `basic_usage.py`
Demonstrates the basic functionality of the library:
- Loading pre-trained models
- Comparing words across languages
- Getting word embeddings

**Usage:**
```bash
cd examples
python basic_usage.py
```

**Prerequisites:**
- Trained models must exist in the `models/` directory
- Phonetic data must be available in the `data/` directory

### 2. `train_models.py`
Shows how to train new CBOW models:
- Setting up the data pipeline
- Training phoneme and word models
- Saving models for later use

**Usage:**
```bash
cd examples
python train_models.py
```

**Note:** Training can take some time depending on the size of your dataset and hardware.

## Configuration

You can modify hyperparameters in `library/embedding_service/embeding/hyperparameters.py`:

```python
EMBEDDING_DIM = 128      # Embedding vector dimension
WINDOW_SIZE = 3          # Context window size for CBOW
MIN_COUNT = 2            # Minimum word frequency
EPOCHS = 10              # Training epochs
BATCH_SIZE = 64          # Batch size for training
LEARNING_RATE = 0.001    # Learning rate
```

## Data Requirements

### Phonetic Data Format

The library expects phonetic data in the following format:

```
data/
└── {language_code}/
    └── phonemes.txt
```

Each line in `phonemes.txt` should be:
```
word<TAB>phoneme1 phoneme2 phoneme3 ...
```

Example:
```
hello	h ə l oʊ
world	w ɜː l d
```

## Troubleshooting

### Models Not Found
If you get a "models not found" error, you need to train models first:
```bash
python train_models.py
```

### Missing Phonetic Data
The library will attempt to download phonetic data automatically. If this fails, you may need to manually add phoneme files to the `data/{language_code}/` directory.

### CUDA Out of Memory
If you encounter CUDA memory errors during training:
1. Reduce `BATCH_SIZE` in hyperparameters
2. Reduce `EMBEDDING_DIM`
3. Train on CPU by setting `device='cpu'` in WordComparator

## Advanced Usage

For more advanced usage patterns, see the main README.md in the repository root.
