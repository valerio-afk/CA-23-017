from typing import Dict

class Employee:


  def __init__(this, name:str, payment_details:Dict[str,float]):
    this.name = name
    this.payment_details = payment_details

  def send_payment(this) -> None:
    if "salary" in this.payment_details:
        amount = (this.payment_details["salary"] / 12)
    else:
      hourly_rate = this.payment_details["hourly_rate"]
      number_of_hours = this.payment_details["number_of_hours"]
      amount = (hourly_rate * number_of_hours)

    print(f"Sending ${amount} to {this.name}")


jennifer = Employee("Jennifer Smith", { "salary": 135000 })
jennifer.send_payment()

max = Employee("Max Baxter", { "hourly_rate": 92.50, "number_of_hours": 122 })
max.send_payment()