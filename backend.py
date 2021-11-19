import sqlite3

def connect(): 
    conn = sqlite3.connect(".\\aluno.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS ALUNO(
                        id_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome VARCHAR(50) NOT NULL, 
                        matricula INTEGER UNIQUE NOT NULL,
                        email VARCHAR(50) UNIQUE NOT NULL,
                        endereco VARCHAR(50) NOT NULL,
                        campus VARCHAR(20) NOT NULL, 
                        periodo CHAR(1) NOT NULL,  
                        av1 NUMERIC NOT NULL,  
                        av2 NUMERIC NOT NULL,  
                        av3 NUMERIC NOT NULL,  
                        avd NUMERIC NOT NULL,  
                        avds NUMERIC NOT NULL)
                    ''')
    conn.commit()
    conn.close()
    
def insert(nome, matricula, email, endereco, campus, periodo, av1, av2, av3, avd, avds):
    conn = sqlite3.connect(".\\aluno.db")
    cursor = conn.cursor()
    cursor.execute('INSERT INTO ALUNO(nome, matricula, email, endereco, campus, periodo, av1, av2, av3, avd, avds) VALUES(?,?,?,?,?,?,?,?,?,?,?)', (nome, matricula, email, endereco, campus, periodo, av1, av2, av3, avd, avds))
    conn.commit()
    conn.close()
    
def view(matricula):
    conn = sqlite3.connect(".\\aluno.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ALUNO WHERE matricula = ?', (matricula,))
    linhas = cursor.fetchall()
    conn.close()
    return linhas

def delete(matricula):
    conn = sqlite3.connect('C:\\Users\\carlos.ozorio\\Desktop\\Agenda\\livros.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM aluno WHERE matricula = ?' ,(matricula,))
    conn.commit()
    conn.close()

connect()