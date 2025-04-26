[X] Encontrar melhor modelo de detecção de pose (Coco VS Movenet) \
    - [X] Testar Coco
    - [X] Testar Movenet
    - [X] Comparar resultados

    Resultados:
    - Coco é mais lento, porém muito mais preciso. Talvez isso pode ser melhorado com otimizações das diferentes versões do modelo.

[X] Explorar dataset de jiu jitsu e entender como os keypoints são anotados

[X] Testar Coco com imagens de jiu jitsu e comparar com keypoints das annotations
    - Obs: Resultados são semelhantes, porém não exatamente iguais, provavelmente o autor do dataset usou outro modelo
    - Foi usado o VitPose

[X] Treinar modelo para classificar posições de jiu jitsu a partir dos keypoints
    - Resultado: +90% de precisão

[X] Usar modelo de detecção de keypoints "estado da arte" ViTPose baseado em transformers

[X] Otimizar processo

[] Estabelecer novos métodos de coleta de dados e treinamento

[] Implementar análise de sequências temporais
    - [] Desenvolver detector de sequências de keypoints
    - [] Extrair características de movimento (velocidade, aceleração)
    - [] Criar dataset de sequências de movimentos anotadas
    - [] Treinar modelo LSTM para classificação de movimentos

[] Expandir as classes de movimentos e transições
    - [] Adicionar transições entre posições (ex: passagem de guarda)
    - [] Incluir finalizações e defesas
    - [] Classificar sweeps (raspagens) e escapes
    - [] Detectar movimentos de transição vs. posições estáticas

[] Avaliação e validação do sistema de análise temporal
    - [] Criar métricas de avaliação específicas para sequências
    - [] Comparar desempenho entre arquiteturas (LSTM vs Transformer)
    - [] Validar com especialistas (professores de BJJ)
    - [] Testar em competições reais

[] Interfaces e visualizações
    - [] Desenvolver interface para visualização de transições
    - [] Criar gráficos de fluxo de movimento
    - [] Implementar linha do tempo com classificações
    - [] Exportar análises para instrutores e atletas

[] Integração com o sistema atual
    - [] Unificar detector de posições estáticas e movimentos
    - [] Harmonizar APIs para suportar ambas análises
    - [] Atualizar a documentação com os novos recursos
