_base_ = 'faster_rcnn/faster_rcnn_r50_caffe_fpn_1x_coco.py'

model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=13)))

data_root = '/home/dhm/Data/RoboTHOR_Detection_Data/'

# Modify dataset related settings
dataset_type = 'RoboTHORDataset'
classes = (
    'AlarmClock', 'Apple', 'BaseballBat', 'BasketBall', 'Bowl', 'GarbageCan', 'HousePlant',
    'Laptop', 'Mug', 'RemoteControl', 'SprayBottle', 'Television', 'Vase',
)
data = dict(
    train=dict(
        img_prefix=data_root+'train/',
        classes=classes,
        ann_file='balloon/train/annotation_coco.json'),
    val=dict(
        img_prefix=data_root+'val/',
        classes=classes,
        ann_file='balloon/val/annotation_coco.json'),
    test=dict(
        img_prefix=data_root+'val/',
        classes=classes,
        ann_file='balloon/val/annotation_coco.json'))
