# Vision Transformer

An implementation of a simple vision transformer in PyTorch.

Trained on the [Oxford-IIIT Pets dataset](https://www.kaggle.com/datasets/tomasfern/oxford-iit-pets) to recognize dog and cat breeds.

Running clean_dataset.py puts images of different breeds of dogs and cats into different folders to use PyTorch's ImageFolder data loader. (All images are in a single folder in the Kaggle dataset)

ViT Paper: [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/abs/2010.11929)