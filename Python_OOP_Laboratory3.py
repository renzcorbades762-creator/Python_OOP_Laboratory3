from abc import ABC, abstractmethod

class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):

    def send(self, message):
        print(f"Sending Email: {message}")


class SMSNotification(Notification):

    def send(self, message):
        print(f"Sending SMS: {message}")

class AppNotification(Notification):

    def send(self, message):
        print(f"Sending App Notification: {message}")

notifications = [
    EmailNotification(),
    SMSNotification(),
    AppNotification()
]
for notification in notifications:
    notification.send("Enrollment is now open!")