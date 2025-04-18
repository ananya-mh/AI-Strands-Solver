#Use of Llama as an alternative transformer.

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from huggingface_hub import login
import torch
import torch.nn.functional as F
from wordfreq import word_frequency

login(token="Enter Token here ")

model_id = "meta-llama/Llama-2-7b-hf"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id, 
    output_hidden_states=True  
).eval()

fill_mask_pipeline = pipeline("fill-mask", model="bert-base-uncased")

def get_embedding(text: str) -> torch.Tensor:
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.hidden_states[-1].mean(dim=1).squeeze()

def semantic_similarity(candidate: str, theme: str) -> float:
    cand_emb = get_embedding(candidate)
    theme_emb = get_embedding(theme)
    return F.cosine_similarity(cand_emb.unsqueeze(0), theme_emb.unsqueeze(0)).item()

def lm_score(candidate: str, theme: str) -> float:
    prompt = f"The theme is {theme}. A related word is [MASK]."
    results = fill_mask_pipeline(prompt, targets=[candidate])
    return results[0]["score"] if results else 0.0  
def rank_candidates(
    candidates: list,
    hint: str,
    weight_sim: float = 0.5,
    weight_lm: float = 0.3,
    weight_freq: float = 0.2,
    verbose: bool = False,
) -> list:
    ranked = []
    for candidate, positions in candidates:
        sim = semantic_similarity(candidate, hint)
        lm_sc = lm_score(candidate, hint)
        freq = word_frequency(candidate.lower(), "en", wordlist="large")
        overall_score = (weight_sim * sim) + (weight_lm * lm_sc) + (weight_freq * freq)
        ranked.append((candidate, positions, overall_score))

        if verbose:
            print(f"\t{candidate}: sim={sim:.3f}, lm={lm_sc:.3f}, freq={freq:.5f}, score={overall_score:.4f}")

    ranked.sort(key=lambda x: x[2], reverse=True) 
    return ranked
