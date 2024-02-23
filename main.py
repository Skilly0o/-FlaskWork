from flask import Flask

from data import db_session
from data.jobs import Jobs
from data.yawork import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


# вызывать для заполнения базы данных с составом команды
def add_captain_and_colonists():
    session = db_session.create_session()

    captain_data = {
        "surname": "Scott",
        "name": "Ridley",
        "age": 21,
        "position": "captain",
        "speciality": "research engineer",
        "address": "module_1",
        "email": "scott_chief@mars.org"
    }

    captain = User(**captain_data)

    session.add(captain)
    session.commit()

    colonists_data = [
        {
            "surname": "Smith",
            "name": "John",
            "age": 30,
            "position": "engineer",
            "speciality": "mechanical engineer",
            "address": "module_2",
            "email": "john_smith@mars.org"
        },
        {
            "surname": "Johnson",
            "name": "Emily",
            "age": 28,
            "position": "botanist",
            "speciality": "agricultural scientist",
            "address": "module_3",
            "email": "emily_johnson@mars.org"
        },
        {
            "surname": "Garcia",
            "name": "Carlos",
            "age": 25,
            "position": "doctor",
            "speciality": "medical doctor",
            "address": "module_4",
            "email": "carlos_garcia@mars.org"
        }
    ]

    colonists = [User(**data) for data in colonists_data]

    session.add_all(colonists)
    session.commit()
    print('Done')


def add_job():
    session = db_session.create_session()
    cap_job = {
        "team_leader": 1,
        "job": "deployment of residential modules 1 and 2",
        "work_size": 15,
        "collaborators": '2, 3',
        "is_finished": False
    }

    captain = Jobs(**cap_job)

    session.add(captain)
    session.commit()
    print('Done_Job')


def main():
    db_session.global_init("db/blogs.db")
    add_job()
    app.run()


if __name__ == '__main__':
    main()
