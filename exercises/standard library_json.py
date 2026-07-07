import json

config = {
    "model_name": "ResNet50",
    "learning_rate": 0.001,
    "batch_size": 32,
    "optimizer": "Adam",
    "device": "cuda:0"
    }

with open('config.json', 'w') as f:
    json.dump(config, f, indent=4)
    
with open("config.json", "r") as f:
    loaded_config = json.load(f)
    
print(loaded_config["learning_rate"])

'''
with open("dataset.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# {"images": [{"id": 1, "file_name": "001.jpg"}, ...]}
for img in data["images"]:
    print(f"Processing {img['file_name']}...")
'''
