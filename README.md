# Projeto de Conexão de APIs com Python no Sistema Financeiro My Fin


Este documento visa detalhar o processo de desenvolvimento do projeto de Conexão de APIs utilizando Python no sistema modelo financeiro My Fin. O objetivo é apresentar as etapas envolvidas, desde a extração dos dados via API até os próximos passos de integração e análise com Power BI.

# 1. Introdução ao Projeto
Este projeto foi idealizado para simular um cenário real de uma empresa, utilizando o sistema My Fin. O desafio principal é desenvolver uma solução automatizada para extrair dados financeiros via API e integrá-los em um ambiente de análise. Até o momento, foram concluídas duas etapas fundamentais, com foco na extração e tratamento inicial dos dados.

# 2.Objetivo e Escopo
A missão principal deste projeto é criar um processo eficiente de extração de dados financeiros do My Fin através de APIs, utilizando Python como ferramenta principal. O objetivo é transformar esses dados em formatos que possam ser facilmente integrados e analisados no Power BI, garantindo a segurança e otimização dos dados ao longo do processo.

# 3. Extração e Tratamento de Dados
Na primeira etapa do projeto, foi realizada a extração dos dados utilizando a biblioteca requests para conectar-se à API do My Fin. Os dados extraídos foram transformados em um DataFrame com a ajuda da biblioteca pandas, permitindo um tratamento mais eficaz. Esses dados foram então salvos em dois formatos diferentes: xlsx, para fácil visualização, e parquet, que oferece uma melhor performance e otimização para consumo no Power BI.

# 4. Melhorias no Script Python
Na segunda etapa, foram implementadas melhorias no script Python para garantir maior segurança e eficiência. As credenciais de acesso (TOKEN) foram armazenadas de forma segura utilizando a biblioteca dotenv. Além disso, foi desenvolvida uma rotina de paginação via API para garantir que todos os dados fossem capturados, independentemente da quantidade de páginas disponíveis.

# 5. Próximas Etapas e Integração com Power BI

O próximo passo do projeto envolve a extração dos dados e o armazenamento em um banco de dados, como SQL Server ou Google Big Query. Após essa etapa, o objetivo é conectar diretamente o banco de dados ao Power BI, permitindo o desenvolvimento de um dashboard financeiro completo que apresente insights detalhados sobre a performance empresarial.
