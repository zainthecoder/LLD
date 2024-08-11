from Faiz.ObservorDesignPattern.Observable import observable_interface
from Faiz.ObservorDesignPattern.Observor.observer import ObserverInterface as observer


class EmailObserver(observer):

    def __init__(self, observable: observable_interface, email_id):
        self.observable = observable
        self.email_id = email_id

    def update(self):
        self._send_email(self.email_id, "Product is in stock, hurry up")
        return

    @staticmethod
    def _send_email(email_id: str, message: str):
        print(f"Email sent to: {email_id} with the message {message}")
        return
