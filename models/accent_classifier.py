from speechbrain.pretrained import EncoderClassifier

accent_classifier_model = EncoderClassifier.from_hparams(source="Jzuluaga/accent-id-commonaccent_ecapa", 
                                            savedir="chkt")
