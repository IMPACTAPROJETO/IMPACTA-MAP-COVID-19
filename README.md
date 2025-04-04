Dashboard de Monitoramento da COVID-19 no Brasil
-
📌 Funcionalidades

Mapa interativo: Exibe um mapa de calor dos estados brasileiros com base nos casos de COVID-19.

Gráficos interativos: Permite visualizar a evolução dos casos acumulados, novos casos, óbitos e outras métricas por estado.

Seleção de Data: O usuário pode selecionar uma data específica para visualizar os dados correspondentes.

Filtragem por Estado: Alternar entre os dados do Brasil inteiro ou de estados específicos.
-
Indicadores Chave: Exibição de estatísticas como casos recuperados, casos em acompanhamento, total de casos confirmados e número de óbitos.
-
📁 Projeto_Dash_COVID19
│── app.py  # Script principal da aplicação
│── HIST_PAINEL_COVIDBR_13mai2021.csv  # Base de dados com os registros da COVID-19
│── geojson/
│   ├── brazil_geo.json  # Arquivo com as coordenadas dos estados brasileiros
│── assets/
│   ├── logo_dark.png # Logo exibido no painel
    ├──  Style.css # Estrutura css
│── df_states.csv  # Dados processados por estado
│── df_brasil.csv  # Dados processados do Brasil


## ⚠️ PROJETO FACULDADE ⚠️
---
Análise de Dados🔍📊   IMPACTA 
                      MAPCOVID🌎

---

### Sobre o Projeto💡
Este projeto apresenta a construção de um dashboard interativo desenvolvido em CSS, Python, utilizando as bibliotecas Plotly e Dash com o objetivo de fornecer, uma ferramenta acessível e dinâmica para a visualização e análise de dados da epidemia Covid-19😷
---
Com esse painel, os usuários podem:🖥️

✅ Visualizar a evolução dos casos ao longo do tempo.
✅ Comparar o impacto da Covid-19 em diferentes regiões.
✅ Identificar tendências e padrões epidemiológicos.
✅ Selecionar datas específicas para um estudo mais detalhado.

---

# 🚨IMPACTA MAP COVID-19🦠💉😷🚨
Painel Dashboard Análise De Dados da COVID-19
![Dashboard IMPACTA-MAPCOVID](https://snipboard.io/FnbUQz.jpg)  
---
Painel Dashboard (Carregando)
![Análise de dados Carregando](https://snipboard.io/m5HpJn.jpg)
----
Painel Dashboard (Visão Geral)
![Análise de Dados evolução COVID-19](https://snipboard.io/MbJNPC.jpg)
----
Painel Dashboard Estado De São Paulo Selecionado
![Visualização do Estado de São Paulo](https://snipboard.io/xaIVUE.jpg)



---
PAINEL Interativo com Data e Cards informando os Dados do Dataframe.📈
![PAINEL INTERATIVO COM DATA E CARDS](https://snipboard.io/Vtnu6N.jpg)
---
PAINEL PARA SELECIONAR A DATA DOS CASOS OCORRIDOS DA COVID-19📉
![Selecionar Data](https://snipboard.io/Q24PpJ.jpg)
---
Gráfico de Linha para Visualização de Casos Acumulados e Óbitos Totais! 📊
![Gráfico de Linha](https://snipboard.io/2FUXiG.jpg)
---
Gráfico de Barras para Visualização de Novos Casos e Óbitos por Dia!📑
![Gráfico de Barras](https://snipboard.io/wi3NOt.jpg)
---
Gráfico de Mapa para Visualização do Brasil e Estados afetados pela COVID-19!🗺️
![Mapa para visualização geral e de estados afetados](https://snipboard.io/QpDMsa.jpg)
---



### Tecnologias e Imports Utilizados
- ✅ **Python** 
- ✅ **Pandas**
- ✅ **Numpy**
- ✅ **Plotly**
- ✅ **Dash Bootstrap Components**
- ✅ **plotly.express**
- ✅ **plotly.graph_objects** 
- ✅ **CSS**
- ✅ **json** 
---

### Como Executar
🚀 Como Executar o Projeto

Clone o repositório:

git clone https://github.com/IMPACTAPROJETO/IMPACTA-MAP-COVID-19
cd projeto-dash-covid

Instale as dependências necessárias:

pip install -r requirements.txt

Execute o script:

python app.py

Acesse a aplicação no navegador: http://127.0.0.1:8050/
OBSERVAÇÃO! FAZER O DOWNLOAD DA PLANILHA COMPLETA DIRETO DO SITE DA CORONAVÍRUS: https://covid.saude.gov.br/ PARA QUE FUNCIONE CORRETAMENTE A APLICAÇÃO.
🔥 Exemplo de Uso

O painel exibe um mapa interativo onde a cor dos estados representa a quantidade de casos novos registrados em um determinado dia. Além disso, indicadores e gráficos mostram estatísticas detalhadas da COVID-19 no Brasil.
