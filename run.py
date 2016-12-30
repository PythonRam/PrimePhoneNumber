"""
START
"""

import phone_numbers
import get_contacts_data


def make():
    """
    Download and build function
    """
    path_to_client_json = raw_input('Enter the name of client.json file: ')
    path_to_auth_json = raw_input('Enter a file name for saving your data: ')
    path_to_storage_json = raw_input('Enter the name of output.json file: ')
    path_to_pickle_file = raw_input('Enter the filename pickle: ')
    path_to_auth_json += '.json'
    path_to_storage_json += '.json'
    path_to_client_json += '.json'
    path_to_pickle_file += '.pk'
    data_extractor = get_contacts_data.GetDataFromGoogleContacts()
    data_extractor.run(path_to_client_json,
                       path_to_auth_json, path_to_pickle_file)
    data_maker = phone_numbers.PhoneNumbers()
    data_maker.run(path_to_pickle_file, path_to_storage_json)


def build():
    """
    build function
    """
    path_to_storage_json = raw_input('Enter the name of output.json file: ')
    path_to_pickle_file = raw_input('Enter the filename pickle: ')
    path_to_storage_json += '.json'
    path_to_pickle_file += '.pk'
    data_maker = phone_numbers.PhoneNumbers()
    data_maker.run(path_to_pickle_file, path_to_storage_json)


def main():
    """
    Choose your option
    """
    print "1.Make the file (Download and build the files)"
    print "2.Build the file(Run 1 atleast once before this)"
    while True:
        i = input('Enter the option:')
        if i is 1:
            make()
            break
        elif i is 2:
            build()
            break
        else:
            print 'Check the input'
            continue
    print "Open our output file for the data"
main()
