import io
import torch
import torchvision.transforms as transforms
from fastapi import FastAPI, File, UploadFile
from PIL import Image
from torchvision.models import resnet101

# Initialize FastAPI app
app = FastAPI(title="Plant Disease Detection API")

# Load the model
MODEL_PATH = "model/ResNet_101_ImageNet_plant-model-84.pth"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = resnet101(pretrained=False)
# Adjust the final fully connected layer according to your number of classes
num_classes = 20  # Change this to match your model's output classes
model.fc = torch.nn.Linear(model.fc.in_features, num_classes)
model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
model.to(device)
model.eval()

# Define the image transformations
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Define the class labels
class_labels = [
    "Apple Aphis spp", "Apple Erisosoma lanigerum",
    "Apple Monillia laxa", "Apple Venturia inaequalis",
    "Apricot Coryneum beijerinckii", "Apricot Monillia laxa",
    "Cancer symptom", "Cherry Aphis spp",
    "Downy mildew", "Drying symptom",
    "Gray mold", "Leaf scars",
    "Peach Monillia laxa", "Peach Parthenolecanium corni",
    "Pear Erwinia amylovora", "Plum Aphis spp",
    "RoughBark", "StripeCanker",
    "Walnut Eriophyies erineus", "Walnut Gnomonialeptostyla",
]

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Read and preprocess the image
    image_data = await file.read()
    image = Image.open(io.BytesIO(image_data)).convert('RGB')
    image_tensor = transform(image).unsqueeze(0).to(device)

    # Make prediction
    with torch.no_grad():
        outputs = model(image_tensor)
        _, predicted = torch.max(outputs, 1)

    # Get the predicted class label
    predicted_class = class_labels[predicted.item()]

    return {"predicted_disease": predicted_class}
    #return JSONResponse(content={"predicted_disease": predicted_class})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)