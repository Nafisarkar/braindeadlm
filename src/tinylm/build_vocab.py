from pathlib import Path
from tinylm.tokenizer import Tokenizer
import json

DATA_FILE = Path("data/train.txt")
VOCAB_FILE = Path("data/vocab.json")


def main():
    tokenizer = Tokenizer()
    text = DATA_FILE.read_text(encoding="utf-8")
    
    tokens = tokenizer.tokenize(text)
    vocab = tokenizer.generate_vocab(tokens)
    
    print(f"Characters: {len(text):,}")
    print(f"Tokens    : {len(tokens):,}")
    print(f"Vocab     : {len(vocab):,}")
    print(list(vocab.items())[:20])
    VOCAB_FILE.write_text(json.dumps(vocab,ensure_ascii=False,indent=2),encoding="utf-8")

if __name__ == "__main__":
    main()