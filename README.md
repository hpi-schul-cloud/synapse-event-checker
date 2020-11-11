# synapse-event-checker
A event checker module for Synapse to block certain user events. Based on Synapse [RoomAccessRules](https://github.com/matrix-org/synapse-dinsic/blob/dinsic/synapse/third_party_rules/access_rules.py) configuration.


## Installation

In your Synapse python environment:
```bash
pip install git+https://github.com/schul-cloud/synapse-event-checker#egg=synapse-event-checker
```

Then add to your `homeserver.yaml`:
```yaml
third_party_event_rules:
  module: "synapse_event_checker.EventChecker"
  config:
    # A list of homeservers to block invites from.
    block_room_creation: true
    permission_endpoint: "http://server:3030/messengerPermissions/"
    room_creators_whitelist:
      - "@sync"
```

Synapse will need to be restarted to apply the changes. To modify the list of homeservers,
update the config and restart Synapse.
