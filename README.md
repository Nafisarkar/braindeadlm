<div align="center">

# braindeadlm

**a language model so small it makes nanoGPT look like GPT-4**

<br/>

_Building an LLM from absolute scratch — tokenizer, dataset, attention, the whole cursed pipeline._
_No `transformers`. No shortcuts. Just tensors, tea, and poor life decisions._

<br/>

![Python](https://img.shields.io/badge/python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/pytorch-2.x-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![Status](https://img.shields.io/badge/status-under_construction-yellow?style=for-the-badge&labelColor=FFD166&color=grey)
![Vibes](https://img.shields.io/badge/vibes-immaculate-9B5DE5?style=for-the-badge)

[the plan](./ROADMAP.md) · [the code](./src/braindeadlm) · [the crime scene](#known-crimes-aka-todo-later-i-promise)

</div>

---

## what even is this

`braindeadlm` is a personal weekend-project-that-got-out-of-hand: a **tiny language model written from scratch** in Python + PyTorch.
---

## the receipts

| thing | number | notes |
|---|---|---|
| source corpus | 1,000 stories | [TinyStories](https://huggingface.co/datasets/roneneldan/TinyStories) — vocab-level: dragons, friendship, mild weather |
| train / validation | 950 / 50 | the 50 stories the model is not allowed to peek at |
| raw corpus | ~934 KB | smaller than one (1) meme folder |
| vocabulary | **4,568 tokens** | whole language, basically |
| context length | 16 tokens | goldfish memory. on purpose. for now. |
| GPU required | lol no | CPU-friendly until further notice |


## quickstart

```bash
git clone https://github.com/Nafisarkar/braindeadlm.git
cd braindeadlm

uv sync                       # summon the dependencies

# 1. grab 1000 tiny stories from HuggingFace
uv run python -m braindeadlm.prepare_data

# 2. build the vocabulary (4,568 words of pure toddler literature)
uv run python -m braindeadlm.build_vocab

# 3. peek at training batches
uv run python tests/test_dataset.py
```

requirements: **Python 3.12+**, `torch`, `datasets`, `numpy`, and `uv` for the rest.

> **note:** the data files are regenerable, not committed. if `data/` is empty, run steps 1–2 and the folder will simply manifest.


---

## faq

**why not just use an existing LLM?**
where's the sport in that.

**is it good?**
it's a lot of things. "good" is not currently one of them. it's *early*.

**why TinyStories?**
the corpus reads like a fever dream narrated by a 5-year-old ("suddenly, they saw a large gust of wind!"). training a transformer on that is objectively funny.

**will it run on my laptop?**
yes. this thing is so tiny it could be out-computed by a determined pocket calculator.

**can it beat GPT-4?**
it cannot beat a well-organized spreadsheet. but it will beat *not understanding transformers*, which is the actual benchmark.

---

<div align="center">

**built for fun, kept for learning.** ⭐ starring this repo will not improve the model, but it will improve *my* training signal.

<br/>

<sub>no GPUs were harmed in the making of this project · several optimizer steps were · MIT-ish, do what you want</sub>

</div>
