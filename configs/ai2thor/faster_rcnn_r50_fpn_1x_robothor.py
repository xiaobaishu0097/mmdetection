_base_ = '../faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py'

model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=14)))

# Modify dataset related settings
dataset_type = 'RoboTHORDataset'
data_root = '/home/duhm/Data/RoboTHOR_Detection_Data/'
classes = (
    'AlarmClock', 'Apple', 'BaseballBat', 'BasketBall', 'Bowl', 'GarbageCan', 'HousePlant',
    'Laptop', 'Mug', 'RemoteControl', 'SprayBottle', 'Television', 'Vase',
)
data = dict(
    train=dict(
        img_prefix=data_root+'train/',
        classes=classes,
        ann_file=data_root+'annotations/instances_train.json'),
    val=dict(
        img_prefix=data_root+'val/',
        classes=classes,
        ann_file=data_root+'annotations/instances_val.json'),
    test=dict(
        img_prefix=data_root+'val/',
        classes=classes,
        ann_file=data_root+'annotations/instances_val.json'))
