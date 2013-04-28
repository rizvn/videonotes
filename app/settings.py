settings = {
    #sqlite config
    'db_path': 'db/videonotes.db',

    #Mysql config
    'host': 'localhost',
    'port': 3306,
    'user': 'riz',
    'passwd': 'pass',
    'db': 'videonotes'
}


#jinja2 templates
from app.utils import sec_to_time
from jinja2 import Environment, FileSystemLoader
jinja_env = Environment(loader=FileSystemLoader('views'))
jinja_env.filters['sec_to_time'] = sec_to_time


