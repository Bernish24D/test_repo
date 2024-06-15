import torch
import torchvision.transforms as T
from torchvision.models.detection import maskrcnn_resnet50_fpn
from PIL import Image, ImageDraw

def instance_segmentation(image_path):
    # Load image
    image = Image.open(image_path).convert("RGB")
    
    # Define the transform
    transform = T.Compose([T.ToTensor()])

    # Apply the transform to the image
    image_tensor = transform(image)

    # Load pre-trained Mask R-CNN model
    model = maskrcnn_resnet50_fpn(pretrained=True)
    model.eval()

    # Forward pass to get predictions
    with torch.no_grad():
        prediction = model([image_tensor])

    # Draw masks on the image
    draw = ImageDraw.Draw(image)
    masks = prediction[0]['masks']
    for i in range(masks.shape[0]):
        mask = masks[i, 0].mul(255).byte().cpu().numpy()
        mask_img = Image.fromarray(mask)
        image.paste(mask_img, (0, 0), mask_img.convert('L').point(lambda p: p * 0.5))



    # Display the result
    image.show()

# Path to the input image
image_path = 'sam.jpg'

# Perform instance segmentation on the image
instance_segmentation(image_path)
