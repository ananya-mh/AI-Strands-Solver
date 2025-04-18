#The file used to rank the candidate keys in the dictionary using the input from sentence transformer

import numpy as np
from sentence_transformers import SentenceTransformer, util
from transformers import pipeline
from wordfreq import word_frequency

sentence_model = SentenceTransformer("all-mpnet-base-v2")

fill_mask = pipeline("fill-mask", model="bert-base-uncased", framework="pt")


def semantic_similarity(candidate: str, theme: str) -> float:
    cand_emb = sentence_model.encode(candidate, convert_to_tensor=True)
    theme_emb = sentence_model.encode(theme, convert_to_tensor=True)
    cosine_score = util.pytorch_cos_sim(cand_emb, theme_emb)
    return cosine_score.item()


def lm_score(
    candidate: str,
    theme: str,
    prompt_template: str = "The theme is {theme}. A related word is [MASK].",
) -> float:
    prompt = prompt_template.format(theme=theme)
    results = fill_mask(prompt)
    for result in results:
        if result["token_str"].strip() == candidate:
            return result["score"]
    return 0.0


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
        overall_score = weight_sim * sim + weight_lm * lm_sc + weight_freq * freq
        ranked.append((candidate, positions, overall_score))

        if verbose:
            print(f"\t{candidate}: {overall_score}")
    ranked.sort(key=lambda x: x[2], reverse=True)
    return ranked
