#!/usr/bin/env python3
from __future__ import annotations


class NewsSubject:
    def __init__(self) -> None:
        self._observers: list[
            tuple[
                object,
                set[str] | None
            ]
        ] = []

    def subscribe(
        self,
        observer: object,
        topics: set[str] | None = None
    ) -> None:
        self._observers.append((observer, topics))

    def unsubscribe(self, observer: object) -> None:
        self._observers = [
            (obs, topics)
            for (obs, topics) in self._observers
            if obs != observer
        ]

    def notify(self, topic: str, data: str) -> None:
        for observer, topics in list(self._observers):
            if topics is None or topic in topics:
                observer.update(topic, data)


class LogObserver:
    def update(self, topic: str, data: str) -> None:
        print(f"log:{topic}={data}")


class EmailObserver:
    def update(self, topic: str, data: str) -> None:
        print(f"email:{topic}={data}")


class SmsObserver:
    def update(self, topic: str, data: str) -> None:
        print(f"sms:{topic}={data}")


def main() -> None:
    subject = NewsSubject()

    log = LogObserver()
    email = EmailObserver()

    subject.subscribe(log, topics={"sports", "breaking"})
    subject.subscribe(email, topics=None)

    subject.notify("weather", "rain")
    subject.notify("sports", "goal")
    subject.notify("breaking", "alert")

    sms = SmsObserver()
    subject.subscribe(sms, topics={"breaking"})


if __name__ == "__main__":
    main()
