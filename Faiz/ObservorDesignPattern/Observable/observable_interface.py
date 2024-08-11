from Faiz.ObservorDesignPattern.Observor.observer import ObserverInterface as observorinterface


class StockObservableInterface:
    def add(self, notification_alert_observer: observorinterface):
        pass

    def remove(self, notification_alert_observer: observorinterface):
        pass

    def notify_subscribers(self):
        pass

    def get_stock_count(self):
        pass

    def set_stock_count(self, added_stock_count: int):
        pass
