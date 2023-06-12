#discord bot for sending messages from code to discord server
from discord import SyncWebhook
import os 
import datetime
import subprocess 
class Logger(object):

    def __init__(self,webhook=None,log_file=None,run_name=None):
        self.webhook = webhook 
        self.terminal_mode = False 
        self.run_name = run_name 
        self.log_file = log_file
        self.maxlen = 20

    def set_run_name(self,run_name):
        self.run_name = run_name
    
    def set_log_file(self,log_file):
        self.log_file = log_file 
    
    def set_webhook(self, url = None):
        if url is None:
            #read from env variable and set webhook
            url = os.getenv('DISCORD_WEBHOOK_URL')

        self.webhook = SyncWebhook.from_url(url)   
    
    def set_terminal_mode(self,mode=True,maxlen=20):
        self.terminal_mode = mode 
        self.maxlen =maxlen 
    
    def ping(self,message):
        assert not self.terminal_mode, "Terminal mode is on, cannot ping"
        assert self.webhook is not None, "Webhook is not set"
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message  = f"**{self.run_name.upper()}**: {now}\n\n{message}"
        self.webhook.send(message)
    

    def read_log(self,maxlen=20):
        if self.log_file is not None:
            with open(self.log_file,'r') as f:
                lines = f.readlines()
                l = min(maxlen,len(lines))
                return lines[-l:]
        
        else:
            #read from terminal
            raise NotImplementedError("Reading from terminal is not implemented yet")

    def run_terminal_mode(self):
        self.ping('\n'.join(self.read_log()))




####TESTING#######
# logger = Logger()
# logger.set_webhook(
#     'your log')
# logger.set_run_name('test')
# logger.ping('testing')
# logger.set_log_file('/users/himanshugauravsingh/Desktop/score_responses.py')
# logger.run_terminal_mode()