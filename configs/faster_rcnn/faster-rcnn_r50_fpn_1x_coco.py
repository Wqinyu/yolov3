_base_ = [
    '../_base_/models/faster-rcnn_r50_fpn.py',
    '../_base_/datasets/coco_detection.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]

log_config = dict(
    interval=50,  # 每50个batch打印一次日志
    hooks=[
        dict(type='TensorboardLoggerHook'),  # 启用 Tensorboard 日志记录
        dict(type='TextLoggerHook')  # 同时启用文本日志，以在控制台输出训练信息
    ])

classes = ('aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car',
           'cat', 'chair', 'cow', 'diningtable', 'dog', 'horse',
           'motorbike', 'person', 'pottedplant', 'sheep', 'sofa', 'train',
           'tvmonitor')

evaluation = dict(interval=1, metric='mAP')



