## Explicação
#### LINK .pbix: https://drive.google.com/file/d/1RHwCQlga1-SuSzmfyiklbZeXBPZ8vfOK/view?usp=drive_link

O modelo OLAP foi desenvolvido com base nos objetivos de análise definidos, centralizando a tabela de fatos Fato_Desempenho, que armazena as principais medidas como notas das provas objetivas e redação. As tabelas de dimensões, como Dim_Aluno, Dim_Escola, Dim_Local_Prova, Dim_Socioeconômica, Dim_Tipo_Escola e Dim_Provas, foram criadas para armazenar atributos qualitativos que permitem segmentações e agrupamentos, como tipo de escola, localização geográfica, informações socioeconômicas e características das provas.

O modelo foi estruturado em um esquema estrela, com a tabela fato conectada às dimensões por chaves, garantindo eficiência nas consultas analíticas. A desnormalização das dimensões foi adotada para reduzir junções e otimizar o desempenho. As medidas, como médias e somatórios de notas, foram escolhidas para atender às análises de desempenho por fatores geográficos, socioeconômicos e características demográficas. As dimensões foram enriquecidas para permitir uma visão detalhada dos dados, enquanto as hierarquias criadas, como região → estado → município, facilitam análises em diferentes níveis de agregação.

Utilizei o algoritmo em Python fornecido acima para extrair as tabelas com as dimensões e os fatos do conjunto de dados. As colunas foram organizadas de acordo com o modelo, resultando em tabelas CSV que representam a tabela fato e as tabelas dimensão.

Em seguida, importei essas tabelas para o Power BI, estabelecendo as relações entre elas com base nas chaves primárias e estrangeiras definidas no modelo. Ao fazer isso, ajustei e formatei as tabelas, conforme necessário, para resolver problemas como duplicatas e garantir a consistência das relações. Assim, o ambiente foi configurado para permitir análises multidimensionais e consultas eficientes, alinhadas aos objetivos definidos inicialmente.








