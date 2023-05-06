from flask import Flask, jsonify, abort, request
from datetime import datetime, timedelta
from sqlalchemy import create_engine, Column, Integer, String, Date, Float, Boolean, DateTime
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import NoResultFound, MultipleResultsFound

app = Flask(__name__)
Base = declarative_base()
engine = create_engine('sqlite:///hw.db')
Session = sessionmaker(bind=engine)
session = Session()


class Books(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    count = Column(Integer, default=1)
    release_date = Column(DateTime, nullable=False)
    author_id = Column(Integer, nullable=False)

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Students(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    phone = Column(String(11))
    email = Column(String(50))
    average_score = Column(Float, nullable=False)
    scholarship = Column(Boolean, default=False)

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @classmethod
    def get_scholarship_students(cls):
        return session.query(Students).filter(Students.scholarship == True).all()

    @classmethod
    def get_students_with_higher_score(cls, score):
        return session.query(Students).filter(Students.average_score > score).all()


class ReceivingBook(Base):
    __tablename__ = 'receiving_books'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, nullable=False)
    student_id = Column(Integer, nullable=False)
    date_of_issue = Column(DateTime, nullable=False)
    date_of_return = Column(DateTime)

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @hybrid_property
    def count_date_with_book(self):
        if self.date_of_return:
            return (self.date_of_return - self.date_of_issue).days
        else:
            return (datetime.now() - self.date_of_issue).days


@app.before_request
def before_request_func():
    Base.metadata.create_all(engine)


@app.route('/books', methods=['GET'])
def get_books():
    books = session.query(Books).all()
    books_list = []
    for book in books:
        books_list.append(book.to_json())
    return jsonify(books_list=books_list), 200


@app.route('/debtors', methods=['GET'])
def get_debtors():
    debtors = session.query(ReceivingBook).filter(ReceivingBook.date_of_return == None).all()
    debtors_list = []
    for debtor in debtors:
        if debtor.count_date_with_book > 14:
            debtors_list.append(debtor.to_json())
    return jsonify(debtors_list=debtors_list), 200


@app.route('/issue_book', methods=['POST'])
def issue_book():
    book_id = request.form.get('book_id', type=int)
    student_id = request.form.get('student_id', type=int)
    new_issue = ReceivingBook(book_id=book_id,
                                student_id=student_id,
                                date_of_issue=datetime.now())
    session.add(new_issue)
    session.commit()
    return f"Книга с id {book_id} выдана", 201


@app.route('/pass_book', methods=['POST'])
def pass_book():
    try:
        book_id = request.form.get('book_id', type=int)
        student_id = request.form.get('student_id', type=int)
        book = session.query(ReceivingBook).filter(ReceivingBook.book_id == book_id, ReceivingBook.student_id == student_id).one()
        book.date_of_return = datetime.now()
        session.commit()
        return f"Книга с id {book_id} сдана"
    except NoResultFound:
        return 'Такой связки book_id и student_id не существует'
    except MultipleResultsFound:
        return 'С такой связкой book_id и student_id надено несколько записей'


if __name__ == "__main__":
    app.run()


