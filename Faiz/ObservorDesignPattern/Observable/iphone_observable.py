from Faiz.ObservorDesignPattern.Observable.observable_interface import StockObservableInterface
from Faiz.ObservorDesignPattern.Observor.observer import ObserverInterface as observorinterface


class IphoneObservable(StockObservableInterface):

    def __init__(self):
        self.observer_list: list[observorinterface] = []
        self.stock_count = 0

    def add(self, notification_alert_observer: observorinterface):
        self.observer_list.append(notification_alert_observer)

    def remove(self, notification_alert_observer: observorinterface):
        self.observer_list.remove(notification_alert_observer)

    def notify_subscribers(self):
        if not len(self.observer_list) == 0:
            for observer in self.observer_list:
                observer.update()
        return

    def set_stock_count(self, new_stock_added: int):
        if self.stock_count == 0:
            self.notify_subscribers()

        self.stock_count = self.stock_count + 1
        return

    def get_stock_count(self):
        return self.stock_count
