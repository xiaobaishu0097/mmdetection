_base_ = '../faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py'

model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=22)))

# Modify dataset related settings
dataset_type = 'iTHORDataset'
data_root = '/home/duhm/Data/iTHOR_Detection_Data/'
classes = (
    'AlarmClock', 'Book', 'Bowl', 'CellPhone', 'Chair', 'CoffeeMachine', 'DeskLamp', 'FloorLamp',
    'Fridge', 'GarbageCan', 'Kettle', 'Laptop', 'LightSwitch', 'Microwave', 'Pan', 'Plate', 'Pot',
    'RemoteControl', 'Sink', 'StoveBurner', 'Television', 'Toaster',
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

runner = dict(max_epochs=4)
