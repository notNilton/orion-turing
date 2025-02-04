# Aplicação do Algoritmo A⋆ no Quebra-Cabeça de 8 Peças

Este documento constitui a primeira avaliação prática da disciplina de Inteligência Artificial, ministrada no ano de 2024 na Universidade Federal de Mato Grosso (UFMT). O trabalho tem como tema central a aplicação do algoritmo **A⋆** na resolução do **quebra-cabeça de 8 peças**, um problema clássico na área de busca em inteligência artificial.

A atividade é de caráter individual, cabendo a cada discente desenvolver sua própria solução, seguindo as diretrizes e critérios estabelecidos.

## O Quebra-Cabeça de 8 Peças

O quebra-cabeça de 8 peças consiste em uma matriz **3×3** composta por 8 células quadradas numeradas de **1 a 8** e uma célula vazia (em branco). O objetivo do jogo é reorganizar as peças, por meio de movimentos válidos, até que a matriz atinja uma configuração ordenada. Movimentos válidos são aqueles realizados horizontalmente ou verticalmente (não diagonalmente), deslizando uma peça adjacente para a posição vazia.

A Figura 1 ilustra um exemplo de sequência de movimentos válidos que levam à solução do quebra-cabeça.

![Exemplo de solução do quebra-cabeça de 8 peças](#)  
*Figura 1: Exemplo de solução do quebra-cabeça de 8 peças.*

## Tarefas do Trabalho

O trabalho está estruturado em quatro tarefas principais, cada uma com objetivos específicos e pontuação definida, conforme detalhado a seguir:

### 1. Remoção de Estados Repetitivos
Nesta tarefa, o aluno deve modificar a implementação do algoritmo **A⋆** para evitar a inclusão de estados já visitados durante a busca. Essa otimização visa melhorar a eficiência do algoritmo, reduzindo o tempo de execução e o consumo de memória.

**Pontuação:** 1.0 ponto

### 2. Detecção de Jogos sem Solução
A segunda tarefa consiste em implementar uma função que, dado um estado inicial do quebra-cabeça, determine se a configuração ordenada é alcançável a partir dele. Essa funcionalidade é essencial para identificar casos em que o jogo não possui solução.

**Pontuação:** 1.5 pontos

### 3. Comparação de Heurísticas
Nesta etapa, o aluno deve comparar quantitativamente diferentes heurísticas utilizadas no algoritmo **A⋆**. Para isso, é necessário definir uma métrica de avaliação, como:
- **Tempo para encontrar a solução**, ou
- **Número de estados enfileirados** durante a execução.

A escolha da métrica deve ser justificada, e os resultados obtidos devem ser analisados de forma crítica.

**Pontuação:** 2.5 pontos

### 4. Análise e Experimentos
A última tarefa envolve a realização de um experimento para responder a uma pergunta específica sobre o jogo ou o algoritmo. O aluno deve escolher um aspecto que despertou sua curiosidade durante o estudo, como:
- Por que alguns estados do jogo não possuem solução?
- Qual heurística é mais eficiente e por quê?
- É possível propor uma nova heurística que supere as existentes?

O experimento deve ser planejado e executado de forma rigorosa, com resultados claramente apresentados e discutidos.

**Pontuação:** 5.0 pontos

## Critérios de Avaliação

A nota final do trabalho será composta pela soma das pontuações obtidas em cada tarefa, conforme descrito na Tabela 1.

| **Tarefa**                        | **Pontuação** |
|-----------------------------------|---------------|
| 1. Remoção de estados repetitivos | 1.0 ponto     |
| 2. Detecção de jogos sem solução  | 1.5 pontos    |
| 3. Comparação de heurísticas      | 2.5 pontos    |
| 4. Análise e experimentos         | 5.0 pontos    |
| **Total**                         | **10.0 pontos** |

## Considerações Finais

Este trabalho oferece uma oportunidade para explorar conceitos fundamentais de inteligência artificial, como algoritmos de busca, heurísticas e análise de complexidade. A aplicação do algoritmo **A⋆** no contexto do quebra-cabeça de 8 peças permite não apenas compreender sua eficácia, mas também identificar limitações e oportunidades de melhoria.

A criatividade e o rigor metodológico serão essenciais para o sucesso na realização das tarefas propostas, especialmente na etapa de análise e experimentos, que exige a formulação de perguntas relevantes e a execução de testes