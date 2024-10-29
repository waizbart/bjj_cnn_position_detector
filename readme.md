# Dataset to download https://vicos.si/resources/jiujitsu/

# Pipelines versions
- v1: Versão inicial com treinamento usando somente uma pessoa na imagens
- v2: Treinamento utilizando todas as pessoas na imagem e COCO dataset
- v3: Tentativa de treinamento com somente valores x e y, sem o score
- v4: Duplicando keypoints do dataset inicial usando posições invertidas para os dois lutadores
- v5: Adicionando augmentation ao pré-processamento dos keypoints