import re

class Tokenizer:
    
    def tokenize (self,text:str) -> list[str]:
        return [token.lower() for token in re.findall(r'\w+', text)]
    
    def generate_vocab (self, all_tokens:list[str]) -> dict[str,int]:
        unique_tokens = list(set(all_tokens));
        sorted_tokens = sorted(unique_tokens)    
        return {idx:token for token,idx in enumerate(sorted_tokens)}
    
    def encode (self, vocab:dict[str,int], text:str) -> list[int]:
        ids = []
        tokens = self.tokenize(text)
        for token in tokens:
            ids.append(vocab.get(token))
        return ids;
    
    def decode (self, vocab:dict[str,int],encoding:list[int]) -> list[str]:
        inv_vocab = {v: k for k, v in vocab.items()}
        tokens = []
        for idx in encoding:
            tokens.append(inv_vocab.get(idx))
        return tokens
        
        
        


data = "IdeaWeaver-- a comprehensive CLI tool for AI model training and evaluation? ai"
tool = Tokenizer();
all_tokens = tool.tokenize(data)
vocab = tool.generate_vocab(all_tokens)
encoding = tool.encode(vocab,data)
decoding = tool.decode(vocab,encoding)

print(all_tokens)
print(vocab)
print(encoding)
print(decoding)



