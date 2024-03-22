import unittest
from unittest.mock import patch, MagicMock
import person_detection as pd

class TestPersonDetection(unittest.TestCase):
    def test_ReadLabelFile(self):
        #create a temporary label file for testing
        with open('temp_label_file.txt', 'w') as f:
            f.write('0 label_0\n1 label_1')
        labels = pd.ReadLabelFile('temp_label_file.txt')
        self.assertEqual(labels, {0: 'label_0', 1: 'label_1'})
      
    #create mock object for drawing rectangle
    @patch('cv2.rectangle')
    def test_DrawRectangles(self, mock_rectangle):
        pd.rectangles = [[10, 20, 30, 40], [50, 60, 70, 80]]
        request = MagicMock()
        pd.DrawRectangles(request)
        #checks if cv2.rectangle was called exactly twice which matches the number of rectangles in the pd.rectangles list
        self.assertEqual(mock_rectangle.call_count, 2)
    
    @patch('tflite_runtime.interpreter.Interpreter')
    @patch('cv2.cvtColor')
    @patch('cv2.resize')
    def test_InferenceTensorFlow(self, mock_resize, mock_cvtColor, mock_interpreter):
        #mocking the external calls made within InferenceTensorFlow
        mock_interpreter.return_value.get_input_details.return_value = [{'shape': [1, 300, 300, 3], 'dtype': 'uint8'}]
        mock_interpreter.return_value.get_output_details.return_value = [{'index': 0}, {'index': 1}, {'index': 2}, {'index': 3}]
        mock_interpreter.return_value.allocate_tensors.return_value = None
        mock_interpreter.return_value.set_tensor.return_value = None
        mock_interpreter.return_value.invoke.return_value = None
        mock_interpreter.return_value.get_tensor.side_effect = [
            [[[10, 20, 30, 40]]], # detected_boxes
            [[1]], # detected_classes
            [[0.9]], # detected_scores
            [1] # num_boxes
        ]
        image = MagicMock()
        pd.InferenceTensorFlow(image, 'model.tflite', 'labels.txt', 'output_location')
        #assert if rectangles were populated based on mock inference output
        self.assertTrue(len(pd.rectangles) > 0)

    @patch('person_detection.capture_video')
    @patch('os.path.exists')
    @patch('person_detection.VideoFileClip')
    def test_capture_video(self, mock_VideoFileClip, mock_exists, mock_capture_video):
        # Setup mocks
        mock_exists.return_value = True #simulate the presence of the video without actually creating the directory for it
        mock_video_clip = MagicMock()
        mock_video_clip.duration = 30
        mock_VideoFileClip.return_value = mock_video_clip

        # Call the mocked capture_video function
        test_video_file = 'Tests/test.mp4'
        pd.capture_video(test_video_file)

        # Assert os.path.exists was called to check file creation
        mock_exists.assert_called_with(test_video_file)

        # Assert VideoFileClip was called to check video duration
        mock_VideoFileClip.assert_called_with(test_video_file)
        self.assertEqual(mock_video_clip.duration, 30, "Video duration does not match the expected 30 seconds.") 

if __name__ == '__main__':
    unittest.main()
