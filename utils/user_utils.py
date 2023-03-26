from utils.file_utils import FileUtils


class Recipients(object):
    def __init__(self, path_to_recipients=None):
        self.file_utils = FileUtils()
        path_to_recipients = path_to_recipients if path_to_recipients else \
            'C:\\Users\\annac\\IdeaProjects\\Learning\\users_data\\recipients.json'
        self.recipients_list = self.file_utils.read_json_file(path_to_recipients)


class Senders(object):
    def __init__(self, path_to_senders=None):
        self.file_utils = FileUtils()
        path_to_senders = path_to_senders if path_to_senders else \
            'C:\\Users\\annac\\IdeaProjects\\Learning\\users_data\\sender.json'
        self.senders = self.file_utils.read_json_file(path_to_senders)


class UsersData(Recipients, Senders):
    def __init__(self, recipients=None, senders=None):
        super(UsersData, self).__init__(path_to_recipients=recipients)
        Senders.__init__(self, path_to_senders=senders)
