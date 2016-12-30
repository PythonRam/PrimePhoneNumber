"""
Get Data from Google contacts
"""
import pickle
import gdata.data
import gdata.contacts.client
import gdata.contacts.data
from gdata.gauth import OAuth2Token
from oauth2client.client import flow_from_clientsecrets
from oauth2client import tools
from oauth2client.file import Storage


class GetDataFromGoogleContacts(object):
    """
    Extracts data from google contacts and saves it as pickle file.
    """
    max_results = 1000

    def make_pikle_file(self, gd_client, path_to_pickle_json):
        """
        Dumps the contacts info into pickle file.
        """
        query = gdata.contacts.client.ContactsQuery()
        query.max_results = self.max_results
        feed = gd_client.GetContacts(q=query)
        with open(path_to_pickle_json, 'wb')as pk:
            pickle.dump(feed, pk)

    def authorize(self, path_to_client_json, path_to_storage_json):
        """
        Gets OAuth Verfication and Authorizes the client
        """
        scope = 'https://www.googleapis.com/auth/contacts.readonly'
        gd_client = gdata.contacts.client.ContactsClient()
        flow = flow_from_clientsecrets(
            path_to_client_json, scope=scope, redirect_uri='http://pythonram.github.io')
        storage = Storage(path_to_storage_json)
        credentials = storage.get()
        if credentials is None or credentials.invalid:
            credentials = tools.run_flow(flow, storage)
        token = OAuth2Token(client_id='', client_secret='', scope=scope,
                            user_agent='app.testing', access_token=credentials.access_token)
        token.authorize(gd_client)
        return gd_client

    def run(self, path_to_client_json, path_to_storage_json, path_to_pickle_json):
        """
        Gets the data and saves it in a pickle file
        """
        gd_client = self.authorize(path_to_client_json, path_to_storage_json)
        self.make_pikle_file(gd_client, path_to_pickle_json)
        