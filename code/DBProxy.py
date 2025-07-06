# ==== DBProxy.py ====
#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3

class DBProxy:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        # Cria tabela 'dados' com colunas corretas e vírgulas
        self.connection.execute('''
        CREATE TABLE IF NOT EXISTS dados (
            id    INTEGER PRIMARY KEY AUTOINCREMENT,
            name  TEXT    NOT NULL,
            score INTEGER NOT NULL,
            date  TEXT    NOT NULL
        );
        ''')
        self.connection.commit()

    def save(self, score_dict: dict):
        # score_dict deve ter chaves: 'name', 'score', 'date'
        self.connection.execute(
            'INSERT INTO dados (name, score, date) VALUES (:name, :score, :date)',
            score_dict
        )
        self.connection.commit()

    def retrieve_top10(self) -> list:
        # Retorna as 10 maiores pontuações
        cursor = self.connection.execute(
            'SELECT * FROM dados ORDER BY score DESC LIMIT 10'
        )
        return cursor.fetchall()

    def close(self):
        self.connection.close()

