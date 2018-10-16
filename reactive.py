import abc
import time


class Observer(abc.ABC):
    @abc.abstractmethod
    def on_event(self, event):
        pass


class Observable(abc.ABC):
    def __init__(self):
        self.observers = set()
    
    def subscribe(self, subscriber):
        if not isinstance(subscriber, Observer):
            raise ValueError('only Observer objects are subscribers')
        self.observers.add(subscriber)

    def _event(self, event):
        for obs in self.observers:
            obs.on_event(event)


class AnimalEvent:
    def __init__(self, source, action, value=''):
        self.source = source
        self.action = action
        self.value = value


class Animal(Observable):
    def __init__(self, name, sound):
        super().__init__()
        self.name = name
        self.sound = sound

    def run(self):
        print('wait a sec ...')
        time.sleep(1)
        self._event(AnimalEvent(self, 'this action', 'value'))


class Output(Observer):
    def __init__(self, *sources):
        super().__init__()

        for source in sources:
            source.subscribe(self)

    def on_event(self, event):
        print(event.source.name, 'says', event.source.sound)


if __name__ == '__main__':
    tiger = Animal('tigra', 'rrrrraaaaa')
    cow = Animal('momo', 'moooo')

    out = Output(tiger, cow)

    tiger.run()