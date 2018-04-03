# bacen-participantes-str
Aplicação com a lista de participantes do STR (Sistema de Transferência de Reservas) disponibilizadas pelo Banco Central do Brasil

# usando

```sh
> python download_participantes_str.py
```

O script faz o download da lista atualizada do site do BACEN e formata num arquivo de saída (bancos.csv)[bancos.csv] que pode ser utilizado como base de dados de informações.

O arquivo [bancos.csv](bancos.csv) possui as seguintes colunas: co_acesso,codigo,dt_ini_operacao,ic_participa_compe,ispb,no_extenso,nome

