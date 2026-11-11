# sparv-sbx-cefr-classification 

A plugin for [Sparv](https://spraakbanken.gu.se/sparv/) for classifying language learner texts.
The plugin accepts the following languages at the moment:
 - Swedish
 - Estonian
 - German
 - Portugese

**Note that this plugin does not guarantee full accuracy of predictions and the predictions should be taken as illustrative rather than as autorithative..**

## Install

1. Install [Sparv](https://spraakbanken.gu.se/sparv/):  
```
pipx install sparv
sparv setup
```

2. Clone this plugin's repository:  
```
git clone https://github.com/spraakbanken/sparv-sbx-cefr-classification
```

3. Inject the plugin into Sparv:  
```
pipx inject sparv /YOUR/PATH/TO/THE/PLUGIN/sparv-sbx-cefr-classification 
```

Alternatively to 2 & 3:
```
pipx inject sparv https://github.com/spraakbanken/sparv-sbx-cefr-classification/archive/main.zip
```

_In case you need to uninstall the plugin:_  
```
pipx runpip sparv uninstall sparv-sbx-cefr-classification 
```

## Usage

In your `config.yaml` file for corpus configuration, you can now specify `sparv-sbx-cefr-classification` as a text annotation. Effectively, you need to include the following elements in your corpus configuration:  

```
export:
  annotations:
    - <text>:sbx_cefr_classification.cefr_level
```

## Models

All of the models used in this plugin are BERT-like models. They can be found [here](https://hf.co/collections/rimusa/cefr-classification-models). See [this publication](https://aclanthology.org/2024.nlp4call-1.11/) for training details.  

See the webpage of the [CompSLA working group](https://spraakbanken.gu.se/en/compsla) for more information on the work we do on NLP for computational second language acquisition.

## Citing

If you use this plugin e.g. in a publication, please cite it as:

TODO

And

> Ricardo Muñoz Sánchez, David Alfter, Simon Dobnik, Maria Irena Szawerna, and Elena Volodina. 2024. Jingle BERT, Frozen All the Way: Freezing Layers to Identify CEFR Levels of Second Language Learners Using BERT. In Proceedings of the 13th Workshop on Natural Language Processing for Computer Assisted Language Learning, pages 137–152, Rennes, France. LiU Electronic Press.



