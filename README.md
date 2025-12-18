# Language Embedding Toolkit

A Python library for training and comparing multilingual word embeddings using both phonetic (IPA) and character-level representations. This toolkit enables cross-lingual word comparison through combined embeddings trained via CBOW (Continuous Bag of Words) models.

## Features

- 🔤 **Dual Embedding Approach**: Combines phonetic (IPA) and character-level word embeddings
- 🌍 **Multilingual Support**: Train models on multiple languages simultaneously
- 🧠 **CBOW Training**: Efficient word embedding training using PyTorch
- 📊 **Word Comparison**: Calculate similarity metrics between words across languages
- 📈 **Automated Data Pipeline**: Download and process phonetic data automatically
- 🔧 **Flexible Architecture**: Easy to extend and customize

## Installation

### From Source

```bash
git clone https://github.com/yourusername/language-embedding-toolkit.git
cd language-embedding-toolkit
pip install -r requirements.txt
pip install -e .
```

### Using pip (if published to PyPI) (curently not done)

```bash
pip install language-embedding-toolkit
```

## Requirements

- Python >= 3.8
- PyTorch >= 2.0
- See `requirements.txt` for full dependency list

## Quick Start

### 1. Training CBOW Models

```python
from library.embedding_service.run_train_data_pipeline import main

# Train models for multiple languages
# This will download phonetic data and train both phoneme and word models
main()
```

### 2. Comparing Words Across Languages

```python
from library.embedding_service.compare_words import WordComparator

# Initialize comparator (auto-discovers models)
comparator = WordComparator(
    languages=['en', 'pl'],  # English and Polish
    data_dir='data'
)

# Compare two words
result = comparator.compare_words(
    word1='hello',
    lang1='en',
    word2='cześć',
    lang2='pl',
    data_dir='data'
)

print(f"Cosine Similarity: {result['cosine_similarity']:.4f}")
print(f"Euclidean Distance: {result['euclidean_distance']:.4f}")
```

### 3. Using Pre-trained Models

```python
from library.embedding_service.compare_words import WordComparator

# Load specific model files
comparator = WordComparator(
    phoneme_model_path='models/cbow_phonemes_en_pl.pt',
    word_model_path='models/cbow_words_en_pl.pt'
)
```

## Project Structure

```
library/
├── embedding_service/          # Main embedding functionality
│   ├── compare_words.py        # Word comparison utilities
│   ├── run_train_data_pipeline.py  # Training pipeline
│   ├── data/                   # Data processing modules
│   │   ├── data_pipeline.py
│   │   ├── data_scraping/      # Phoneme data extraction
│   │   └── datasets/           # PyTorch dataset classes
│   └── embeding/               # CBOW model implementation
│       ├── cbow.py             # Model architecture
│       ├── train_cbow.py       # Training logic
│       └── hyperparameters.py  # Model configuration
└── logger/                     # Logging utilities
    └── logging_config.py
```

## How It Works

1. **Data Collection**: Automatically downloads phonetic transcriptions (IPA) for words in specified languages
2. **Dual Model Training**: 
   - Trains a CBOW model on phoneme sequences
   - Trains a CBOW model on character sequences
3. **Combined Embeddings**: Concatenates phoneme and character embeddings for each word
4. **Similarity Calculation**: Uses cosine similarity and Euclidean distance to compare word embeddings

## API Documentation

### WordComparator

Main class for word comparison operations.

**Constructor Parameters:**
- `phoneme_model_path` (str, optional): Path to phoneme CBOW model
- `word_model_path` (str, optional): Path to word CBOW model
- `languages` (List[str], optional): Languages to support (required if models not provided)
- `data_dir` (str): Data directory path (default: 'data')
- `device` (str): Computation device ('cpu', 'cuda', or 'auto')

**Key Methods:**
- `compare_words(word1, lang1, word2, lang2, data_dir)`: Compare two words
- `get_combined_embedding(word, phonemes)`: Get concatenated embedding for a word
- `phonemes_to_embedding(phonemes)`: Convert phoneme sequence to embedding
- `characters_to_embedding(characters)`: Convert character sequence to embedding

## Examples

See the `examples/` directory for more detailed usage examples:
- `basic_usage.py`: Simple word comparison
- `train_models.py`: Custom model training

## Configuration

Model hyperparameters can be configured in `embedding_service/embeding/hyperparameters.py`:

```python
EMBEDDING_DIM = 128
WINDOW_SIZE = 3
MIN_COUNT = 2
EPOCHS = 10
BATCH_SIZE = 64
LEARNING_RATE = 0.001
```

## Logging

The library includes comprehensive logging functionality. Logs are saved to the `logs/` directory by default.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Citation

If you use this library in your research, please cite:

```bibtex
@software{language_embedding_toolkit,
  title={Language Embedding Toolkit},
  author={Your Name},
  year={2025},
  url={https://github.com/yourusername/language-embedding-toolkit}
}
```

## Acknowledgments

- Built with PyTorch
- Phonetic data sourced from Wiktionary
- Inspired by cross-lingual NLP research

## Contact

For questions or feedback, please open an issue on GitHub or contact [your.email@example.com](mailto:your.email@example.com).
