from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, BookDB, User

engine = create_engine('sqlite:///BookCatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# creating a  dummy user
User1 = User(name="admin", email="loganscream@gmail.com")
session.add(User1)
session.commit()

# Dummy books data
book1 = BookDB(bookName="The way of the zen",
               authorName="Alan Watts",
               coverUrl="""https://books.google.com/books/content/
               images/frontcover/F9uIBAAAQBAJ?fife=w300-rw""",
               description="bye", category="Romance", user_id=1)

session.add(book1)
session.commit()

book2 = BookDB(bookName="Harry Potter",
               authorName="J.K Rowlings",
               coverUrl="""https://books.google.com/books/content/images/
               frontcover/sQAfCgAAQBAJ?fife=w300-rw""",
               description="one", category="Fantasy", user_id=1)

session.add(book2)
session.commit()

book3 = BookDB(bookName="Las mil y una noches",
               authorName="Anonimo",
               coverUrl="""https://books.google.com/books/content/
               images/frontcover/xE15t_pAG34C?fife=w300-rw""",
               description="three", category="Fiction", user_id=1)

session.add(book3)
session.commit()

book4 = BookDB(bookName="Gog",
               authorName="Giovanni Papini",
               coverUrl="""https://books.google.com/books/content/
               images/frontcover/fEI4qWTBoZMC?fife=w300-rw""",
               description="two", category="Mystery", user_id=1)

session.add(book4)
session.commit()

book5 = BookDB(bookName="El principe",
               authorName="Maquiavelo",
               coverUrl="""https://books.google.com/books/content/images
               frontcover/CDQnAgAAQBAJ?fife=w300-rw""",
               description="four", category="Romance", user_id=1)

session.add(book5)
session.commit()


print "added Books!"