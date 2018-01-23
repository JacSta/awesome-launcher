import random
import string


class Details:
    def __init__(self, selenium):
        self.selenium = selenium
        self.nip_number = self.nip_generator()
        self.email = self.email_generator()
        self.login = self.login_generator()
        self.password = 'test567!'

    @staticmethod
    def email_generator():
        return Details.__generate_string()+'@test.pl'

    @staticmethod
    def login_generator():
        return Details.__generate_string()+'selenium'

    @staticmethod
    def __generate_string(chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(7))

    def purchaser_details_array(self):
        return {
            'pNip': self.nip_number,
            'pName': 'Jan',
            'pSurname': 'Nabywca',
            'pPhone': '555777888',
            'pCity': 'Gdynia',
            'pStreetName': 'Kolorowa',
            'pStreetNumber': '37/1',
            'pEmail': self.email,
            'pPostalCode': '12345',
        }

    def nip_generator(self):
        """Generates NIP number"""
        weight = [6, 5, 7, 2, 3, 4, 5, 6, 7]
        nip = []

        for x in range(0, 9, 1):
            nip.extend([random.randint(0, 9)])
        temp_sum = 0
        for y in range(0, 9, 1):
            add = nip[y] * weight[y]
            temp_sum = add + temp_sum
        check_sum = temp_sum % 11

        if check_sum >= 10:
            return self.nip_generator()
        else:
            nip.extend([check_sum])
            temp_nip = (''.join([str(x) for x in nip]))
            return temp_nip
