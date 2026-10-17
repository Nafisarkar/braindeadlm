from pathlib import Path
from datasets import load_dataset
import random
random.seed(42)

# Configuration
NUM_STORIES = 1000
VALIDATION_SIZE = 50

DATA_DIR = Path("data")
RAW_DIR = DATA_DIR / "raw"

RAW_FILE = RAW_DIR / "train_raw.txt"
TRAIN_FILE = DATA_DIR / "train.txt"
VALIDATION_FILE = DATA_DIR / "validation.txt"


def main():
    
    print("Loading TinyStories...")
    
    dataset = load_dataset("roneneldan/TinyStories",split="train",streaming=True)
    stories = []
    
    print(f"Collecting {NUM_STORIES} stories...")
    
    for story in dataset:
        text = story["text"].strip()
        if not text:
            continue
        stories.append(text)
        if len(stories) >= NUM_STORIES:
            break
        
    print(f"Collected {len(stories)} stories")
    
    random.shuffle(stories)
    # Split train / validation
    validation = stories[:VALIDATION_SIZE]
    train = stories[VALIDATION_SIZE:]
    
    # Create directories
    RAW_DIR.mkdir(parents=True,exist_ok=True)
    DATA_DIR.mkdir(parents=True,exist_ok=True)
    
    # Save raw data
    RAW_FILE.write_text("\n\n".join(stories), encoding="utf-8")
    # Save train data
    TRAIN_FILE.write_text("\n\n".join(train), encoding="utf-8")
    # Save validation data
    VALIDATION_FILE.write_text("\n\n".join(validation),encoding="utf-8")
    
    print()
    print("Dataset prepared!")
    print(f"Raw:        {RAW_FILE}")
    print(f"Training:   {TRAIN_FILE}")
    print(f"Validation: {VALIDATION_FILE}")


if __name__ == "__main__":
    main()