# Biobertology

**Setup**:

```
pip install biobert-pytorch==0.9 pytorch-transformers==1.2.0 torch==1.5.1
```

Ready to use [BioBert](https://arxiv.org/abs/1901.08746) pytorch weights for [HuggingFace](https://github.com/huggingface/transformers)
pytorch [BertModel](https://arxiv.org/abs/1810.04805).

To load the model:

```python
from biobertology import get_biobert, get_tokenizer

biobert = get_biobert(model_dir=None, download=True)
tokenizer = get_tokenizer()
```

Example of fine tuning biobert [here](https://github.com/MeRajat/SolvingAlmostAnythingWithBert/tree/master/biobert_ner).

## How was it converted to pytorch?

Model weights have been downloaded from [here](https://github.com/naver/biobert-pretrained/releases/tag/v1.1-pubmed) and converted

by following the commands described [here](https://github.com/huggingface/transformers/issues/457#issuecomment-518403170).pytorch

Specifically, using the command:

```
pytorch_transformers bert biobert_v1.1_pubmed/model.ckpt-1000000 biobert_v1.1_pubmed/bert_config.json biobert_v1.1_pubmed/pytorch_model.bin
```

followed by the renaming of the config file:

```
mv biobert_v1.1_pubmed/bert_config.json biobert_v1.1_pubmed/config.json
```

all of the other files inside the original weights file have been deleted.

## Learn more about Bert & Transformer

1. [The Illustrated Transformer](http://jalammar.github.io/illustrated-transformer/)

2. [The Annotated Transformer](http://nlp.seas.harvard.edu/2018/04/03/attention.html)

3. [BERT Word Embeddings Tutorial](https://mccormickml.com/2019/05/14/BERT-word-embeddings-tutorial/)