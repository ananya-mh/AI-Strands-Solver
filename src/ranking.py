import numpy as np
from sentence_transformers import SentenceTransformer, util
from transformers import pipeline
from wordfreq import word_frequency

# Load a sentence-transformer model for context-dependent semantic similarity.
# Models like 'all-mpnet-base-v2' produce high-quality sentence embeddings.

# sentence_model = SentenceTransformer("all-mpnet-base-v2")
sentence_model = SentenceTransformer("all-MiniLM-L6-v2")


# Load a fill-mask pipeline (e.g., using BERT) for LM likelihood scoring.
fill_mask = pipeline("fill-mask", model="bert-base-uncased", framework="pt")


def semantic_similarity(candidate: str, theme: str) -> float:
    """
    Calculate cosine similarity between the candidate and the hint using sentence embeddings.

    Parameters:
        candidate (str): The candidate word or phrase.
        hint (str): The context or hint phrase.

    Returns:
        float: Cosine similarity score.
    """
    cand_emb = sentence_model.encode(candidate, convert_to_tensor=True)
    theme_emb = sentence_model.encode(theme, convert_to_tensor=True)
    cosine_score = util.pytorch_cos_sim(cand_emb, theme_emb)
    return cosine_score.item()


def lm_score(
    candidate: str,
    theme: str,
    prompt_template: str = "The theme is {theme}. A related word is [MASK].",
) -> float:
    """
    Score the candidate word/phrase using a masked language model.

    Parameters:
        candidate (str): The candidate word or phrase.
        hint (str): The hint phrase providing context.
        prompt_template (str): A prompt template that includes {hint} and a [MASK] token.

    Returns:
        float: The LM likelihood score for the candidate.
    """
    prompt = prompt_template.format(theme=theme)
    results = fill_mask(prompt)
    # Check if candidate appears in the predictions.
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
    """
    Rank candidate words/phrases using a weighted sum of semantic similarity, LM likelihood, and frequency.

    Parameters:
        candidates (list): List of tuples (candidate, positions).
        hint (str): The context-dependent hint phrase.
        freq_dict (dict): Dictionary mapping candidate (lowercase) to frequency score.
        weight_sim (float): Weight for semantic similarity.
        weight_lm (float): Weight for LM likelihood.
        weight_freq (float): Weight for frequency.

    Returns:
        list: Sorted list of tuples (candidate, positions, overall_score) in descending order.
    """
    ranked = []
    for candidate, positions in candidates:
        sim = semantic_similarity(candidate, hint)
        lm_sc = lm_score(candidate, hint)
        freq = word_frequency(candidate.lower(), "en", wordlist="large")
        overall_score = weight_sim * sim + weight_lm * lm_sc + weight_freq * freq
        # overall_score = weight_sim * sim + weight_freq * freq
        ranked.append((candidate, positions, overall_score))

        # if verbose:
        #     print(f"\t{candidate}: {overall_score}")
    ranked.sort(key=lambda x: x[2], reverse=True)
    return ranked
