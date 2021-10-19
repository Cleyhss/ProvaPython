from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

receita = [
{
    'title': "Hamburguer",
    'lista de ingredientes':[
        "Pão",
        "carne de hamburguer",
        "tomate",
        "alface",
        "ovo",
        "creme de milho"
    ],
    'modo de preparo': "Asse a carne de hamburguer, depois coloque no pão junto com o ovo assado, as tomates cortadas em rodelas ...",
    'rendimento': "1 "
}
]

class Recs(Resource):
    def get(self):
        return {'status': 200, 'data': receita}

    def post(self):
        newRec = json.loads(request.data)
        receita.append(newRec)
        return {
            "message": "Updated!",
            "new": newRec
        }

class Rec(Resource):
    def get(self, indice):
        try:
            return receita[indice]
        except IndexError:
            messagem = "Indice {} não encontrado!".format(indice)
            return {
                "status": "Erro de índice!"
                "mensage": messagem,
            }
        except:
            messagem = "Erro desconhecido"
            return {
                "status": "Erro de índice",
                "mensage": messagem,
            }


    def put(self, indice):
        newValue = json.loads(request.data)
        receita[indice] = newValue
        return {
            "message": "Updated!",
            "new": newValue
        }

    def delete(self, indice):
        receita.pop(indice)
        return {
            "message": "Deleted!",
            "Lista de Receitas": receita
        }


api.add_resource(Recs,'/recs/')
api.add_resource(Rec,'/recs/<int:indice>')

if __name__ == '__main__':
    app.run(debug=True)
