



import os, time, torch

from torchvision import models, transforms
from torch import nn, optim
from Trainer import Trainer
from Loss import LDAMLoss
from Data.Organiser import Organiser

data = {
    "train": ["/home/wesley/Snaked/train", "/work/data/Line_bot/final/Snaked/src/train_labels.csv", 0, 0.95],
    "validation": ["/home/wesley/Snaked/train", "/work/data/Line_bot/final/Snaked/src/train_labels.csv", 0.95, 1],
   "test": ["/home/wesley/Snaked/train", "/work/data/Line_bot/final/Snaked/src/train_labels.csv", 0.975, 1]
}

image_transforms = {
    "train":
    transforms.Compose([
        transforms.RandomResizedCrop(size=256, scale=(0.8, 1)),
        transforms.RandomRotation(90),
        transforms.ColorJitter(),
        transforms.RandomHorizontalFlip(),
        transforms.RandomVerticalFlip(),
        transforms.CenterCrop(size=224), #ImgNet standards
        transforms.ToTensor(),
        transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225)), # ImgNet standards
    ]),
    "validation":
    transforms.Compose([
        transforms.Resize(size=256),
        transforms.CenterCrop(size=224), #ImgNet standards
        transforms.ToTensor(),
        transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225)), # ImgNet standards
    ]),
    "test":
    transforms.Compose([
        transforms.Resize(size=256),
        transforms.CenterCrop(size=224), #ImgNet standards
        transforms.ToTensor(),
        transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225)), # ImgNet standards
    ])
}


organiser = Organiser(data, image_transforms)

def default_trainer(model, path, batch_size, lr=3e-3, find_lr=False):
    data_loaders = organiser.get_loaders(batch_size=batch_size)
    criterion = nn.CrossEntropyLoss()
    criterion = LDAMLoss(organiser.label_counts)
    optimizer = optim.AdamW(model.parameters())
    scheduler = optim.lr_scheduler.OneCycleLR(optimizer, lr, epochs=10, steps_per_epoch=len(data_loaders["train"]))
    organiser.create_folder(path)
    trainer = Trainer(model, criterion, optimizer, scheduler, path, data_loaders)
    if find_lr == True:
        trainer.find_lr()
    return trainer


def predict(imgpath=None):
    organiser = Organiser(data, image_transforms)

    # MobileNet V2 model
    # Note max learning rate of 3e-4 works best for cross entropy loss and 5e-4 for LDAM loss
#     print("Training MobileNet V2 model - " + str(time.strftime("%Y-%m-%d %H:%M:%S")))
    model = models.mobilenet_v2(pretrained=True)
    model.classifier[1] = nn.Linear(model.classifier[1].in_features, 85)
    # pdb.set_trace()
    trainer = default_trainer(model, "/work/data/Line_bot/final/Snaked/Saved/Model", 64, 5e-4)
    # trainer.train()
    # trainer.evaluate()
    trainer.predict(img_path='../cobra.jpg')

