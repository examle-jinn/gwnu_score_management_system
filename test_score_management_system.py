import unittest
from score_management_system import ScoreManagementSystem
from unittest.mock import Mock
from unittest.mock import patch
from unittest.mock import mock_open

class TestScoreManagementSystem(unittest.TestCase):

    def setUp(self):
        self.m_open_1 = mock_open(read_data="1,강호민,85,90,95\n")
        self.m_open_2 = mock_open(read_data="1,강호민,85,90,95\n2,김광호,80,70,60\n")

        self.m_write_open_1 = mock_open()
        self.m_w = mock_open().return_value
        self.m_write_open_1.side_effect = [self.m_open_2.return_value, self.m_w]

    def test_constructor(self):
        sms = ScoreManagementSystem()
        self.assertIsNotNone(sms)

    def test_read_1(self):
        with patch('score_management_system.open', self.m_open_1):
            sms = ScoreManagementSystem()
            self.assertEqual(1, sms.read('score.csv'))

        self.m_open_1.assert_called_with('score.csv', 'rt', encoding="utf-8")

    def test_read_2(self):
        with patch('score_management_system.open', self.m_open_2):
            sms = ScoreManagementSystem()
            self.assertEqual(2, sms.read('score.csv'))

    def test_sort_1(self):
        with patch('score_management_system.open', self.m_open_1):
            sms = ScoreManagementSystem()
            sms.read('score.csv')

            #result = sms.sort_by_reg(order="asc")
            result = sms.sort(order_key="register", order_way="asc")
            self.assertEqual('1,강호민,85,90,95,270,90.0', result)

    def test_sort_2(self):
        with patch('score_management_system.open', self.m_open_2):
            sms = ScoreManagementSystem()
            sms.read('score.csv')

            result = sms.sort(order_key="register", order_way="asc")
            self.assertEqual('1,강호민,85,90,95,270,90.0\n2,김광호,80,70,60,210,70.0', result)

    def test_sort_3(self):
        with patch('score_management_system.open', self.m_open_2):
            sms = ScoreManagementSystem()
            sms.read('score.csv')

            result = sms.sort(order_key="register", order_way="des")
            self.assertEqual('2,김광호,80,70,60,210,70.0\n1,강호민,85,90,95,270,90.0', result)

    def test_sort_4(self):
        with patch('score_management_system.open', self.m_open_2):
            sms = ScoreManagementSystem()
            sms.read('score.csv')

            result = sms.sort("avg", "asc")
            self.assertEqual('2,김광호,80,70,60,210,70.0\n1,강호민,85,90,95,270,90.0', result)

    def test_sort_5(self):
        with patch('score_management_system.open', self.m_open_2):
            sms = ScoreManagementSystem()
            sms.read('score.csv')

            result = sms.sort("avg", "des")
            self.assertEqual('1,강호민,85,90,95,270,90.0\n2,김광호,80,70,60,210,70.0', result)

    def test_sort_6(self):
        with patch('score_management_system.open', self.m_open_2):
            sms = ScoreManagementSystem()
            sms.read('score.csv')

            result = sms.sort("rank", "acs")
            self.assertEqual('2,김광호,80,70,60,210,70.0\n1,강호민,85,90,95,270,90.0', result)


    def test_write_1(self):
        with patch('score_management_system.open', self.m_write_open_1):
            sms = ScoreManagementSystem()
            sms.read('score.csv')
            sms.write('result.csv')

        self.m_w.write.assert_called_with("1,강호민,85,90,95,270,90.0\n2,김광호,80,70,60,210,70.0")

    def test_write_2(self):
        with patch('score_management_system.open', self.m_write_open_1):
            sms = ScoreManagementSystem()
            sms.read('score.csv')
            sms.write('result.csv', 'register', 'des')

        self.m_w.write.assert_called_with("2,김광호,80,70,60,210,70.0\n1,강호민,85,90,95,270,90.0")

    def test_write_3(self):
        with patch('score_management_system.open', self.m_write_open_1):
            sms = ScoreManagementSystem()
            sms.read('score.csv')
            sms.write('result.csv', 'avg', 'asc')

        self.m_w.write.assert_called_with("2,김광호,80,70,60,210,70.0\n1,강호민,85,90,95,270,90.0")

    def test_write_4(self):
        with patch('score_management_system.open', self.m_write_open_1):
            sms = ScoreManagementSystem()
            sms.read('score.csv')
            sms.write('result.csv', 'avg', 'des')

        self.m_w.write.assert_called_with("1,강호민,85,90,95,270,90.0\n2,김광호,80,70,60,210,70.0")




if __name__ == "__main__":
    unittest.main()