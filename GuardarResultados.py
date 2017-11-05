import csv

class DAO():
    def __init__(self):
        contexto = 'c:\\Users\\James\\Google Drive\\01 - FAESA\\2017.2\\06 - INTERDICIPLINAR\\BASE_DADOS\\'
        self.ENTRAGAS_FILE = contexto + 'resultados_entregas.csv'
        self.ROTAS_FILE = contexto + 'resultados_rotas.csv'
    
    def abrirEntregas(self):
        self.csvfile, self.escritor = self.abrirArquivo(self.ENTRAGAS_FILE)
        self.guardar(['dia','carro','cliente','produto'])

    def abrirRotas(self):
        self.csvfile, self.escritor = self.abrirArquivo(self.ROTAS_FILE)
        self.guardar(['dia','carro','cliente','custo'])

    def guardar(self, args):
            self.escritor.writerow(args)

    def fecharArquivo(self):
        self.csvfile.close()
    
    def abrirArquivo(self, arquivo):
        csvfile = open(arquivo, 'w', newline='')
        escritor = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        return csvfile, escritor

