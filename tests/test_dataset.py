import json
from pathlib import Path
from braindeadlm.tool import clear_screen_safe
from braindeadlm.dataset import TextDataset
from braindeadlm.tokenizer import Tokenizer
from  torch.utils.data import DataLoader

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

    # Create DataLoader
    dataset = TextDataset(
        text=text,
        tokenizer=tokenizer,
        vocab=vocab,
        context_length=16,
    )

    clear_screen_safe()
    print("Dataset size:", len(dataset))
    
    
    loader = DataLoader(dataset,
    batch_size=32,
    shuffle=True)

    inputs, targets = next(iter(loader))

    print("Inputs shape:", inputs.shape)
    print("Targets shape:", targets.shape)

    print("Inputs:")
    print(inputs)

    print("Targets:")
    print(targets)


if __name__ == "__main__":
    main()