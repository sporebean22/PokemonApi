from enum import Enum

class Mpxn:
  def __init__(this, mpxn)
    this.mpxn = Mpxn
    commodity = Commodity(Mpxn)
​
class Commodity:
  def __init__(this, mpxn):
    this.mpxn = Mpxn
    commodity = findCommodity()

  Commodity = Enum('Gas', 'Electricity')

  def findCommodity(this):
    if 6 < len(this.Mpxn) < 10:
      commodity = Commodity.Gas
    elif 10 < len(this.Mpxn) < 13:
      commodity = Commodity.Electricity
