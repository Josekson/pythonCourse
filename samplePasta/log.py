from pathlib import Path

LOG_FILE = Path(__file__).parent/'log.txt'
print(LOG_FILE)
class Log:
    def log(self,msg):
        #print(self.__class__.__name__)
        raise NotImplemented('Implemente o método log')
    
    def log_error(self,msg):
        return self.log(f'Error: {msg}')   

    def log_success(self,msg):
        return self.log(f'Success: {msg}')

class LogFileMixin(Log):
    def log(self,msg):
        msg_formatada = f'{msg} -> {self.__class__.__name__}'
        with open(LOG_FILE,'a') as file:
            file.write(msg_formatada)
            file.write('\n')
            
class LogPrintMixin(Log):
    def log(self,msg):
      print(f'{msg} -> {self.__class__.__name__}')

if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_success('VOCÊ ESTÁ CERTO!')
    lp.log_error('errado, mas não desista. Você consegue!')
     
    lf = LogFileMixin()
    lf.log_success('VOCÊ ESTÁ CERTO!')
    lf.log_error('errado, mas não desista. Você consegue!')