from sparv.api import Annotation, Output, annotator, Language, get_logger

from datasets.arrow_dataset import Dataset
import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers.trainer import Trainer
import numpy as np
#from transformers.trainer import Trainer
#from datasets import Dataset


logger = get_logger(__name__)


@annotator("Assign each document a CEFR level",
           language=["est"]
           )

def cefr_level_classifier(
    text: Annotation = Annotation("<text>"),
    out: Output = Output("<text>:sbx_cefr_classification.cefr_level",description="The CEFR level as a string"),
    lang: Language = Language(),
    ):

    txt = [i for i in text.read_text()]

    predictions = inference(text.read_text(), lang)

    out.write(predictions)
    # Inference is in another function for easy debugging/development purposes
    #cefr_levels = inference(text, lang)
    #out.write(cefr_levels)


def inference(text,lang):

    # The model used depends on the language
    model_name = MODELS[lang]

    # Load model and tokenizer
    tokenizer =  AutoTokenizer.from_pretrained(model_name, do_lower_case=True)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)

    # Tokenizer function
    def tokenize_function(examples):
        return tokenizer(examples['text'], padding="max_length", max_length=255, truncation=True)

    # I'm assuming we need the text as a list
    if isinstance(text, str):
        text = [text]

    # Tokenize the data
    example = Dataset.from_pandas(pd.DataFrame({"text":text}))
    tokenized_example = example.map(tokenize_function)

    # Inference step
    trainer = Trainer(model=model)

    # Get predictions out of logits
    logits = trainer.predict(tokenized_example)[0]
    pred_ids = np.argmax(logits,axis=1)
    predictions = [model.config.id2label[p] for p in pred_ids]

    return predictions



MODELS = {
    "est": "sprakbanken-se/estbert-estonian_CEFR-classification",
    "deu": "sprakbanken-se/bert-base-german_CEFR-classification",
    "por": "sprakbanken-se/portbert-portuguese_CEFR-classification",
    "swe": "sprakbanken-se/KB-bert-swedish_CEFR-classification",
}