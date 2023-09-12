# FUNinfo - Fungal informatics

## Modulo para calculo de centralidades
> o arquivo [`calculate_centrality.py`](03-module/calculate_centrality.py), contém as funções que podem ser usadas para calcular 5 tipos de centralidade ( Degree, Closeness, Betweenness, Eigenvector e Harmonic), deve ser enviado como paramêtro para as funções um arquivo `.csv` contendo todas as ligações desejadas entre os genes e obrigatoriamente devem existir nesse arquivo duas colunas `tg_locus_tag` e `tf_locus_tag`, o resultado será um dicionário contendo a tag do gene e a sua importância de acordo com o método de calculo escolhido. Você pode encontrar um exemplo da chamada das funções no arquivo [`example.py`](./example.py)

> EXEMPLO:
```json
{
    'FOXG_04464': 0.00257534779425911,
    'FOXG_11375': 0.00257534779425911,
    'FOXG_13256': 0.00257534779425911,
    'FOXG_17175': 0.00257534779425911,
    'FOXG_17402': 0.00257534779425911
}
```

## Testes e códigos relacionados ao estudo de grafos e representação de fungos
> Tasks da semana
- [X] Representar o fungo diferenciado o tamanho dos nós de acordo com o valor da centralidade
- [X] Criar um módulo que faça isso recebendo parâmetros de outra plataforma
