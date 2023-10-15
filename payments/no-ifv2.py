from typing import Dict, Type, Union
from dataclasses import dataclass
from abc import  ABC, abstractmethod

@dataclass
class PaymentStrategy (ABC):
  type:str
  @abstractmethod
  def calculate_amount(this):
    ...

@dataclass
class SalaryStrategy(PaymentStrategy):
  salary:float

  def calculate_amount(this):
    return this.salary / 12

@dataclass
class HourlyStrategy(PaymentStrategy):
  hourly_rate: float
  number_of_hours:float

  def calculate_amount(this):
    return this.hourly_rate * this.number_of_hours
class Employee:


  def __init__(this, name:str, payment_details:Dict[str,Union[str|float]]):
    this.name = name
    this.payment_details = payment_details

  def send_payment(this, stategy:Type[PaymentStrategy]) -> None:
    amount = stategy(**this.payment_details).calculate_amount()

    print(f"Sending ${amount} to {this.name}")


def make_strategy(type:str) -> Type[SalaryStrategy]:
  strategies_available={"salary":SalaryStrategy, "hourly":HourlyStrategy}

  return strategies_available[type]



jennifer = Employee("Jennifer Smith", { "type":"salary", "salary": 135000 })
jennifer.send_payment(make_strategy(jennifer.payment_details['type']))

max = Employee("Max Baxter", { "type":"hourly", "hourly_rate": 92.50, "number_of_hours": 122 })
max.send_payment(make_strategy(max.payment_details['type']))