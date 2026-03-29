from sqlalchemy import create_engine,text


engine = create_engine(
    "sqlite:///C:\\Users\\josek\\Documents\\Curso_Python\\sqlAlchemy\\teste.db"
    )

print(engine)

with engine.connect() as conn:
    result = conn.execute(
        text(
            "INSERT INTO usuarios (nome, email) VALUES ('Ana Silva, 'ana@email.com)"
            )
            )
    conn.commit()
    print(result.all())