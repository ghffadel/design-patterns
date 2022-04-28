class IObserver:  # interface
    def update(self, subject):
        pass


class ISubject:  # interface
    def attach(self, observer):
        pass

    def detach(self, observer):
        pass

    def notify(self):
        pass


class WeatherData(ISubject):
    def __init__(self):
        self.observers = []
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    def measurementsChanged(self):
        self.notify()

    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurementsChanged()

class CurrentConditionsDisplay(IObserver):
    def __init__(self, weather_data):
        self.weather_data = weather_data
        self.weather_data.attach(self)
    def update(self, subject):
        self.temperature = subject.temperature
        self.humidity = subject.humidity
        self.display()

    def display(self):
        print("Current conditions: %.1fF degrees and %.1f%% humidity" % (self.temperature, self.humidity))

class StatisticsDisplay(IObserver):
    def __init__(self, weatherData):
        self.weatherData = weatherData
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0
        self.weatherData.attach(self)

    def update(self, subject):
        self.temperature = subject.temperature
        self.humidity = subject.humidity
        self.pressure = subject.pressure
        self.display()

    def display(self):
        print("Avg/Max/Min temperature = %.1f/%.1f/%.1f" % (self.temperature, self.humidity, self.pressure))

class ForecastDisplay(IObserver):
    def __init__(self, weatherData):
        self.weatherData = weatherData
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0
        self.weatherData.attach(self)

    def update(self, subject):
        self.temperature = subject.temperature
        self.humidity = subject.humidity
        self.pressure = subject.pressure
        self.display()

    def display(self):
        print("Forecast: Avg/Max/Min temperature = %.1f/%.1f/%.1f \n" % (self.temperature, self.humidity, self.pressure))

class PortugueseDisplay(IObserver):
    def __init__(self, weatherData):
        self.weatherData = weatherData
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0
        self.weatherData.attach(self)

    def update(self, subject):
        self.temperature = subject.temperature
        self.humidity = subject.humidity
        self.pressure = subject.pressure
        self.display()

    def display(self):
        print("Temperatura: %.1f graus e %.1f%% de humidade" % (self.temperature, self.humidity))

class Main:
    def __init__(self):
        self.weatherData = WeatherData()
        self.currentDisplay = CurrentConditionsDisplay(self.weatherData)
        self.statisticsDisplay = StatisticsDisplay(self.weatherData)
        self.portugueseDisplay = PortugueseDisplay(self.weatherData)
        self.forecastDisplay = ForecastDisplay(self.weatherData)
      
    def run(self):
        print("\n")
        self.weatherData.setMeasurements(80, 65, 30.4)
        self.weatherData.setMeasurements(82, 70, 29.2)
        self.weatherData.setMeasurements(78, 90, 29.2)
        self.weatherData.setMeasurements(80, 95, 29.2)
        self.weatherData.setMeasurements(82, 100, 29.2)
        self.weatherData.setMeasurements(78, 90, 29.2)
        self.weatherData.setMeasurements(80, 95, 29.2)
        

if __name__ == "__main__":
    Main().run()