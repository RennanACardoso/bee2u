import cherrypy
import os
from pymongo import MongoClient
import pymongo
import conect
import pandas as pd


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["beer2u_leitos"]
leitos = mydb["leitos"]


class Home(object):
    @cherrypy.expose()
    def index(self):
        return open('index.html')


estado = []
municipio = []
estadoSigla = []
nomeCnes = []
a = 'não informado'

for i in leitos.find():
    estado.append(i['estado'])
    municipio.append(i['municipio'])   
    estadoSigla.append(i['estadoSigla'])
    try:
        nomeCnes.append(i['nomeCnes'])
    except:
        nomeCnes.append(a)
        

df = pd.DataFrame()
df['Estado'] = pd.Series(estado).values
df['Municipio'] = pd.Series(municipio).values
df['EstadoSigla'] = pd.Series(estadoSigla).values
df['Hospital'] = pd.Series(nomeCnes).values

html = df.to_html() 
  
text_file = open("dataframe.html", "w") 
text_file.write(html) 
text_file.close()




class Consulta(object):
    @cherrypy.expose()
    def index(self):
        return open('consulta.html')

    @cherrypy.expose()
    def result(self, estado, cidade, data):  
        for i in leitos.find():
            estado = i['estado']

        result = estado +'-' + cidade
        return ' = {}'.format(result)

class Config(object):
    @cherrypy.expose()
    def index(self):
        return open('config.html')
        
    


















if __name__ =='__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './static'
        
        },
        '/public': {
            'tools.publicdir.on': True,
            'tools.publicdir.dir': './public'
        }
    }
    cherrypy.tree.mount(Home(), '/', conf)
    cherrypy.tree.mount(Consulta(),'/consulta', conf)
    cherrypy.tree.mount(Config(),'/config',conf)
    cherrypy.engine.start()
    cherrypy.engine.block()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    