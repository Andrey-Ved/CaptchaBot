import json
import logging


class User:
    def __init__(self, verified, added, captcha):
        self.verified = verified
        self.added = added
        self.captcha = captcha

    def __str__(self):
        return ' '.join(
            map(str, (
                self.verified,
                self.added,
                self.captcha
            ))
        )

    def to_dict(self):
        return {
            'verified': self.verified,
            'added': self.added,
            'captcha': self.captcha
        }


class Users:
    def __init__(self):
        self.users = {}

    def __str__(self):
        return '\n'.join(f'{str(k)} {str(self.users[k])}' for k in self.users)

    def add(self, user_id, user_verified, user_added, user_captcha):
        self.users[user_id] = User(user_verified, user_added, user_captcha)

    def __setitem__(self, user_id, value):
        user_verified, user_added, user_captcha = value
        self.add(user_id, user_verified, user_added, user_captcha)

    def __getitem__(self, item):
        return self.users[item]

    def __delitem__(self, item):
        if self.__contains__(item):
            del self.users[item]

    def __contains__(self, item):
        return item in self.users


class UsersWithFile(Users):
    def __init__(self, file):
        super().__init__()
        self.file = file
        try:
            with open(file, 'r') as file:
                users_json = json.load(file)

            for k in users_json:
                self.users[int(k)] = User(
                    users_json[k]['verified'],
                    users_json[k]['added'],
                    users_json[k]['captcha']
                )

        except FileNotFoundError as e:
            logging.info(e)

    def writing_to_file(self):
        data = {}
        for k in self.users:
            data[k] = self.users[k].to_dict()
        with open(self.file, 'w') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def add(self, *args, **kwargs):
        super().add(*args, **kwargs)
        self.writing_to_file()

    def __delitem__(self, item):
        super().__delitem__(item)
        self.writing_to_file()
