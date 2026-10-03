from pathlib import Path
import torch
from torch.fft import Tensor
from torch.utils.data import Dataset
from tinylm.tokenizer import Tokenizer

class TextDataset(Dataset):
    def __init__(self,
        text: str,
        tokenizer: Tokenizer,
        vocab: dict[str, int],
        context_length: int) -> None:
        self.tokens = tokenizer.encode(vocab, text)
        self.context_length = context_length
        
    def __len__(self):
        return len(self.tokens) - self.context_length
    
    def __getitem__(self, index) -> tuple[Tensor, Tensor]:
        start = index
        end = start + self.context_length
        input_ids = self.tokens[start:end]
        target_ids = self.tokens[start + 1:end + 1]
        
        #Python list -> PyTorch Tensor
        return (
            torch.tensor(input_ids, dtype=torch.long),
            torch.tensor(target_ids, dtype=torch.long),
        )