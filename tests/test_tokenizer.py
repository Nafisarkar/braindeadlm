from tinylm.tokenizer import Tokenizer

data = "IdeaWeaver a comprehensive CLI tool"

tool = Tokenizer()

all_tokens = tool.tokenize(data)

vocab = tool.generate_vocab(all_tokens)

encoding = tool.encode(
    vocab,
    "IdeaWeaver a comprehensive Banana"
)

decoding = tool.decode(
    vocab,
    encoding
)

print(all_tokens)
print(vocab)
print(encoding)
print(decoding)