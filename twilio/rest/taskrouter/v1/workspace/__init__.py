# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource
from twilio.rest.page import Page
from twilio.rest.taskrouter.v1.workspace.activity import ActivityList
from twilio.rest.taskrouter.v1.workspace.event import EventList
from twilio.rest.taskrouter.v1.workspace.task import TaskList
from twilio.rest.taskrouter.v1.workspace.task_queue import TaskQueueList
from twilio.rest.taskrouter.v1.workspace.worker import WorkerList
from twilio.rest.taskrouter.v1.workspace.workflow import WorkflowList
from twilio.rest.taskrouter.v1.workspace.workspace_statistics import WorkspaceStatisticsList


class WorkspaceList(ListResource):

    def __init__(self, version):
        """
        Initialize the WorkspaceList
        
        :param Version version: Version that contains the resource
        
        :returns: WorkspaceList
        :rtype: WorkspaceList
        """
        super(WorkspaceList, self).__init__(version)
        
        # Path Solution
        self._solution = {}
        self._uri = '/Workspaces'.format(**self._solution)

    def stream(self, friendly_name=values.unset, limit=None, page_size=None):
        """
        Streams WorkspaceInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param unicode friendly_name: The friendly_name
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
            friendly_name=friendly_name,
            page_size=limits['page_size'],
        )
        
        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def read(self, friendly_name=values.unset, limit=None, page_size=values.unset):
        """
        Reads WorkspaceInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param unicode friendly_name: The friendly_name
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
            friendly_name=friendly_name,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, friendly_name=values.unset, page_token=values.unset,
             page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of WorkspaceInstance records from the API.
        Request is executed immediately
        
        :param unicode friendly_name: The friendly_name
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50
        
        :returns: Page of WorkspaceInstance
        :rtype: Page
        """
        params = values.of({
            'FriendlyName': friendly_name,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        
        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )
        
        return WorkspacePage(
            self._version,
            response,
        )

    def create(self, friendly_name, event_callback_url=values.unset,
               template=values.unset):
        """
        Create a new WorkspaceInstance
        
        :param unicode friendly_name: The friendly_name
        :param unicode event_callback_url: The event_callback_url
        :param unicode template: The template
        
        :returns: Newly created WorkspaceInstance
        :rtype: WorkspaceInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'EventCallbackUrl': event_callback_url,
            'Template': template,
        })
        
        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )
        
        return WorkspaceInstance(
            self._version,
            payload,
        )

    def get(self, sid):
        """
        Constructs a WorkspaceContext
        
        :param sid: The sid
        
        :returns: WorkspaceContext
        :rtype: WorkspaceContext
        """
        return WorkspaceContext(
            self._version,
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a WorkspaceContext
        
        :param sid: The sid
        
        :returns: WorkspaceContext
        :rtype: WorkspaceContext
        """
        return WorkspaceContext(
            self._version,
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkspaceList>'


class WorkspacePage(Page):

    def __init__(self, version, response):
        """
        Initialize the WorkspacePage
        
        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        
        :returns: WorkspacePage
        :rtype: WorkspacePage
        """
        super(WorkspacePage, self).__init__(version, response)
        
        # Path Solution
        self._solution = {}

    def get_instance(self, payload):
        """
        Build an instance of WorkspaceInstance
        
        :param dict payload: Payload response from the API
        
        :returns: WorkspaceInstance
        :rtype: WorkspaceInstance
        """
        return WorkspaceInstance(
            self._version,
            payload,
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkspacePage>'


class WorkspaceContext(InstanceContext):

    def __init__(self, version, sid):
        """
        Initialize the WorkspaceContext
        
        :param Version version: Version that contains the resource
        :param sid: The sid
        
        :returns: WorkspaceContext
        :rtype: WorkspaceContext
        """
        super(WorkspaceContext, self).__init__(version)
        
        # Path Solution
        self._solution = {
            'sid': sid,
        }
        self._uri = '/Workspaces/{sid}'.format(**self._solution)
        
        # Dependents
        self._activities = None
        self._events = None
        self._tasks = None
        self._task_queues = None
        self._workers = None
        self._workflows = None
        self._statistics = None

    def fetch(self):
        """
        Fetch a WorkspaceInstance
        
        :returns: Fetched WorkspaceInstance
        :rtype: WorkspaceInstance
        """
        params = values.of({})
        
        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )
        
        return WorkspaceInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
        )

    def update(self, default_activity_sid=values.unset,
               event_callback_url=values.unset, friendly_name=values.unset,
               timeout_activity_sid=values.unset):
        """
        Update the WorkspaceInstance
        
        :param unicode default_activity_sid: The default_activity_sid
        :param unicode event_callback_url: The event_callback_url
        :param unicode friendly_name: The friendly_name
        :param unicode timeout_activity_sid: The timeout_activity_sid
        
        :returns: Updated WorkspaceInstance
        :rtype: WorkspaceInstance
        """
        data = values.of({
            'DefaultActivitySid': default_activity_sid,
            'EventCallbackUrl': event_callback_url,
            'FriendlyName': friendly_name,
            'TimeoutActivitySid': timeout_activity_sid,
        })
        
        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )
        
        return WorkspaceInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the WorkspaceInstance
        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    @property
    def activities(self):
        """
        Access the activities
        
        :returns: ActivityList
        :rtype: ActivityList
        """
        if self._activities is None:
            self._activities = ActivityList(
                self._version,
                workspace_sid=self._solution['sid'],
            )
        return self._activities

    @property
    def events(self):
        """
        Access the events
        
        :returns: EventList
        :rtype: EventList
        """
        if self._events is None:
            self._events = EventList(
                self._version,
                workspace_sid=self._solution['sid'],
            )
        return self._events

    @property
    def tasks(self):
        """
        Access the tasks
        
        :returns: TaskList
        :rtype: TaskList
        """
        if self._tasks is None:
            self._tasks = TaskList(
                self._version,
                workspace_sid=self._solution['sid'],
            )
        return self._tasks

    @property
    def task_queues(self):
        """
        Access the task_queues
        
        :returns: TaskQueueList
        :rtype: TaskQueueList
        """
        if self._task_queues is None:
            self._task_queues = TaskQueueList(
                self._version,
                workspace_sid=self._solution['sid'],
            )
        return self._task_queues

    @property
    def workers(self):
        """
        Access the workers
        
        :returns: WorkerList
        :rtype: WorkerList
        """
        if self._workers is None:
            self._workers = WorkerList(
                self._version,
                workspace_sid=self._solution['sid'],
            )
        return self._workers

    @property
    def workflows(self):
        """
        Access the workflows
        
        :returns: WorkflowList
        :rtype: WorkflowList
        """
        if self._workflows is None:
            self._workflows = WorkflowList(
                self._version,
                workspace_sid=self._solution['sid'],
            )
        return self._workflows

    @property
    def statistics(self):
        """
        Access the statistics
        
        :returns: WorkspaceStatisticsList
        :rtype: WorkspaceStatisticsList
        """
        if self._statistics is None:
            self._statistics = WorkspaceStatisticsList(
                self._version,
                workspace_sid=self._solution['sid'],
            )
        return self._statistics

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.WorkspaceContext {}>'.format(context)


class WorkspaceInstance(InstanceResource):

    def __init__(self, version, payload, sid=None):
        """
        Initialize the WorkspaceInstance
        
        :returns: WorkspaceInstance
        :rtype: WorkspaceInstance
        """
        super(WorkspaceInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'default_activity_name': payload['default_activity_name'],
            'default_activity_sid': payload['default_activity_sid'],
            'event_callback_url': payload['event_callback_url'],
            'friendly_name': payload['friendly_name'],
            'sid': payload['sid'],
            'timeout_activity_name': payload['timeout_activity_name'],
            'timeout_activity_sid': payload['timeout_activity_sid'],
        }
        
        # Context
        self._context = None
        self._solution = {
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context
        
        :returns: WorkspaceContext for this WorkspaceInstance
        :rtype: WorkspaceContext
        """
        if self._context is None:
            self._context = WorkspaceContext(
                self._version,
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date_updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def default_activity_name(self):
        """
        :returns: The default_activity_name
        :rtype: unicode
        """
        return self._properties['default_activity_name']

    @property
    def default_activity_sid(self):
        """
        :returns: The default_activity_sid
        :rtype: unicode
        """
        return self._properties['default_activity_sid']

    @property
    def event_callback_url(self):
        """
        :returns: The event_callback_url
        :rtype: unicode
        """
        return self._properties['event_callback_url']

    @property
    def friendly_name(self):
        """
        :returns: The friendly_name
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def timeout_activity_name(self):
        """
        :returns: The timeout_activity_name
        :rtype: unicode
        """
        return self._properties['timeout_activity_name']

    @property
    def timeout_activity_sid(self):
        """
        :returns: The timeout_activity_sid
        :rtype: unicode
        """
        return self._properties['timeout_activity_sid']

    def fetch(self):
        """
        Fetch a WorkspaceInstance
        
        :returns: Fetched WorkspaceInstance
        :rtype: WorkspaceInstance
        """
        return self._proxy.fetch()

    def update(self, default_activity_sid=values.unset,
               event_callback_url=values.unset, friendly_name=values.unset,
               timeout_activity_sid=values.unset):
        """
        Update the WorkspaceInstance
        
        :param unicode default_activity_sid: The default_activity_sid
        :param unicode event_callback_url: The event_callback_url
        :param unicode friendly_name: The friendly_name
        :param unicode timeout_activity_sid: The timeout_activity_sid
        
        :returns: Updated WorkspaceInstance
        :rtype: WorkspaceInstance
        """
        return self._proxy.update(
            default_activity_sid=default_activity_sid,
            event_callback_url=event_callback_url,
            friendly_name=friendly_name,
            timeout_activity_sid=timeout_activity_sid,
        )

    def delete(self):
        """
        Deletes the WorkspaceInstance
        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    @property
    def activities(self):
        """
        Access the activities
        
        :returns: activities
        :rtype: activities
        """
        return self._proxy.activities

    @property
    def events(self):
        """
        Access the events
        
        :returns: events
        :rtype: events
        """
        return self._proxy.events

    @property
    def tasks(self):
        """
        Access the tasks
        
        :returns: tasks
        :rtype: tasks
        """
        return self._proxy.tasks

    @property
    def task_queues(self):
        """
        Access the task_queues
        
        :returns: task_queues
        :rtype: task_queues
        """
        return self._proxy.task_queues

    @property
    def workers(self):
        """
        Access the workers
        
        :returns: workers
        :rtype: workers
        """
        return self._proxy.workers

    @property
    def workflows(self):
        """
        Access the workflows
        
        :returns: workflows
        :rtype: workflows
        """
        return self._proxy.workflows

    @property
    def statistics(self):
        """
        Access the statistics
        
        :returns: statistics
        :rtype: statistics
        """
        return self._proxy.statistics

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.WorkspaceInstance {}>'.format(context)
