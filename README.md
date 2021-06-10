# mBART_summarization

## Description

BART is a denoising auto-encoder that jointly pretrains a bidirectional encoder (similar to BERT) and a forward autoregressive decoder (similar to GPT) by learning to reconstruct a corrupted input sequence. mBART is the multilingual version and was trained on 25 languages.

In this project, mBART is fine-tuned on a summarization dataset, which was generated from wikipedia articles in french. For text generation, some key parameters were amended to improve rouge-scores on wikipedia summaries. More specifically, num_beams = 8, max_length = 1024, min_length = 80 and no_repeat_ngram_size = 3.

This project was built using HuggingFace library.

## How to run the project

To run this project, clone the repo and execute the following commands: 
1) cd mbart_summarization
2) pip install -r requirements.txt
3) mkdir long_wiki_fr 
4) python get_wiki_long_fr_data.py 
5) bash tune_mBART.sh


## Citation

@article{DBLP:journals/corr/abs-1910-03771,<br/>
&nbsp;&nbsp;&nbsp;&nbsp;  author    = {Thomas Wolf and
               Lysandre Debut and
               Victor Sanh and
               Julien Chaumond and
               Clement Delangue and
               Anthony Moi and
               Pierric Cistac and
               Tim Rault and
               R{\'{e}}mi Louf and
               Morgan Funtowicz and
               Jamie Brew},<br/>
&nbsp;&nbsp;&nbsp;&nbsp;  title     = {HuggingFace's Transformers: State-of-the-art Natural Language Processing},<br/>
&nbsp;&nbsp;&nbsp;&nbsp;  journal   = {CoRR},<br/>
&nbsp;&nbsp;&nbsp;&nbsp;  volume    = {abs/1910.03771},<br/>
&nbsp;&nbsp;&nbsp;&nbsp;  year      = {2019},<br/>
&nbsp;&nbsp;&nbsp;&nbsp;  url       = {http://arxiv.org/abs/1910.03771},<br/>
&nbsp;&nbsp;&nbsp;&nbsp;  archivePrefix = {arXiv},<br/>
&nbsp;&nbsp;&nbsp;&nbsp;  eprint    = {1910.03771},<br/>
&nbsp;&nbsp;&nbsp;&nbsp;  timestamp = {Tue, 02 Jun 2020 12:49:01 +0200},<br/>
&nbsp;&nbsp;&nbsp;&nbsp;  biburl    = {https://dblp.org/rec/journals/corr/abs-1910-03771.bib},<br/>
&nbsp;&nbsp;&nbsp;&nbsp;  bibsource = {dblp computer science bibliography, https://dblp.org}<br/>
}


@article{DBLP:journals/corr/abs-1910-13461,<br/>
&nbsp;&nbsp;&nbsp;&nbsp;  author    = {Mike Lewis and
               Yinhan Liu and
               Naman Goyal and
               Marjan Ghazvininejad and
               Abdelrahman Mohamed and
               Omer Levy and
               Veselin Stoyanov and
               Luke Zettlemoyer},<br/>
&nbsp;&nbsp;&nbsp;&nbsp;  title     = {{BART:} Denoising Sequence-to-Sequence Pre-training for Natural Language
               Generation, Translation, and Comprehension},<br/>
&nbsp;&nbsp;&nbsp;&nbsp;  journal   = {CoRR},<br/>
&nbsp;&nbsp;&nbsp;&nbsp;  volume    = {abs/1910.13461},<br/>
&nbsp;&nbsp;&nbsp;&nbsp;  year      = {2019},<br/>
&nbsp;&nbsp;&nbsp;&nbsp;  url       = {http://arxiv.org/abs/1910.13461},<br/>
&nbsp;&nbsp;&nbsp;&nbsp;  archivePrefix = {arXiv},<br/>
&nbsp;&nbsp;&nbsp;&nbsp;  eprint    = {1910.13461},<br/>
&nbsp;&nbsp;&nbsp;&nbsp;  timestamp = {Thu, 31 Oct 2019 14:02:26 +0100},<br/>
&nbsp;&nbsp;&nbsp;&nbsp;  biburl    = {https://dblp.org/rec/journals/corr/abs-1910-13461.bib},<br/>
&nbsp;&nbsp;&nbsp;&nbsp;  bibsource = {dblp computer science bibliography, https://dblp.org}<br/>
}

