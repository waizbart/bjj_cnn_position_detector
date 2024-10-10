[X] Encontrar melhor modelo de detecção de pose (Coco VS Movenet) \
    - [X] Testar Coco
    - [X] Testar Movenet
    - [X] Comparar resultados

    Resultados:
    - Coco é mais lento, porém muito mais preciso. Talvez isso pode ser melhorado com otimizações das diferentes versões do modelo.

[X] Explorar dataset de jiu jitsu e entender como os keypoints são anotados

[X] Testar Coco com imagens de jiu jitsu e comparar com keypoints das annotations
    - Obs: Resultados são semelhantes, porém não exatamente iguais, provavelmente o autor do dataset usou outro modelo

[X] Treinar modelo para classificar posições de jiu jitsu a partir dos keypoints
    - Resultado: +90% de precisão

[X] Usar modelo de detecção de keypoints "estado da arte" ViTPose baseado em transformers

[ ] Otimizar processo

[ ] Estabelecer novos métodos de coleta de dados e treinamento
