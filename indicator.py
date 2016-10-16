import debug
import json
import requests
import requests_toolbelt.adapters.appengine

# Use the App Engine Requests adapter. This makes sure that Requests uses URLFetch.
requests_toolbelt.adapters.appengine.monkeypatch()


class Indicator(object):
    def __init__(self, num, name, baseline=0, target=0):
        self.num = num
        self.name = name
        self.baseline = baseline
        self.target = target
        self.milestones = []

    def display(self):
        notification = "Indicator: " + str(self.num) + ":" + self.name + "\nBaseline: " + self.baseline + "\nTarget: " +  self.target + "\n"
        print notification

        self.print_slack(notification)

    def add_milestone(self, ms):
        self.milestones.append(ms)
        if debug.state:
            print "[milestone added]"

    def print_milestones(self):
        for i in self.milestones:
            i.display()

    def print_slack(self, notification):
        url = 'https://hooks.slack.com/services/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'

        data = {}
        data['channel'] = '#random'
        data['username'] = 'webhookbot'
        data['text'] = notification
        data['icon_emoji'] = ':ghost'

        payload = json.dumps(data)


        # POST with JSON
        r = requests.post(url, payload)

        # Response, status etc
        r.text
        r.status_code
        print r.text, r.status_code

