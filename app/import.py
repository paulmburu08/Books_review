import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql+psycopg2://paul:pauldatabase@localhost/bookreview1')
db = scoped_session(sessionmaker(bind=engine))


def main():
    # db.execute("CREATE TABLE Books (name VARCHAR NOT NULL, \
    #                                 year INTEGER NOT NULL, \
    #                                 author VARCHAR NOT NULL, \
    #                                 book_num VARCHAR PRIMARY KEY)")

    with open('books.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for isbn, title, author, year in csv_reader:
		
			


            try:
                db.execute("INSERT INTO Books (name, year, author, book_num) VALUES (:title, :year, :author, :book_num)",
                           {"title": title, "year": year, "author": author, "book_num": isbn})
                print(f"{title} Added to the Books Database.")
            except Exception as e:
                print(f"{title} DIDNT ADD TO THE DATABASE------- {e}")
                db.rollback()
        db.commit()


if __name__ == "__main__":
    main()
