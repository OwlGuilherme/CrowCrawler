import os
import subprocess

def run_spy_ml():
    command = "scrapy crawl mercado_livre"
    subprocess.run(command, shell = True)

run_spy_ml()