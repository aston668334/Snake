import os, time, torch
from torchvision import models, transforms
from torch import nn, optim
from Trainer import Trainer
from Loss import LDAMLoss
from Data.Organiser import Organiser
import pdb
os.chdir('/work/data/Line_bot/final/Snaked/src/')
#!/usr/bin/env python
# coding: utf-8

class model_predict():

    def __init__(self):
        self.data = {
            "train": ["/home/wesley/Snaked/train", "/work/data/Line_bot/final/Snaked/src/train_labels.csv", 0, 0.95],
            "validation": ["/home/wesley/Snaked/train", "/work/data/Line_bot/final/Snaked/src/train_labels.csv", 0.95, 1],
           "test": ["/home/wesley/Snaked/train", "/work/data/Line_bot/final/Snaked/src/train_labels.csv", 0.975, 1]
        }

        self.image_transforms = {
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

        self.organiser = Organiser(self.data, self.image_transforms)
    
    
    
    def default_trainer(self,model, path, batch_size, lr=3e-3, find_lr=False):
        data_loaders = self.organiser.get_loaders(batch_size=batch_size)
        criterion = nn.CrossEntropyLoss()
        criterion = LDAMLoss(self.organiser.label_counts)
        optimizer = optim.AdamW(model.parameters())
        scheduler = optim.lr_scheduler.OneCycleLR(optimizer, lr, epochs=10, steps_per_epoch=len(data_loaders["train"]))
        self.organiser.create_folder(path)
        trainer = Trainer(model, criterion, optimizer, scheduler, path, data_loaders)
        if find_lr == True:
            trainer.find_lr()
        return trainer



    def predict(self,img):
        
        organiser = Organiser(self.data, self.image_transforms)

        # MobileNet V2 model
        # Note max learning rate of 3e-4 works best for cross entropy loss and 5e-4 for LDAM loss
        print("Training MobileNet V2 model - " + str(time.strftime("%Y-%m-%d %H:%M:%S")))
        model = models.mobilenet_v2(pretrained=True)
        model.classifier[1] = nn.Linear(model.classifier[1].in_features, 85)
        # pdb.set_trace()
        trainer = self.default_trainer(model, "/work/data/Line_bot/final/Snaked/Saved/Model", 64, 5e-4)
        # trainer.train()
        # trainer.evaluate()
        species = trainer.predict(img)
        return(species)