import json

with open('jiu_annotations.json', 'r') as file:
    annotations = json.load(file)
    
n_per_class = {}

for annotation in annotations:
    label = annotation['position']
    
    if label not in n_per_class:
        n_per_class[label] = 0

    n_per_class[label] += 1
    
print(n_per_class)