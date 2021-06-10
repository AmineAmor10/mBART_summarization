# mBART_summarization

## Description




## How to run the project

To run this project, clone the repo and execute the following commands: 
1) cd mbart_summarization
2) pip install -r requirements.txt
3) mkdir long_wiki_fr 
4) python get_wiki_long_fr_data.py 
5) bash tune_mBART.sh


## Citation

@inproceedings{wolf-etal-2020-transformers,
    title = "Transformers: State-of-the-Art Natural Language Processing",
    author = "Wolf, Thomas  and
      Debut, Lysandre  and
      Sanh, Victor  and
      Chaumond, Julien  and
      Delangue, Clement  and
      Moi, Anthony  and
      Cistac, Pierric  and
      Rault, Tim  and
      Louf, Remi  and
      Funtowicz, Morgan  and
      Davison, Joe  and
      Shleifer, Sam  and
      von Platen, Patrick  and
      Ma, Clara  and
      Jernite, Yacine  and
      Plu, Julien  and
      Xu, Canwen  and
      Le Scao, Teven  and
      Gugger, Sylvain  and
      Drame, Mariama  and
      Lhoest, Quentin  and
      Rush, Alexander",
    booktitle = "Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing: System Demonstrations",
    month = oct,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.emnlp-demos.6",
    doi = "10.18653/v1/2020.emnlp-demos.6",
    pages = "38--45",
    abstract = "Recent progress in natural language processing has been driven by advances in both model architecture and model pretraining. Transformer architectures have facilitated building higher-capacity models and pretraining has made it possible to effectively utilize this capacity for a wide variety of tasks. Transformers is an open-source library with the goal of opening up these advances to the wider machine learning community. The library consists of carefully engineered state-of-the art Transformer architectures under a unified API. Backing this library is a curated collection of pretrained models made by and available for the community. Transformers is designed to be extensible by researchers, simple for practitioners, and fast and robust in industrial deployments. The library is available at https://github.com/huggingface/transformers.",
}
