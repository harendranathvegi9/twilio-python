# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest.api.v2010.account.available_phone_number.local import LocalList
from twilio.rest.api.v2010.account.available_phone_number.mobile import MobileList
from twilio.rest.api.v2010.account.available_phone_number.toll_free import TollFreeList
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource
from twilio.rest.page import Page


class AvailablePhoneNumberCountryList(ListResource):

    def __init__(self, version, account_sid):
        """
        Initialize the AvailablePhoneNumberCountryList
        
        :param Version version: Version that contains the resource
        :param account_sid: A 34 character string that uniquely identifies this resource.
        
        :returns: AvailablePhoneNumberCountryList
        :rtype: AvailablePhoneNumberCountryList
        """
        super(AvailablePhoneNumberCountryList, self).__init__(version)
        
        # Path Solution
        self._solution = {
            'account_sid': account_sid,
        }
        self._uri = '/Accounts/{account_sid}/AvailablePhoneNumbers.json'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams AvailablePhoneNumberCountryInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)
        
        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        limits = self._version.read_limits(limit, page_size)
        
        page = self.page(
            page_size=limits['page_size'],
        )
        
        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def read(self, limit=None, page_size=values.unset):
        """
        Reads AvailablePhoneNumberCountryInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. read() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, read() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)
        
        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of AvailablePhoneNumberCountryInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50
        
        :returns: Page of AvailablePhoneNumberCountryInstance
        :rtype: Page
        """
        params = values.of({
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        
        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )
        
        return AvailablePhoneNumberCountryPage(
            self._version,
            response,
            account_sid=self._solution['account_sid'],
        )

    def get(self, country_code):
        """
        Constructs a AvailablePhoneNumberCountryContext
        
        :param country_code: The country_code
        
        :returns: AvailablePhoneNumberCountryContext
        :rtype: AvailablePhoneNumberCountryContext
        """
        return AvailablePhoneNumberCountryContext(
            self._version,
            account_sid=self._solution['account_sid'],
            country_code=country_code,
        )

    def __call__(self, country_code):
        """
        Constructs a AvailablePhoneNumberCountryContext
        
        :param country_code: The country_code
        
        :returns: AvailablePhoneNumberCountryContext
        :rtype: AvailablePhoneNumberCountryContext
        """
        return AvailablePhoneNumberCountryContext(
            self._version,
            account_sid=self._solution['account_sid'],
            country_code=country_code,
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.AvailablePhoneNumberCountryList>'


class AvailablePhoneNumberCountryPage(Page):

    def __init__(self, version, response, account_sid):
        """
        Initialize the AvailablePhoneNumberCountryPage
        
        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: A 34 character string that uniquely identifies this resource.
        
        :returns: AvailablePhoneNumberCountryPage
        :rtype: AvailablePhoneNumberCountryPage
        """
        super(AvailablePhoneNumberCountryPage, self).__init__(version, response)
        
        # Path Solution
        self._solution = {
            'account_sid': account_sid,
        }

    def get_instance(self, payload):
        """
        Build an instance of AvailablePhoneNumberCountryInstance
        
        :param dict payload: Payload response from the API
        
        :returns: AvailablePhoneNumberCountryInstance
        :rtype: AvailablePhoneNumberCountryInstance
        """
        return AvailablePhoneNumberCountryInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.AvailablePhoneNumberCountryPage>'


class AvailablePhoneNumberCountryContext(InstanceContext):

    def __init__(self, version, account_sid, country_code):
        """
        Initialize the AvailablePhoneNumberCountryContext
        
        :param Version version: Version that contains the resource
        :param account_sid: The account_sid
        :param country_code: The country_code
        
        :returns: AvailablePhoneNumberCountryContext
        :rtype: AvailablePhoneNumberCountryContext
        """
        super(AvailablePhoneNumberCountryContext, self).__init__(version)
        
        # Path Solution
        self._solution = {
            'account_sid': account_sid,
            'country_code': country_code,
        }
        self._uri = '/Accounts/{account_sid}/AvailablePhoneNumbers/{country_code}.json'.format(**self._solution)
        
        # Dependents
        self._local = None
        self._toll_free = None
        self._mobile = None

    def fetch(self):
        """
        Fetch a AvailablePhoneNumberCountryInstance
        
        :returns: Fetched AvailablePhoneNumberCountryInstance
        :rtype: AvailablePhoneNumberCountryInstance
        """
        params = values.of({})
        
        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )
        
        return AvailablePhoneNumberCountryInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            country_code=self._solution['country_code'],
        )

    @property
    def local(self):
        """
        Access the local
        
        :returns: LocalList
        :rtype: LocalList
        """
        if self._local is None:
            self._local = LocalList(
                self._version,
                country_code=self._solution['country_code'],
                account_sid=self._solution['account_sid'],
            )
        return self._local

    @property
    def toll_free(self):
        """
        Access the toll_free
        
        :returns: TollFreeList
        :rtype: TollFreeList
        """
        if self._toll_free is None:
            self._toll_free = TollFreeList(
                self._version,
                country_code=self._solution['country_code'],
                account_sid=self._solution['account_sid'],
            )
        return self._toll_free

    @property
    def mobile(self):
        """
        Access the mobile
        
        :returns: MobileList
        :rtype: MobileList
        """
        if self._mobile is None:
            self._mobile = MobileList(
                self._version,
                country_code=self._solution['country_code'],
                account_sid=self._solution['account_sid'],
            )
        return self._mobile

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.AvailablePhoneNumberCountryContext {}>'.format(context)


