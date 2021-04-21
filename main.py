from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    lastname = Column(String(50))
    email = Column(String(50))
    registro = relationship("Registro", uselist=False, back_populates="student")


class Registro(Base):
    __tablename__ = 'registro'

    registroID = Column(Integer, primary_key=True)
    user_ID = Column(Integer, ForeignKey('student.id'))
    result = Column(Integer)
    student = relationship("Student", back_populates="registro")


engine = create_engine("mysql+mysqldb://root:1984@localhost/levelup")
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

student1 = Student(name='Samuel', lastname='Martinez', email='1594@holbertonschool.com')
session.add(student1)
session.commit()

registro_Samuel = Registro(user_ID=student1.id, result=100)

session.add(registro_Samuel)
session.commit()

query = session.query(Student).first()
print(query.registro.student.registro.student.email)
