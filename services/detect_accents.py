import torchaudio
from speechbrain.pretrained import EncoderClassifier
from .config import accent_mapping

classifier = EncoderClassifier.from_hparams(source="Jzuluaga/accent-id-commonaccent_ecapa", 
                                            savedir="chkt")

index_to_label = {v: k for k, v in accent_mapping.items()}


def classify_accent(audio_path):

    out_prob, score, index, text_lab = classifier.classify_file(audio_path)
    probs = out_prob.squeeze().tolist()

    
    all_confidences = {index_to_label[i]: round(probs[i] * 100, 2) for i in range(len(probs))}

    top_label = text_lab[0]
    top_score = round(float(score[0]) * 100, 2)

    print(f"Predicted Accent: {top_label} | Confidence: {top_score:.2f}")
    print("All confidences:", all_confidences)

    return top_label, top_score, all_confidences
