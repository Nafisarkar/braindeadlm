
import torch
from braindeadlm.embeddings import TokenEmbedding, PositionalEmbedding
from braindeadlm.tool import clear_screen_safe

def main( ):
    
    vocab_size = 8000
    embedding_dim = 256
    
    context_length = 16
    
    embedding = TokenEmbedding(vocab_size,embedding_dim)
    position_embedding = PositionalEmbedding(context_length=context_length,embedding_dim=embedding_dim);
    
    token_ids = torch.tensor([[42, 91, 17, 5],
                                           [10, 20, 30, 40],])
    positions = torch.arange(context_length)
    
    output:torch.Tensor = embedding(token_ids)
    position_vectors = position_embedding(positions)
    
    
    clear_screen_safe()
    print("Input Size : ", token_ids.shape)
    print("Output Size: ", output.shape)
    
    print("Position IDs shape:", positions.shape)
    print("Position embedding shape:", position_vectors.shape)

if __name__ == "__main__":
    main()