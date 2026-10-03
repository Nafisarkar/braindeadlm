import json
from pathlib import Path

from tinylm.dataset import TextDataset
from tinylm.tokenizer import Tokenizer


DATA_FILE = Path("data/train.txt")
VOCAB_FILE = Path("data/vocab.json")


def main():
    tokenizer = Tokenizer()

    text = DATA_FILE.read_text(
        encoding="utf-8"
    )

    vocab = json.loads(
        VOCAB_FILE.read_text(
            encoding="utf-8"
        )
    )

    dataset = TextDataset(
        text=text,
        tokenizer=tokenizer,
        vocab=vocab,
        context_length=16,
    )

    print("Dataset size:", len(dataset))

    input_ids, target_ids = dataset[0]

    print("Input:")
    print(input_ids)

    print("Target:")
    print(target_ids)

    print("Input shape:", input_ids.shape)
    print("Target shape:", target_ids.shape)


if __name__ == "__main__":
    main()