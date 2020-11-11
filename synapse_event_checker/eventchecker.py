from typing import Dict

from synapse.api.constants import EventTypes, JoinRules, Membership, RoomCreationPreset
from synapse.api.errors import SynapseError
from synapse.events import EventBase
from synapse.module_api import ModuleApi
from synapse.types import Requester, StateMap

import requests

class EventChecker(object):
    def __init__(self, config: Dict, module_api: ModuleApi):
        self.module_api = module_api
        self._room_creators_whitelist = config.get('room_creators_whitelist')
        self._permission_endpoint = config.get("permission_endpoint")

    @staticmethod
    def parse_config(config: Dict) -> Dict:
        """Parses and validates the options specified in the homeserver config.
        Args:
            config: The config dict.
        Returns:
            The config dict.
        Raises:
            ConfigError: If there was an issue with the provided module configuration.
        """
        return config


    async def on_create_room(self, requester: Requester, config: Dict, is_requester_admin: bool) -> bool:
        """Implements synapse.events.ThirdPartyEventRules.on_create_room.
        Args:
            requester: The user who is making the createRoom request.
            config: The createRoom config dict provided by the user.
            is_requester_admin: Whether the requester is a Synapse admin.
        Returns:
            True if the request should be allowed, False otherwise.
        """
        user_prefix = '@sso_'
        user_id, servername, *_ = requester.user.to_string().split(':')
        if user_id.startswith(user_prefix):
            user_id = user_id[len(user_prefix):]

        if any(user_id == whitelisted_user_id for whitelisted_user_id in self._room_creators_whitelist):
            return True

        request_result = requests.get(self._permission_endpoint + user_id)
        if request_result.json().get('createRoom'):
            return True
        return False


    async def check_event_allowed(self, event: EventBase, state_events: StateMap[EventBase]) -> bool:
        """Implements synapse.events.ThirdPartyEventRules.check_event_allowed.

        Checks the event's type and the current rule and calls the right function to
        determine whether the event can be allowed.
        Args:
            event: The event to check.
            state_events: A dict mapping (event type, state key) to state event.
                State events in the room the event originated from.
        Returns:
            True if the event can be allowed, False otherwise.
        """
        return True

