import re

class Tokenizer:
    
    def tokenize (self,text:str) -> list[str]:
        return [token.lower() for token in re.findall(r'\w+', text)]
    
    def generate_vocab (self, all_tokens:list[str]) -> dict[str,int]:
        unique_tokens = list(set(all_tokens));
        vocab = {
            "<UNK>": 0
        }
        for idx, token in enumerate(unique_tokens, start=1):
            vocab[token] = idx
        return vocab
    
    # [{1:i}, {2:you}, {3:me}] -> [1, 3, 4]
    def encode (self, vocab:dict[str,int], text:str) -> list[int]:
        tokens = self.tokenize(text)
        unk_id = vocab["<UNK>"]
        encoded = []
        for token in tokens:
            encoded.append(vocab.get(token, unk_id))
        return encoded
    
    # [1, 3, 4] -> [{1:i}, {2:you}, {3:me}]
    def decode (self, vocab:dict[str,int], encoding:list[int]) -> list[str]:
        inv_vocab = {v: k for k, v in vocab.items()}
        tokens = []
        for idx in encoding:
            tokens.append(inv_vocab.get(idx))
        return tokens
        
        




