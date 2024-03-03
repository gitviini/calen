import os, time, sqlite3

def msg(color=31,type='',content=''):
    print(f'\033[{color};3m{type} :. {content}\033[m')

class Model():
    def __init__(self):
        #CONSTANTS
        self.BASE_PATH = os.getcwd()
        self.FOUDER = 'src'
        self.PATH = os.path.join(self.BASE_PATH,self.FILE_NAME)

        #VARIABLES
        self.template = []

        self.table_exists()

    def connect():
        pass

    def table_exists(self):
        pass

    def template_define(self,topics=[]):
        self.template = topics
        msg(32,'template define','new template defined')

    def time_define(self,mode=0,date=''):
        match (mode):
            case 0:
                pass
            case 1:
                pass
            case _:
                msg(31,'time define',f'not found mode:{mode}')

    def insert(self,topic='', content=False):
        pass

#model = Model()