class AvailablePhoneNumberCountryInstance(InstanceResource):

    def __init__(self, version, payload, account_sid, country_code=None):
        """
        Initialize the AvailablePhoneNumberCountryInstance
        
        :returns: AvailablePhoneNumberCountryInstance
        :rtype: AvailablePhoneNumberCountryInstance
        """
        super(AvailablePhoneNumberCountryInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'country_code': payload['country_code'],
            'country': payload['country'],
            'uri': payload['uri'],
            'beta': payload['beta'],
            'subresource_uris': payload['subresource_uris'],
        }
        
        # Context
        self._context = None
        self._solution = {
            'account_sid': account_sid,
            'country_code': country_code or self._properties['country_code'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context
        
        :returns: AvailablePhoneNumberCountryContext for this AvailablePhoneNumberCountryInstance
        :rtype: AvailablePhoneNumberCountryContext
        """
        if self._context is None:
            self._context = AvailablePhoneNumberCountryContext(
                self._version,
                account_sid=self._solution['account_sid'],
                country_code=self._solution['country_code'],
            )
        return self._context

    @property
    def country_code(self):
        """
        :returns: The country_code
        :rtype: unicode
        """
        return self._properties['country_code']

    @property
    def country(self):
        """
        :returns: The country
        :rtype: unicode
        """
        return self._properties['country']

    @property
    def uri(self):
        """
        :returns: The uri
        :rtype: unicode
        """
        return self._properties['uri']

    @property
    def beta(self):
        """
        :returns: The beta
        :rtype: bool
        """
        return self._properties['beta']

    @property
    def subresource_uris(self):
        """
        :returns: The subresource_uris
        :rtype: unicode
        """
        return self._properties['subresource_uris']

    def fetch(self):
        """
        Fetch a AvailablePhoneNumberCountryInstance
        
        :returns: Fetched AvailablePhoneNumberCountryInstance
        :rtype: AvailablePhoneNumberCountryInstance
        """
        return self._proxy.fetch()

    @property
    def local(self):
        """
        Access the local
        
        :returns: local
        :rtype: local
        """
        return self._proxy.local

    @property
    def toll_free(self):
        """
        Access the toll_free
        
        :returns: toll_free
        :rtype: toll_free
        """
        return self._proxy.toll_free

    @property
    def mobile(self):
        """
        Access the mobile
        
        :returns: mobile
        :rtype: mobile
        """
        return self._proxy.mobile

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.AvailablePhoneNumberCountryInstance {}>'.format(context)
