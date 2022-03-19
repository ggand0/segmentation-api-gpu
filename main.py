import os, torch, encoding
import torchvision.transforms as transform
from PIL import Image
import numpy as np

def load_model():
    model_name = 'DeepLab_ResNeSt269_ADE'
    model = encoding.models.get_model(model_name, pretrained=True)
    return model.eval().cuda()

def infer(image, model):
    input_transform = transform.Compose([
        transform.ToTensor(),
        transform.Normalize([.485, .456, .406], [.229, .224, .225])])
    img = input_transform(image).unsqueeze(0).cuda()

    with torch.no_grad():
        output = model.evaluate(img)
    pred = torch.max(output, 1)[1].cpu().numpy() + 1
    
    mask = encoding.utils.get_mask_pallete(pred, 'ade20k')
    mask.convert('RGB').save('pred.jpg', 'JPEG', quality=95)

if __name__ == '__main__':
    image = Image.open('sample_image.jpg')
    print(np.array(image).shape)
    model = load_model()
    infer(image, model)
    print('DONE.')