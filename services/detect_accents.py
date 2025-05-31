from .config import accent_mapping
from models import accent_classifier_model

index_to_label = {v: k for k, v in accent_mapping.items()}


def classify_accent(audio_path):
    """
    Classify the accent of the given audio file.

    """

    out_prob, score, index, text_lab = accent_classifier_model.classify_file(audio_path)
    probs = out_prob.squeeze().tolist()
    
    all_confidences = {index_to_label[i]: float(probs[i]) for i in range(len(probs))}

    top_label = text_lab[0]
    top_score = float(score[0])
    return top_label, top_score, all_confidences
