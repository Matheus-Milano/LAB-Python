# -*- coding: utf-8 -*-

import configparser
import ssl
import pymysql

def conectar():
    cfg = configparser.ConfigParser(interpolation=None)
    cfg.read("config.ini", encoding="utf-8")
    banco = cfg["banco"]
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    return pymysql.connect(
        host=banco["host"],
        port=banco.getint("porta"),
        user=banco["usuario"],
        password=banco["senha"],
        database=banco["nome"],
        ssl=ssl_context
    )