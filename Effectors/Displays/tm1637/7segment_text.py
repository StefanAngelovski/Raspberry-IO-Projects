import tm1637
from time import sleep

# Initialize the TM1637 display
# CLK -> GPIO 5, DIO -> GPIO 6
display = tm1637.TM1637(clk=5, dio=6)

# Example text to display
text_to_display = ["HELLO", "COOL", "1234", "BYE", "Pi"]


for text in text_to_display:
    display.show("    ")
    display.show(text)  # Display the text
    sleep(2)           # Wait 2 seconds before displaying the next text

