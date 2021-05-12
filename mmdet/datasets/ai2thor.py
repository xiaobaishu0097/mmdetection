from .builder import DATASETS
from pycocotools.coco import COCO
from .custom import CustomDataset

import numpy as np


@DATASETS.register_module()
class iTHORDataset(CustomDataset):

    CLASSES = (
        'AlarmClock', 'Book', 'Bowl', 'CellPhone', 'Chair', 'CoffeeMachine', 'DeskLamp', 'FloorLamp',
        'Fridge', 'GarbageCan', 'Kettle', 'Laptop', 'LightSwitch', 'Microwave', 'Pan', 'Plate', 'Pot',
        'RemoteControl', 'Sink', 'StoveBurner', 'Television', 'Toaster',
    )

    def load_annotations(self, ann_file):
        self.coco = COCO(ann_file)
        self.cat_ids = self.coco.getCatIds()
        self.cat2label = {
            cat_id: i + 1
            for i, cat_id in enumerate(self.cat_ids)
        }
        self.img_ids = self.coco.getImgIds()
        img_infos = []
        for i in self.img_ids:
            info = self.coco.loadImgs([i])[0]
            info['filename'] = info['file_name']
            img_infos.append(info)
        return img_infos

    def get_ann_info(self, idx):
        img_id = [self.img_infos[idx]['id']]
        anns = self.coco.dataset['annotations']
        ann_info = [ann for ann in anns if ann['image_id'] in img_id]

        bboxs = []
        labels = []

        for ann in ann_info:
            x1, y1, w, h = ann['bbox']
            bbox = [x1, y1, x1 + w - 1, y1 + h - 1]
            bboxs.append(bbox)
            labels.append(self.cat2label[ann['category_id']])

        bboxs = np.array(bboxs, dtype=np.float32)
        labels = np.array(labels, dtype=np.int64)

        assert bboxs.shape[0] == len(labels), 'data wrong!'

        ann = dict(
            bboxes=bboxs,
            labels=labels,
            bboxes_ignore=np.zeros((0, 4), dtype=np.float32),
        )

        return ann


@DATASETS.register_module()
class RoboTHORDataset(CustomDataset):

    CLASSES = (
        'AlarmClock', 'Apple', 'BaseballBat', 'BasketBall', 'Bowl', 'GarbageCan', 'HousePlant',
        'Laptop', 'Mug', 'RemoteControl', 'SprayBottle', 'Television', 'Vase',
    )

    def load_annotations(self, ann_file):
        self.coco = COCO(ann_file)
        self.cat_ids = self.coco.getCatIds()
        self.cat2label = {
            cat_id: i + 1
            for i, cat_id in enumerate(self.cat_ids)
        }
        self.img_ids = self.coco.getImgIds()
        img_infos = []
        for i in self.img_ids:
            info = self.coco.loadImgs([i])[0]
            info['filename'] = info['file_name']
            img_infos.append(info)
        return img_infos

    def get_ann_info(self, idx):
        img_id = [self.img_infos[idx]['id']]
        anns = self.coco.dataset['annotations']
        ann_info = [ann for ann in anns if ann['image_id'] in img_id]

        bboxs = []
        labels = []

        for ann in ann_info:
            x1, y1, w, h = ann['bbox']
            bbox = [x1, y1, x1 + w - 1, y1 + h - 1]
            bboxs.append(bbox)
            labels.append(self.cat2label[ann['category_id']])

        bboxs = np.array(bboxs, dtype=np.float32)
        labels = np.array(labels, dtype=np.int64)

        assert bboxs.shape[0] == len(labels), 'data wrong!'

        ann = dict(
            bboxes=bboxs,
            labels=labels,
            bboxes_ignore=np.zeros((0, 4), dtype=np.float32),
        )

        return ann


@DATASETS.register_module()
class InteractiveiTHORDataset(CustomDataset):

    CLASSES = (

    )

    def load_annotations(self, ann_file):
        self.coco = COCO(ann_file)
        self.cat_ids = self.coco.getCatIds()
        self.cat2label = {
            cat_id: i + 1
            for i, cat_id in enumerate(self.cat_ids)
        }
        self.img_ids = self.coco.getImgIds()
        img_infos = []
        for i in self.img_ids:
            info = self.coco.loadImgs([i])[0]
            info['filename'] = info['file_name']
            img_infos.append(info)
        return img_infos

    def get_ann_info(self, idx):
        img_id = [self.img_infos[idx]['id']]
        anns = self.coco.dataset['annotations']
        ann_info = [ann for ann in anns if ann['image_id'] in img_id]

        bboxs = []
        labels = []

        for ann in ann_info:
            x1, y1, w, h = ann['bbox']
            bbox = [x1, y1, x1 + w - 1, y1 + h - 1]
            bboxs.append(bbox)
            labels.append(self.cat2label[ann['category_id']])

        bboxs = np.array(bboxs, dtype=np.float32)
        labels = np.array(labels, dtype=np.int64)

        assert bboxs.shape[0] == len(labels), 'data wrong!'

        ann = dict(
            bboxes=bboxs,
            labels=labels,
            bboxes_ignore=np.zeros((0, 4), dtype=np.float32),
        )

        return ann
