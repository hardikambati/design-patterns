from datetime import datetime
from abc import (
    ABC,
    abstractmethod,
)


# ----------------- DATA-SOURCE : Database -----------------
# add any data source (postgresql db, mongodb, etc) here,
# with specified functions in the abstract class


class DataSource(ABC):
    """
    Abstract class for defining the data source
    eg : dict or DB (in our case)

    Extend this class and implement the following methods while
    creating new data source
    """

    @abstractmethod
    def get_source(self):
        """
        Abstract method for getting the source
        Should return all users
        """
        pass

    @abstractmethod
    def add_user(self, user):
        """
        Add user logic
        Return user instance
        """
        pass

    @abstractmethod
    def get_users(self):
        """
        Return all users
        """
        pass

    @abstractmethod
    def get_single_user(self, username):
        """
        Return single instance
        """
        pass

    @abstractmethod
    def delete_user(self, username) -> None:
        """
        Delete user logic
        """
        pass

    @abstractmethod
    def delete_user(self) -> None:
        """
        Print all users
        """
        pass


class DictDB(DataSource):
    """
    Database : Stores data in dict
    """

    def __init__(self) -> None:
        self.users = {}
        self.index = 1    # refers to user id count

    def get_source(self) -> None:
        return self.users
    
    def add_user(self, user):
        self.users[user.username] = user
        return user
    
    def get_users(self):
        return self.users
    
    def get_single_user(self, username):
        user = self.users[username]
        return user
    
    def delete_user(self, username) -> None:
        del self.users[username]

    def print_users(self) -> None:
        for key, value in self.users.items():
                print(f'\nid       : {value.id}')
                print(f'username : {value.username}')
                print(f'password : {value.password}')
                print(f'role     : {value.role}')
                print(f'loggedin : {value.last_login_timestamp}')


# ----------------- RESPONSE : Custom response -----------------


class CustomResponse:
    """
    Dict response with a particular structure
    To handle success, failure and error cases
    """
    
    def __init__(self, status_code: int, detail: dict,  error: bool=False):
        self.status_code = status_code
        self.error       = error
        self.detail      = detail


    def response(self) -> dict:
        return {
            'status_code': self.status_code,
            'error': self.error,
            'detail': self.detail
        }
    

# ----------------- USER : Base and Management -----------------


class Session:
    """
    Store the session info about the user login
    """

    def __init__(self) -> None:
        self.last_login_timestamp = None


class User(Session):
    """
    Store info about the user
    """

    def __init__(self, id: int, username: str, password: str, role: str) -> None:
        super().__init__()

        self.id       = id
        self.username = username
        self.password = password
        self.role     = role


class AuthManagement:
    """
    Managing auth for users 
    """

    def __init__(self, db: DictDB) -> None:
        self.db = db

    def login(self, username: str, password: str) -> None:
        if not username in self.db.get_users():
            raise TypeError(f'Invalid username')
        user_instance: User = self.db.get_single_user(username)

        if password != user_instance.password:
            raise TypeError(f'Invalid password')
        
        # set login timestamp
        user_instance.last_login_timestamp = datetime.now()
        print(f'user {username} : logged in')


    def logout(self, username: str) -> None:
        print(f'user {username} : logged out')


class UserManagement:
    """
    Managing CRUD operations for users
    """

    all_user_roles = ['user', 'admin', 'manager']


    def __init__(self, db: DictDB) -> None:
        self.db = db

    def create_user(self, username: str, password: str, role: str=all_user_roles[0]) -> User:
        """
        Creates a user
        """

        # check for valid role
        if role not in self.all_user_roles:
            raise TypeError(f'Invalid role : {role}')
        
        # check for already existing username
        if username in self.db.get_users():
            raise TypeError(f'User with username {username} already exists')
        user = User(
            id=self.db.index,
            username=username,
            password=password,
            role=role
        )
        self.db.add_user(user=user)
        self.db.index += 1
        return user
    
    def delete_user(self, username: str) -> None:
        """
        Deletes a user based on username
        """

        if not username in self.db.get_users():
            raise TypeError(f'User with username {username} does not exist')
        self.db.delete_user(username)

    def all_users(self) -> None:
        """
        Prints all users
        """
        self.db.print_users()


if __name__ == '__main__':

    # create instances here
    
    db = DictDB()

    um = UserManagement(db)

    um.create_user(
        username='hardik',
        password='hello123',
        role='admin'
    )
    um.create_user(
        username='heisenberg',
        password='meth123',
        role='user'

    )

    # am = AuthManagement(db)
    # am.login('hardik', 'hello123')

    um.all_users()

