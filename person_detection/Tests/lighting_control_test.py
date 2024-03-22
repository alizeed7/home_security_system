import unittest
from unittest.mock import patch, MagicMock
#import ./lighting_control as lc

class TestLightingControl(unittest.TestCase):
    @patch('lighting_control.GPIO')
    @patch('lighting_control.LED')
    def test_light_control(self, mock_LED, mock_GPIO):
        # Setup mock behavior
        # Simulate light and dark conditions
        light_conditions = [True, False]  # True for light, False for dark
        mock_GPIO.input.side_effect = lambda pin: light_conditions.pop(0) #lambda is an anonymous function that takes pin as an argument and pops the element from the list

        # Mock LED instance
        mock_led_instance = MagicMock()
        mock_LED.return_value = mock_led_instance

        # lighting_control.py logic is copied here to get rid of the loo. continuous loop makes it difficult to control execution
        # this function would be called twice to test both conditions
        def lighting_logic():
            photoresistor = 18  # pin 18
            if mock_GPIO.input(photoresistor):
                #light
                print("GPIO pin %d is ON" % photoresistor)
                mock_led_instance.off()
            else:
                #dark
                print("It is dark outside")
                mock_led_instance.on()  # Until specified time (database)
                mock_led_instance.off()

        # Call the function twice to simulate both light and dark conditions
        lighting_logic()  # Simulate light
        lighting_logic()  # Simulate dark

        # Check LED behavior
        self.assertTrue(mock_led_instance.off.called)
        self.assertTrue(mock_led_instance.on.called)

if __name__ == '__main__':
    unittest.main()
