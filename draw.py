import json
import matplotlib.pyplot as plt

def parse_json_log(json_file):
    train_losses = []
    val_mAP_50s = []

    with open(json_file, 'r') as f:
        for line in f:
            data = json.loads(line)
            if 'loss' in data and 'iter' in data:
                train_losses.append(data['loss'])
            elif 'coco/bbox_mAP' in data:
                val_mAP_50s.append(data['coco/bbox_mAP_50'])

    return train_losses, val_mAP_50s

def plot_loss_and_mAP(train_losses, val_mAP_50s):
    train_epochs = list(range(1, len(train_losses) + 1))
    val_epochs = list(range(1, len(val_mAP_50s)  + 1))

    plt.figure(figsize=(10, 5))

    # Plot train loss
    plt.plot(train_epochs, train_losses, label='Train Loss', color='blue')
    plt.xlabel('50 iterations')
    plt.ylabel('Loss')
    plt.title('Training Loss')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.savefig("train_loss.png")
    plt.show()

    # Plot validation mAP@50
    plt.figure(figsize=(10, 5))
    plt.plot(val_epochs, val_mAP_50s, label='Validation mAP@50', color='green')
    plt.xlabel('7 Epochs')
    plt.ylabel('mAP@50')
    plt.title('Validation mAP@50')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.savefig("map.png")
    plt.show()


json_file = 'D:\PycharmProjects\mmdetection\work_dirs\yolov3_d53_8xb8-ms-608-273e_coco\\20240419_205006\\vis_data\\20240419_205006.json'
train_losses, val_mAP_50s = parse_json_log(json_file)
plot_loss_and_mAP(train_losses, val_mAP_50s)





