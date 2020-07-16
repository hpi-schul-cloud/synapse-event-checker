import logging

logger = logging.getLogger(__name__)

class EventChecker(object):
    def __init__(self, config, hs):
        self._block_room_creation = config.get("block_room_creation", False)
        self._room_creators_whitelist = config.get("room_creators_whitelist", [])

        logger.warning("EventChecker")

        self.store = self.hs.get_datastore()

        threepids = await self.store.user_get_threepids("@sync:matrix.stomt.com")
        logger.warning("threepids loaded")

        #addresses = []
        #for threepid in threepids:
        #    if threepid["medium"] == "email":
        #        addresses.append(threepid["address"])

    def check_event_for_spam(self, event):
        return False  # not spam

    def user_may_invite(self, inviter_user_id, invitee_user_id, room_id):
        return True  # allowed

    def user_may_create_room(self, user_id):
        if self._block_room_creation:
            for whitelisted_user_id in self._room_creators_whitelist:
                # can apply if the user_id is defined without a homeserver
                if user_id.startswith(whitelisted_user_id + ":"):
                    return True  # allowed
                # can apply if the user_id is defined without a homeserver
                if user_id.startswith("@" + whitelisted_user_id + ":"):
                    return True  # allowed
                # can apply if the full user_id with homeserver is defined
                if user_id == whitelisted_user_id:
                    return True  # allowed
            return False  # not allowed
        return True  # allowed

    def user_may_create_room_alias(self, user_id, room_alias):
        return True  # allowed

    def user_may_publish_room(self, user_id, room_id):
        return True  # allowed

    @staticmethod
    def parse_config(config):
        return config  # no parsing needed
