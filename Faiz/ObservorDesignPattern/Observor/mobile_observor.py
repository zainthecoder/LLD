from Faiz.ObservorDesignPattern.Observable import observable_interface
from Faiz.ObservorDesignPattern.Observor.observer import ObserverInterface as observer


class MobileObserver(observer):

    def __init__(self, observable: observable_interface, mobile_number):
        self.observable = observable
        self.mobile_number = mobile_number

    def update(self):
        self._send_message(self.mobile_number, "Product is in stock, hurry up")
        return

    @staticmethod
    def _send_message(mobile_number: str, message: str):
        print(f"Email sent to: {mobile_number} with the message {message}")
        return
