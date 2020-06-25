import unittest
from score import Score

class TestScore(unittest.TestCase):

    def setUp(self):
        self.my_score1 = Score("1,강호민,85,90,95")
        self.my_score2 = Score("2,김광호,80,70,60")

    def tearDown(self):
        del self.my_score1
        del self.my_score2

    def test_construcor(self):
        self.assertIsNotNone(self.my_score1)
        self.assertIsNotNone(self.my_score2)

    def test_sid_1(self):
        self.assertEqual("1", self.my_score1.sid)

    def test_sid_2(self):
        self.assertEqual("2", self.my_score2.sid)

    def test_name(self):
        self.assertEqual("강호민", self.my_score1.name)
        self.assertEqual("김광호", self.my_score2.name)

    def test_kor(self):
        self.assertEqual(85, self.my_score1.kor)
        self.assertEqual(80, self.my_score2.kor)

    def test_eng(self):
        self.assertEqual(90, self.my_score1.eng)
        self.assertEqual(70, self.my_score2.eng)

    def test_mat(self):
        self.assertEqual(95, self.my_score1.mat)
        self.assertEqual(60, self.my_score2.mat)

    def test_total(self):
        self.assertEqual(270, self.my_score1.total)
        self.assertEqual(210, self.my_score2.total)

    def test_avg(self):
        self.assertEqual(90, self.my_score1.avg)
        self.assertEqual(70, self.my_score2.avg)


if __name__ == "__main__":
    unittest.main()