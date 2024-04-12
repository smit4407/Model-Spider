from torchvision.datasets import ImageFolder


class AID(ImageFolder):
    """ Aerial Image Dataset (AID) from 'AID: A Benchmark Dataset for Performance
    Evaluation of Aerial Scene Classification', Xia et al. (2017)
    https://arxiv.org/abs/1608.05167
    'The AID dataset has a number of 10000 images within 30 classes.'
    .data/AID
    """
    def __init__(
        self,
        root: str,
        transform
    ):
        super().__init__(
            root=root,
            transform=transform
        )