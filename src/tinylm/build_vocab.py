from pathlib import Path
from tinylm.tokenizer import Tokenizer

DATA_FILE = Path("data/train.txt")

def main():
    tokenizer = Tokenizer()
    text = DATA_FILE.read_text(encoding="utf-8")
    
    tokens = tokenizer.tokenize(text)
    
    
    print(f"Characters: {len(text):,}")
    print(f"Tokens    : {len(tokens):,}")
    

if __name__ == "__main__":
    main()