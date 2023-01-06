import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig():
    @staticmethod
    def getapplicationurl():
        url = config.get('Common info', 'baseURL')
        return url

    @staticmethod
    def getusername():
        useremail = config.get('Common info', 'username')
        return useremail

    @staticmethod
    def getpassword():
        password = config.get('Common info', 'password')
        return password
