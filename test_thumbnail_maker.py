from thumbnail_maker import ThumbnailMakerService
import logging

# Images taken from https://github.com/cvdfoundation/open-images-dataset
IMG_URLS = \
    ['https://open-images-dataset.s3.amazonaws.com/train/000002b66c9c498e.jpg',
     'https://open-images-dataset.s3.amazonaws.com/train/000002b97e5471a0.jpg',
     'https://open-images-dataset.s3.amazonaws.com/train/000002c707c9895e.jpg',
     'https://open-images-dataset.s3.amazonaws.com/train/0000048549557964.jpg',
     'https://open-images-dataset.s3.amazonaws.com/train/000004f4400f6ec5.jpg',
     'https://open-images-dataset.s3.amazonaws.com/train/0000071d71a0a6f6.jpg',
     'https://open-images-dataset.s3.amazonaws.com/train/000013ba71c12506.jpg',
     'https://open-images-dataset.s3.amazonaws.com/train/000018acd19b4ad3.jpg',
     'https://open-images-dataset.s3.amazonaws.com/train/00001bc2c4027449.jpg',
     'https://open-images-dataset.s3.amazonaws.com/train/00001bcc92282a38.jpg',
     'https://open-images-dataset.s3.amazonaws.com/train/0000201cd362f303.jpg',
     'https://open-images-dataset.s3.amazonaws.com/train/000020780ccee28d.jpg',
     'https://open-images-dataset.s3.amazonaws.com/train/000023aa04ab09ed.jpg',
     'https://open-images-dataset.s3.amazonaws.com/train/0000253ea4ecbf19.jpg',
     'https://open-images-dataset.s3.amazonaws.com/train/000025ea48cab6fc.jpg',
     'https://open-images-dataset.s3.amazonaws.com/train/0000271195f2c007.jpg',
     'https://open-images-dataset.s3.amazonaws.com/train/0000286a5c6a3eb5.jpg',
     'https://open-images-dataset.s3.amazonaws.com/train/00002b368e91b947.jpg',
     'https://open-images-dataset.s3.amazonaws.com/train/00002f4ff380c64c.jpg',
     'https://open-images-dataset.s3.amazonaws.com/train/0000313e5dccf13b.jpg',
     'https://open-images-dataset.s3.amazonaws.com/train/000032046c3f8371.jpg',
     'https://open-images-dataset.s3.amazonaws.com/train/00003223e04e2e66.jpg',
     'https://open-images-dataset.s3.amazonaws.com/train/0000333f08ced1cd.jpg',
     'https://open-images-dataset.s3.amazonaws.com/train/000033469fb48bc1.jpg'
    ]
    
def test_thumbnail_maker(caplog):
    caplog.set_level(logging.DEBUG)
    tn_maker = ThumbnailMakerService()
    tn_maker.make_thumbnails(IMG_URLS)
