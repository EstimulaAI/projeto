"""Minimal Litestar application."""

from dataclasses import dataclass
from typing import Any, List

from litestar import Litestar, post

import numpy as np
import pandas as pd
import google.generativeai as genai
from pydantic import BaseModel

GOOGLE_API_KEY="AIzaSyCdHIigpXTIilKMIWQAY-3LBHhPgHd-uAc"
genai.configure(api_key=GOOGLE_API_KEY)

class Item(BaseModel):
    idade: int
    area: str
    itens: List[str]

@post("/")
async def index(data: Item) -> dict[str, Any]:
    idade = data.idade
    area = data.area
    itens = data.itens

    # Documentos sobre o Marco do Desenvolvimento
    DOCUMENT1 = {
        "Title": "Andar",
        "Content": "1 ano. Esperado: Anda com apoio, anda sem apoio. Sugerido: Brincadeiras que incentivem a crianca a se movimentar com seguranca, como caminhar entre moveis estaveis, usar brinquedos que podem ser empurrados."
    }

    DOCUMENT2 = {
        "Title": "Coordenação",
        "Content": "1 ano. Esperado: Segura objetos, transfere objetos de uma mao para outra, faz pinca. Sugerido: Jogos que envolvam encaixar blocos, atividades que estimulem o uso de colher ou garfo durante as refeicoes."
    }

    DOCUMENT3 = {
        "Title": "Relacionar",
        "Content": "1 ano. Esperado: Responde ativamente ao contato social, imita gestos, mostra o que quer. Sugerido: Brincadeiras de imitacao, jogos interativos com outras criancas ou adultos, como esconde-achou."
    }

    DOCUMENT4 = {
        "Title": "Emoções",
        "Content": "1 ano. Esperado: Sorri quando estimulada, brinca de esconde-achou. Sugerido: Jogos que envolvam expressoes faciais e de emocoes, leitura de livros com figuras expressivas."
    }

    DOCUMENT5 = {
        "Title": "Raciocínio",
        "Content": "1 ano. Esperado: Busca ativa de objetos, coloca blocos na caneca. Sugerido: Jogos de causa e efeito, como brinquedos que fazem sons ao serem manuseados, puzzles simples."
    }

    DOCUMENT6 = {
        "Title": "Curiosidade",
        "Content": "1 ano. Esperado: Explora objetos, leva objetos a boca, localiza o som. Sugerido: Atividades de descoberta usando texturas e sons diferentes, explorar ambientes seguros com supervisao."
    }

    DOCUMENT7 = {
        "Title": "Fala",
        "Content": "1 ano. Esperado: Emite sons, ri alto, duplica silabas, diz uma palavra. Sugerido: Conversacao constante com a crianca, leitura interativa, musicas infantis simples que a crianca possa tentar imitar."
    }

    DOCUMENT8 = {
        "Title": "Andar",
        "Content": "2 anos. Esperado: Anda com seguranca, pula com ambos os pes. Sugerido: Brincadeiras que incentivem pular e correr, como pega-pega ou brincadeiras com musica que envolvam movimentos corporais."
    }

    DOCUMENT9 = {
        "Title": "Coordenação",
        "Content": "2 anos. Esperado: Constroi torre de 6 cubos, arremessa bola, imita o desenho de uma linha. Sugerido: Atividades de construcao com blocos maiores, jogos que envolvam arremessar e pegar bolas leves, atividades de desenho com giz de cera ou lapis de cor."
    }

    DOCUMENT10 = {
        "Title": "Relacionar",
        "Content": "2 anos. Esperado: Brinca com outras criancas, veste-se com supervisao. Sugerido: Jogos de faz de conta em grupo, vestir bonecas ou bichos de pelucia, pequenas responsabilidades como escolher a roupa a usar com ajuda."
    }

    DOCUMENT11 = {
        "Title": "Emoções",
        "Content": "2 anos. Esperado: Expressa emocoes mais complexas, reconhece emocoes em outros. Sugerido: Jogos que envolvam identificar expressoes faciais em livros ou jogos, conversas sobre como personagens de historias podem estar se sentindo."
    }

    DOCUMENT12 = {
        "Title": "Raciocínio",
        "Content": "2 anos. Esperado: Reconhece 2 acoes, segue instrucoes simples. Sugerido: Jogos de memoria, quebra-cabecas simples, atividades que pecam para a crianca realizar acoes em sequencia, como pegar o brinquedo e coloca-lo na caixa."
    }

    DOCUMENT13 = {
        "Title": "Curiosidade",
        "Content": "2 anos. Esperado: Exploracao ativa do ambiente, faz perguntas simples. Sugerido: Explorar o ambiente ao redor com atividades de natureza, caca ao tesouro em casa com itens simples."
    }

    DOCUMENT14 = {
        "Title": "Fala",
        "Content": "2 anos. Esperado: Frases com 2 palavras, comunica necessidades. Sugerido: Conversacao constante, leitura interativa que envolva a crianca na narrativa, cantar musicas simples juntos."
    }

    DOCUMENT15 = {
        "Title": "Andar",
        "Content": "3 anos. Esperado: Equilibra-se em cada pe por 1 segundo, corre com maior coordenacao. Sugerido: Jogos de estatua enquanto corre, brincadeiras de equilibrio como caminhar sobre uma linha tracada no chao."
    }

    DOCUMENT16 = {
        "Title": "Coordenação",
        "Content": "3 anos. Esperado: Veste uma camiseta, move o polegar com a mao fechada, copia circulos. Sugerido: Atividades de vestir bonecas ou pelucias com roupas simples, brincadeiras que envolvam desenhar formas e usar tesouras de pontas arredondadas para cortar formas simples."
    }

    DOCUMENT17 = {
        "Title": "Relacionar",
        "Content": "3 anos. Esperado: Brinca cooperativamente com outras criancas, mostra maior independencia. Sugerido: Jogos de montar em grupo, atividades que incentivem a crianca a tomar pequenas decisoes e resolver conflitos simples com supervisao."
    }

    DOCUMENT18 = {
        "Title": "Emoções",
        "Content": "3 anos. Esperado: Expressa uma gama mais ampla de emocoes, identifica emocoes em outros. Sugerido: Atividades dramaticas como teatrinho de fantoches, discussoes sobre como personagens em historias se sentem."
    }

    DOCUMENT19 = {
        "Title": "Raciocínio",
        "Content": "3 anos. Esperado: Emparelha cores, compreende 2 adjetivos. Sugerido: Jogos de memoria com cores e formas, atividades que envolvam classificar objetos por tamanho, cor ou textura."
    }

    DOCUMENT20 = {
        "Title": "Curiosidade",
        "Content": "3 anos. Esperado: Faz perguntas mais complexas, explora o ambiente com detalhes. Sugerido: Atividades de ciencias simples como misturar cores, experimentos com agua e areia, explorar natureza no parque."
    }

    DOCUMENT21 = {
        "Title": "Fala",
        "Content": "3 anos. Esperado: Fala clara e compreensivel, usa frases mais complexas. Sugerido: Conversacao ativa em casa, contar historias, participar de cancoes e rimas infantis."
    }


    documents = [
        DOCUMENT1, DOCUMENT2, DOCUMENT3, DOCUMENT4, DOCUMENT5, DOCUMENT6, DOCUMENT7,
        DOCUMENT8, DOCUMENT9, DOCUMENT10, DOCUMENT11, DOCUMENT12, DOCUMENT13, DOCUMENT14,
        DOCUMENT15, DOCUMENT16, DOCUMENT17, DOCUMENT18, DOCUMENT19, DOCUMENT20, DOCUMENT21
    ]

    df = pd.DataFrame(documents)
    df.columns = ["Title", "Content"]

    model_emb = "models/embedding-001"

    def embed_fn(title, text):
        return genai.embed_content(model=model_emb,
                                 content=text,
                                 title=title,
                                 task_type="RETRIEVAL_DOCUMENT")["embedding"]
    
    df["Embeddings"] = df.apply(lambda row: embed_fn(row["Title"], row["Content"]), axis=1)
    
    def gerar_e_buscar_consulta(consulta, base, model):
        embedding_da_consulta = genai.embed_content(model=model_emb,
                                 content=consulta,
                                 task_type="RETRIEVAL_QUERY")["embedding"]

        produtos_escalares = np.dot(np.stack(df["Embeddings"]), embedding_da_consulta)

        indice = np.argmax(produtos_escalares)
        return df.iloc[indice]["Content"]
    
    consulta = f"{area}. Esperado para {idade} anos."

    trecho = gerar_e_buscar_consulta(consulta, df, model_emb)

    # Modelo

    # Configurações do Modelo

    generation_config = {
    "candidate_count": 1,  # Somente uma opção
    "temperature": 0.6,    # Deixar um pouco mais criativo, pois não imaginamos oq o usuário tem!
    }

    # Deixando o modelo bem restrito para evitar brincadeiras perigosas
    safety_settings = {
        'HATE': 'BLOCK_LOW_AND_ABOVE',
        'HARASSMENT': 'BLOCK_LOW_AND_ABOVE',
        'SEXUAL' : 'BLOCK_LOW_AND_ABOVE',
        'DANGEROUS' : 'BLOCK_LOW_AND_ABOVE'
    }
    
    model = genai.GenerativeModel(model_name='gemini-1.0-pro',
                                  generation_config=generation_config,
                                  safety_settings=safety_settings,)

    response = model.generate_content(f''' Crie uma brincadeira lúdica que ajude a estimular 
                                       somente a {area} de uma criança que tem {idade} anos.
                                       A brincadeira deve conter apenas os itens {itens}.
                                       A resposta deve ter o nome da brincadeira, instruções e os objetivos da estimulação
                                       O {trecho} deve guiar a criação da brincadeira''')
    response.text

    return {"response": response.text}

app = Litestar(route_handlers=[index])