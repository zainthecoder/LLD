from Faiz.ObservorDesignPattern.Observable.iphone_observable import IphoneObservable
from Faiz.ObservorDesignPattern.Observor.observer import ObserverInterface
from Faiz.ObservorDesignPattern.Observor.mobile_observor import MobileObserver
from Faiz.ObservorDesignPattern.Observor.email_observor import EmailObserver


class Store:
    iphonestock = IphoneObservable()
    observors: list[ObserverInterface] = [MobileObserver(iphonestock, "1234"),
                                          EmailObserver(iphonestock, "test@gmail.com"),
                                          EmailObserver(iphonestock, "check@gmail.com")]
    for observer in observors:
        iphonestock.add(observer)
    iphonestock.set_stock_count(10)
