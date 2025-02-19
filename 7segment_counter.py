import tm1637
from time import sleep

# Initialize the TM1637 display
# CLK -> GPIO 5, DIO -> GPIO 6
display = tm1637.TM1637(clk=5, dio=6)

# Counter logic
def counter(max_value=9999, delay=1):
    while True:
        for i in range(max_value + 1):
            display.number(i)  # Display the current number
            sleep(delay)        
# Run the counter
counter(max_value=9999, delay=0.1)
