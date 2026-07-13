import datetime

def parse_time(time_string):
  unit = time_string[-1]
  value = time_string[:-1]

  value = int(value)

  if value > 0:

      if unit == "s":
        output = datetime.timedelta(seconds=value)
      elif unit == "m":
        output = datetime.timedelta(minutes=value)
      elif unit == "h":
        output = datetime.timedelta(hours=value)
      elif unit == "d":
        output = datetime.timedelta(days=value)
      else:
        output = "unitErrot"
  else:
    output = "valueError"


  return output