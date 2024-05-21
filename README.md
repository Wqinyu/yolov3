# 基于YOLO_v3的目标检测



## 数据处理

下载voc数据集至data文件夹中在运用数据集转换脚本将VOC格式数据转换为COCO数据，随后调整数据集标签等相关配置


## 训练模型

在调整参数后，运用如下命令行实现训练
```bash
python tools/train.py configs/yolo/yolov3_d53_8xb8-ms-608-273e_coco.py
```
## 训练情况的可视化
运行draw.py实现训练Loss曲线和验证集map的可视化
```bash
python tools/train.py configs/yolo/yolov3_d53_8xb8-ms-608-273e_coco.py
```
## 测试
测试文件在test.ipynb中，测试图片在test文件夹中，返回结果在test_pred文件夹中



