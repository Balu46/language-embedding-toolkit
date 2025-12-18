"""
Training example for the Language Embedding Toolkit.

This script demonstrates how to:
1. Set up the data pipeline
2. Train CBOW models for phonemes and words
3. Save trained models
"""

import os
import sys

# Add parent directory to path to import library
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from embedding_service.run_train_data_pipeline import main as train_main
from embedding_service.embeding import hyperparameters as hp


def main():
    print("=" * 60)
    print("Language Embedding Toolkit - Training Example")
    print("=" * 60)
    
    print("\n📋 Current Hyperparameters:")
    print(f"  Embedding Dimension: {hp.EMBEDDING_DIM}")
    print(f"  Window Size: {hp.WINDOW_SIZE}")
    print(f"  Min Count: {hp.MIN_COUNT}")
    print(f"  Epochs: {hp.EPOCHS}")
    print(f"  Batch Size: {hp.BATCH_SIZE}")
    print(f"  Learning Rate: {hp.LEARNING_RATE}")
    
    print("\n🚀 Starting training pipeline...")
    print("This will:")
    print("  1. Download phonetic data (if not present)")
    print("  2. Train phoneme CBOW model")
    print("  3. Train word CBOW model")
    print("  4. Save models to 'models/' directory")
    
    response = input("\nProceed with training? (y/n): ")
    if response.lower() != 'y':
        print("Training cancelled.")
        return
    
    try:
        # Run the training pipeline
        train_main()
        
        print("\n" + "=" * 60)
        print("✅ Training completed successfully!")
        print("=" * 60)
        print("\nTrained models saved in 'models/' directory.")
        print("You can now use these models with WordComparator.")
        
    except Exception as e:
        print(f"\n❌ Error during training: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
