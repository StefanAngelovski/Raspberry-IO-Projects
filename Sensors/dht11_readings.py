import time
import adafruit_dht
import board

# Initialize the DHT11 sensor on GPIO4 (BCM numbering)
dht_sensor = adafruit_dht.DHT11(board.D14)

try:
    while True:
        try:
            # Read temperature and humidity
            temperature = dht_sensor.temperature
            humidity = dht_sensor.humidity

            # Print results
            print(f"Temperature: {temperature:.1f}°C | Humidity: {humidity:.1f}%")

        except RuntimeError as e:
            # Handle sensor read errors (common with DHT11)
            print(f"Error: {e} (retrying...)")

        # Wait 2 seconds between readings (DHT11 requires slow polling)
        time.sleep(2)

except KeyboardInterrupt:
    # Cleanup on exit
    dht_sensor.exit()
    print("Program stopped.")
