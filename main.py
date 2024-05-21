from pathlib import Path
import random

from models import Base, User
from router import engines, RoutingSession


def main():
    session = RoutingSession()
    print("  ==== WRITING ====  ")

    session.add_all([
        User(name='paul', email='paul@example.com'),
        User(name='george', email='george@example.com'),
        User(name='john', email='john@example.com'),
        User(name='ringo', email='ringo@example.com'),
    ])

    print("==== END WRITING ====")

    session.commit()

    print("  ==== READING ====  ")

    for _ in range(10):
        user = random.choice(session.query(User.email).all())
        print("🟢 User email is", user.email)

    print("==== END READING ====")

    session.close()


def setup():
    # remove existing SQLite files from previous runs, if any
    for file in Path('.').glob('*.db'):
        file.unlink()
    # create fresh SQLlite files
    for engine in engines.values():
        Base.metadata.create_all(engine)


if __name__ == '__main__':
    setup()
    main()
