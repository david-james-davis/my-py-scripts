import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from unittest.mock import patch, MagicMock
from scripts.ADSBexchange import main

class TestADSBexchange(unittest.TestCase):
    @patch('requests.get')
    @patch('socket.socket')
    @patch('time.sleep')
    def test_main_function(self, mock_sleep, mock_socket, mock_get):
        # Mock the API response
        mock_get.return_value.text = '{"data": "test"}'
        mock_get.return_value.raise_for_status = MagicMock()

        # Mock the socket connection
        mock_socket_instance = MagicMock()
        mock_socket.return_value.__enter__.return_value = mock_socket_instance

        # Make time.sleep raise an exception to break the loop
        mock_sleep.side_effect = KeyboardInterrupt

        # Call the main function
        try:
            main()
        except KeyboardInterrupt:
            pass

        # Assert that the API was called
        mock_get.assert_called_once()

        # Assert that the socket was used to send data
        mock_socket_instance.sendall.assert_called_once()

if __name__ == '__main__':
    unittest.main() 