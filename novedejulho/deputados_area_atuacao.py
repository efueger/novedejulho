import requests as req

from ndj_toolbox.fetch import (xml_df, save_files)

url_base = 'https://www.al.sp.gov.br/repositorioDados/deputados/'
url_file = 'deputado_area_atuacao.xml'
url = url_base + url_file


def process_deputados_area_atuacao():
    xml_data = req.get(url).content
    dataset = xml_df(xml_data).process_data()
    dataset = dataset[['IdDeputado', 'IdArea', 'NrOrdem']]
    dataset = dataset.rename(columns={
        'IdDeputado': 'id_deputado', 'IdArea': 'id_area', 'NrOrdem': 'nr_ordem'
    })
    save_files(dataset, 'data', 'deputados_area_atuacao')


def main():
    process_deputados_area_atuacao()


if __name__ == '__main__':
    main()
