_base_ = 'faster_rcnn/faster_rcnn_r50_caffe_fpn_1x_coco.py'

model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=22)))

data_root = '/home/dhm/Data/iThor_Detection_Data/'

# Modify dataset related settings
dataset_type = 'iTHORDataset'
classes = (
    'AlarmClock', 'Book', 'Bowl', 'CellPhone', 'Chair', 'CoffeeMachine', 'DeskLamp', 'FloorLamp',
    'Fridge', 'GarbageCan', 'Kettle', 'Laptop', 'LightSwitch', 'Microwave', 'Pan', 'Plate', 'Pot',
    'RemoteControl', 'Sink', 'StoveBurner', 'Television', 'Toaster',
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
