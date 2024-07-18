from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain_openai import ChatOpenAI
import os
os.environ["OPENAI_API_KEY"] ="API KEY de OPENAI"
 
 
db_uri = 'mysql+pymysql://usuario:contraseña@host:puerto/namedatabase'
db = SQLDatabase.from_uri(db_uri)
print(db.get_usable_table_names())
 
from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI(temperature=0, model="gpt-3.5")  #Aca escojes el modelo
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

formato = """
Data una pregunta del usuario:
1. crea una consulta de sqlite3
2. revisa los resultados
3. devuelve el dato
4. si tienes que hacer alguna aclaración o devolver cualquier texto que sea siempre en español
#{question}
"""

# 6. Función para hacer la consulta
 
def consulta(input_usuario):
    consulta = formato.format(question = input_usuario)

    resultado = db_chain.invoke(consulta)
    with open("Query.txt", "w") as file_object:
        file_object.write(f"\nResultados de la consulta: {resultado}\n")
        
    resultado = db_chain.run(consulta)
    resultado = str(resultado)

    return(resultado)



#db_chain.invoke("cuantos registros tiene la tabla de groline")
