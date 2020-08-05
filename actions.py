import requests
from requests.auth import HTTPBasicAuth
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

base_url = config['SERVICORESERVA']['URL_BASE']

def action_handler(action, parameters, return_var):
    return_values = {}
    if action == 'consultaDisponibilidade':
        return_values = consultaDisponibilidade(parameters, return_var)

    if action == 'efetuaReserva':
        return_values = efetuaReserva(parameters, return_var)

    return {
            'skills': {
                'main skill': {
                    'user_defined': return_values
                }
            }
        }

def consultaDisponibilidade(pars,return_var):
    datain = pars['dataentrada']
    dataout = pars['datasaida']
    servico = '?servico=consulta'
    pars_get = '&datain='+datain+'&dataout='+dataout
    url_final = base_url+servico+pars_get

    response = requests.get(url_final,auth=HTTPBasicAuth('m317510','123456'))
    if (response.status_code == 200):
        print(response.text)
        return ({return_var: response.text})
    else:
        print("Erro de requisicao!\n")
        return ({return_var: 'Nao consegui consultar as datas!\n'})

def efetuaReserva(pars,return_var):
    datain = pars['datacheckin']
    dataout = pars['datacheckout']
    confirmacao = pars['confirma']
    servico = '?servico=reserva'
    pars_get = '&datain='+datain+'&dataout='+dataout+'&confirmacao='+confirmacao
    url_final = base_url+servico+pars_get

    response = requests.get(url_final,auth=HTTPBasicAuth('m317510','123456'))
    if (response.status_code == 200):
        print(response.text)
        return ({return_var: response.text})
    else:
        print("Erro de requisicao!\n")
        return ({return_var: 'Nao consegui reservar as datas!\n'})
