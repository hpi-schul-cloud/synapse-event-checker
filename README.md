# synapse-event-checker
A event checker module for Synapse to block certain user events. Based on Synapse [Spam Checker](https://github.com/matrix-org/synapse/blob/master/docs/spam_checker.md) configuration.


## Installation

In your Synapse python environment:
```bash
pip install git+https://github.com/schul-cloud/synapse-event-checker#egg=synapse-event-checker
```

Then add to your `homeserver.yaml`:
```yaml
spam_checker:
  module: "synapse_event_checker.EventChecker"
  config:
    # A list of homeservers to block invites from.
    block_room_creation: true
    room_creators_whitelist:
      - sync
      - @sync
      - @sync:homeserver
```

Synapse will need to be restarted to apply the changes. To modify the list of homeservers,
update the config and restart Synapse.
