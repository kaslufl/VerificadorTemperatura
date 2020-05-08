from flask import Flask

app = Flask(__name__)

from application.controller import controller_umidade
from application.controller import controller_temperatura