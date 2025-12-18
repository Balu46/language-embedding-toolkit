"""
Basic usage example for the Language Embedding Toolkit.

This script demonstrates how to:
1. Initialize the WordComparator
2. Compare words across different languages
3. Display similarity metrics
"""

import os
import sys

# Add parent directory to path to import library
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from embedding_service.compare_words import WordComparator


def main():
    print("=" * 60)
    print("Language Embedding Toolkit - Basic Usage Example")
    print("=" * 60)
    
    # Example 1: Auto-discover models for specific languages
    print("\n📚 Example 1: Auto-discovering models...")
    try:
        comparator = WordComparator(
            languages=['en', 'pl'],  # English and Polish
            data_dir='../data'  # Adjust path as needed
        )
        print("Models loaded successfully!")
    except Exception as e:
        print(f"Error loading models: {e}")
        print("\nNote: You need to train models first using run_train_data_pipeline.py")
        return
    
    # Example 2: Compare similar words
    print("\n📊 Example 2: Comparing similar words...")
    word_pairs = [
        ('hello', 'en', 'cześć', 'pl'),
        ('cat', 'en', 'kot', 'pl'),
        ('computer', 'en', 'komputer', 'pl'),
    ]
    
    for word1, lang1, word2, lang2 in word_pairs:
        try:
            result = comparator.compare_words(
                word1=word1,
                lang1=lang1,
                word2=word2,
                lang2=lang2,
                data_dir='../data'
            )
            
            print(f"\n  {word1} ({lang1}) vs {word2} ({lang2}):")
            print(f"    Cosine Similarity: {result['cosine_similarity']:.4f}")
            print(f"    Euclidean Distance: {result['euclidean_distance']:.4f}")
            print(f"    Phonemes: {' '.join(result['phonemes1'])} | {' '.join(result['phonemes2'])}")
        except Exception as e:
            print(f"    ❌ Error comparing {word1} and {word2}: {e}")
    
    # Example 3: Get combined embedding for a single word
    print("\nExample 3: Getting word embedding...")
    word = "hello"
    phonemes = ['h', 'ə', 'l', 'oʊ']  # IPA representation
    
    embedding = comparator.get_combined_embedding(word, phonemes)
    print(f"  Word: {word}")
    print(f"  Phonemes: {' '.join(phonemes)}")
    print(f"  Combined embedding dimension: {len(embedding)}")
    print(f"  First 5 values: {embedding[:5]}")
    
    print("\n" + "=" * 60)
    print("Example completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
