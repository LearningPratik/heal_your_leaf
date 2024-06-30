import base64
import torch
from torchvision import transforms, datasets
from PIL import Image


def Classifier(image, model, class_name):

    # image = Image.open(image)

    transformer = transforms.Compose([
        transforms.Resize(size=(128, 128)),
        transforms.ToTensor()
    ])
    
    transformed_image = transformer(image).unsqueeze(0)

    model.eval()

    with torch.inference_mode():
        pred_logit = model(transformed_image)
        pred_prob = torch.softmax(pred_logit, dim=1)
        pred_label = torch.argmax(pred_prob, dim=1)
        pred_class = class_name[pred_label]

    return pred_class