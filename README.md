# ROADMAP

## 1. Project Setup

- [x] uv + Python environment setup
- [x] Configure `pyproject.toml`
- [x] Verify PyTorch installation
- [x] Verify CPU/CUDA device

## 2. Tokenizer

- [x] Implement custom Tokenizer
- [x] Implement vocabulary
- [x] Implement text → token IDs
- [x] Implement token IDs → text
- [x] Add special tokens
- [x] Test encode/decode
- [ ] Add special tokens
- [ ] Handle unknown tokens
- [ ] Preserve punctuation
- [ ] Return decoded text
- [ ] Add tokenizer tests

## 3. Training Data

- [ ] Prepare plain-text dataset
- [ ] Clean dataset
- [ ] Split into train/validation sets
- [ ] Convert text into token IDs
- [ ] Create context windows
- [ ] Create input/target pairs
- [ ] Implement `Dataset`
- [ ] Implement `DataLoader`
- [ ] Verify batch shapes

## 4. Embeddings

- [ ] Implement token embeddings
- [ ] Implement positional embeddings
- [ ] Combine token + positional embeddings
- [ ] Verify embedding dimensions

## 5. Causal Self-Attention

- [ ] Implement Query, Key, Value projections
- [ ] Calculate attention scores
- [ ] Implement scaling
- [ ] Implement causal mask
- [ ] Apply softmax
- [ ] Calculate weighted values
- [ ] Implement output projection
- [ ] Test attention output shape

## 6. Multi-Head Attention

- [ ] Split embeddings into multiple heads
- [ ] Run self-attention per head
- [ ] Concatenate heads
- [ ] Apply output projection
- [ ] Verify dimensions

## 7. Feed-Forward Network

- [ ] Implement first linear layer
- [ ] Implement activation function
- [ ] Implement second linear layer
- [ ] Test output shape

## 8. Transformer Block

- [ ] Implement LayerNorm
- [ ] Add attention residual connection
- [ ] Add feed-forward residual connection
- [ ] Combine all components
- [ ] Test forward pass

## 9. TinyLM Model

- [ ] Create model configuration
- [ ] Add token embeddings
- [ ] Add positional embeddings
- [ ] Stack Transformer blocks
- [ ] Add final LayerNorm
- [ ] Add language-model head
- [ ] Calculate logits
- [ ] Verify complete forward pass

## 10. Loss

- [ ] Prepare target tokens
- [ ] Implement next-token prediction
- [ ] Implement cross-entropy loss
- [ ] Verify loss calculation
- [ ] Test loss decreases on a tiny dataset

## 11. Training Loop

- [ ] Initialize model
- [ ] Initialize optimizer
- [ ] Load training batches
- [ ] Forward pass
- [ ] Calculate loss
- [ ] Backpropagation
- [ ] Optimizer update
- [ ] Reset gradients
- [ ] Track training loss
- [ ] Track validation loss
- [ ] Add checkpoint saving

## 12. Training

- [ ] Train on a tiny dataset
- [ ] Confirm model can overfit a tiny dataset
- [ ] Train on the full dataset
- [ ] Monitor train/validation loss
- [ ] Save best checkpoint
- [ ] Resume training from checkpoint

## 13. Text Generation

- [ ] Load trained checkpoint
- [ ] Encode prompt
- [ ] Run model
- [ ] Get next-token probabilities
- [ ] Select/sample next token
- [ ] Append token
- [ ] Repeat generation
- [ ] Decode tokens to text

## 14. Evaluation

- [ ] Test different prompts
- [ ] Compare training/validation loss
- [ ] Check generated text quality
- [ ] Test different temperatures
- [ ] Test top-k sampling
- [ ] Document results

## 15. Improve TinyLM

- [ ] Experiment with model size
- [ ] Experiment with context length
- [ ] Experiment with vocabulary size
- [ ] Experiment with learning rate
- [ ] Experiment with batch size
- [ ] Compare experiments

## 16. JavaScript Model

- [ ] Collect JavaScript/TypeScript dataset
- [ ] Clean code dataset
- [ ] Train/adjust tokenizer
- [ ] Prepare code training data
- [ ] Train TinyLM on JavaScript
- [ ] Test code completion
- [ ] Evaluate generated JavaScript