from typing import Dict, Type
from dataclasses import dataclass
from abc import  ABC, abstractmethod

class PaymentStrategy (ABC):

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


  def __init__(this, name:str, payment_details:Dict[str,float]):
    this.name = name
    this.payment_details = payment_details

  def send_payment(this, stategy:Type[PaymentStrategy]) -> None:
    amount = stategy(**this.payment_details).calculate_amount()

    print(f"Sending ${amount} to {this.name}")


jennifer = Employee("Jennifer Smith", { "salary": 135000 })
jennifer.send_payment(SalaryStrategy)

max = Employee("Max Baxter", { "hourly_rate": 92.50, "number_of_hours": 122 })
max.send_payment(HourlyStrategy)