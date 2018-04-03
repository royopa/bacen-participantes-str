#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import requests
import csv
from tqdm import tqdm
import pandas
import time


def download_participantes_str(url, file_name):
    response = requests.get(url, stream=True)

    with open(file_name, "wb") as handle:
        for data in tqdm(response.iter_content()):
            handle.write(data)


def main():
    url = "http://www.bcb.gov.br/pom/spb/estatistica/port/ParticipantesSTRport.csv"
    file_name = "participantes_str.csv"
    download_participantes_str(url,file_name)
    data = []
    df = pandas.read_csv(file_name)

    for i in df.index:
        ispb = df[df.columns[0]][i]
        nome = df[df.columns[1]][i].strip()
        codigo = df[df.columns[2]][i]
        ic_participa_compe = df[df.columns[3]][i]
        co_acesso = df[df.columns[4]][i]
        no_extenso = df[df.columns[5]][i]
        dt_ini_operacao = df[df.columns[6]][i]
        dt_ini_operacao = time.strptime(dt_ini_operacao, "%d/%m/%Y")

        data.append({
            'ispb': ispb,
            'nome': nome,
            'codigo': codigo,
            'ic_participa_compe': ic_participa_compe,
            'co_acesso': co_acesso,
            'no_extenso': no_extenso.strip(),
            'dt_ini_operacao': dt_ini_operacao
        })

    df = pandas.DataFrame(data)
    df.to_csv('bancos.csv', index=False, encoding='utf-8')

#ISPB,Nome_Reduzido,Número_Código,Participa_na_Compe,Acesso_Principal,Nome_Extenso,Início_da_Operação


if __name__ == "__main__":
    main()