import os
from biobertology.download import get_default_biobert_path, download_and_extract
from pytorch_transformers import BertTokenizer, BertModel

MODEL_DIR = os.path.join(get_default_biobert_path(), "biobert_v1.1_pubmed")
VOCAB_FILE = os.path.join(MODEL_DIR, "vocab.txt")


def _load_model(model_dir):
    assert os.path.exists(model_dir)
    model = BertModel.from_pretrained(model_dir)
    return model


def get_biobert(model_dir=None, download=False):
    """
    Loads biobert model, if weights are not available it will download it
    :param model_dir: Location where model weights are stored or should be downloaded to
    :param download: If model weights should be downloaded
    :return: HuggingFace BertModel
    """
    if (model_dir == None) and (download == False):
        model_dir = MODEL_DIR

    if (model_dir == None) and (download == True):
        download_and_extract(get_default_biobert_path())
        model_dir = MODEL_DIR

    if model_dir and (download == True):
        download_and_extract(model_dir)
        model_dir = os.path.join(model_dir, "biobert_v1.1_pubmed")

    if model_dir and (download == False):
        model_dir = os.path.join(model_dir, "biobert_v1.1_pubmed")

    return _load_model(model_dir)


def get_tokenizer(vocab_file=None):
    vocab_file = VOCAB_FILE if vocab_file is None else vocab_file
    os.path.isfile(vocab_file)
    tokenizer = BertTokenizer(vocab_file=vocab_file, do_lower_case=False)
    return tokenizer
