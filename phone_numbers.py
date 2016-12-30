"""
Working on extracted data
"""
from json import dumps
from pickle import load
import prime_factors


class PhoneNumbers(object):
    """
    Converts data recieved to a readable format.
    """

    def __load_data_from_pickle__(self, path_to_pickle_file):
        with open(path_to_pickle_file, 'rb') as pk:
            feed = load(pk)
            return feed

    def __format_phone_number__(self, string):
        """
        Formats the phonenumber into integer
        """
        string = string.replace("\n", "").encode('utf-8').strip()
        string = string.replace(" ", "")
        string = string.replace("+91", "")
        if len(string) >= 10:
            string = string[-10:]
        if string == "":
            return False, string
        if len(string) == 10 and string.isdigit():
            return True, int(str(string))
        return False, string

    def __get_phone_numbers__(self, phone_number_obj):
        """
        Returns list of phone numbers
        """
        phone_numbers_list = []
        for elem in phone_number_obj:
            chk, pnum = self.__format_phone_number__(elem.text)
            if chk:
                phone_numbers_list.append(pnum)
        return phone_numbers_list

    def __make_dictionary__(self, feed):
        """
        Returns dictionary of useful data
        """
        contacts = {}
        for i, entry in enumerate(feed. entry):
            i += 1
            try:
                name = entry.name.full_name.text
                phone_number_list = self.__get_phone_numbers__(
                    entry.phone_number)
                contacts[name] = {}
                for number in phone_number_list:
                    arr = prime_factors.PrimeNumbers(number).all_factors()
                    arr1 = prime_factors.PrimeNumbers(number).prime_factors()
                    arr1 = list(set(arr1))
                    arr.sort()
                    arr1.sort()
                    contacts[name][number] = {}
                    contacts[name][number]['Number of factors'] = len(arr)
                    contacts[name][number]['factors'] = arr
                    contacts[name][number][
                        'Number of prime factors'] = len(arr1)
                    contacts[name][number]['Prime Factors'] = arr1
            except AttributeError:
                pass
        return contacts

    def __dump_dictionary__(self, data, path):
        """
        Writes data into a json file
        """
        with open(path, 'w') as dictionary:
            dictionary.write(dumps(data, sort_keys=True,
                                   indent=4, separators=(',', ': ')))

    def run(self, path_to_pickle_file, path_to_json_file):
        """
        Magic starts
        """
        feed = self.__load_data_from_pickle__(path_to_pickle_file)
        contacts = self.__make_dictionary__(feed)
        self.__dump_dictionary__(contacts, path_to_json_file)
