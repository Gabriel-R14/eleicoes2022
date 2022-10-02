import requests
import json

data = requests.get('https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json')

jsonData = json.loads(data.content)

cands = []
votosValidos = []
porcentagem = []

for info in jsonData['cand']:
    cands.append(info['nm'])
    votosValidos.append(info['vap'])
    porcentagem.append(info['pvap'])

print(f'{"Candidatos":<20}{"Votos Válidos":>20}{"Porcentagem":>21}')
print('-'*61)
for c in range(0, 11):
    print(f'{cands[c]:<20}{votosValidos[c]:>20}{porcentagem[c]:>20}%')
    print('-'*61) 