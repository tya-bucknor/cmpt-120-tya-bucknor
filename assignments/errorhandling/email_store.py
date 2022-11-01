from genericpath import exists


class EmailStore:

    def __init__(self):
        self.emails = []

    def exists(self, email):
        '''
        Method that checks if an email exists in store.
        '''
        return email in self.emails

    def add(self, first_name, last_name):
        '''
        Method that adds a new email to the store.
        The email address is of the format {first_name}.{last_name}{count}@marist.edu
        @return the email that was added.
        '''
        email = None
        # TODO if either first_name or last_name is None raise an exception
        if first_name == None or last_name == None:
            raise Exception("Error, first or last name is none")
        else:
            count = 1
            while True:
                email = f"{first_name}.{last_name}{count}@marist.edu"
                if self.exists (email):
                    count += 1
                    continue
                else:
                    self.emails.append(email)
                    break

        return email

    def remove(self, email):
        '''
        Method that removes an email from the store.
        '''
        # TODO if email doesn't exist, raise an exception.
        if email not in self.emails:
            raise Exception("Email does not exist")
        else:
            self.emails.remove(email)