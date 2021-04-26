from unittest import TestCase, main
from date import Date


class TestDate(TestCase):
    def test_set_date(self):
        self.date = Date(1, 1, 1970)
        self.date.set_date(25, 9, 2019)
        self.assertListEqual([self.date.day, self.date.month, self.date.year],
                             [25, 9, 2019])

    def test_set_day1(self):
        self.date = Date(10, 10, 2019)
        self.date.day = 1
        self.assertEqual(self.date.day, 1)

    def test_set_day2(self):
        self.date = Date(10, 10, 2019)
        self.date.day = 31
        self.assertEqual(self.date.day, 31)

    def test_day_negative(self):
        self.date = Date(1, 1, 1970)
        with self.assertRaises(ValueError):
            self.date.day = -1

    def test_day_zero(self):
        self.date = Date(1, 1, 1970)
        with self.assertRaises(ValueError):
            self.date.day = 0

    def test_day_exceed(self):
        self.date = Date(1, 1, 1970)
        with self.assertRaises(ValueError):
            self.date.day = 32

    def test_set_month1(self):
        self.date = Date(10, 10, 2000)
        self.date.month = 1
        self.assertEqual(self.date.month, 1)

    def test_set_month2(self):
        self.date = Date(10, 10, 2000)
        self.date.month = 12
        self.assertEqual(self.date.month, 12)

    def test_month_negative(self):
        self.date = Date(1, 1, 1970)
        with self.assertRaises(ValueError):
            self.date.month = -1

    def test_month_exceed(self):
        self.date = Date(1, 1, 1970)
        with self.assertRaises(ValueError):
            self.date.month = 13

    def test_month_zero(self):
        self.date = Date(1, 1, 1970)
        with self.assertRaises(ValueError):
            self.date.month = 0

    def test_year_negative(self):
        self.date = Date(1, 1, 1970)
        with self.assertRaises(ValueError):
            self.date.year = -1

    def test_set_year_zero(self):
        self.date = Date(1, 1, 1970)
        with self.assertRaises(ValueError):
            self.date.year = 0

    def test_leap_year(self):
        self.date = Date(1, 1, 2000)
        self.assertTrue(self.date.is_leap_year())

    def test_not_leap_year(self):
        self.date = Date(1, 1, 2019)
        self.assertFalse(self.date.is_leap_year())

    def test_calc_difference1(self):
        self.date1 = Date(1, 1, 2000)
        self.date2 = Date(25, 9, 2019)
        self.assertEqual(self.date1.calc_difference(self.date2), 7207)

    def test_calc_difference2(self):
        self.date1 = Date(1, 1, 2000)
        self.date2 = Date(1, 1, 2019)
        self.assertEqual(self.date1.calc_difference(self.date2), 6940)

    def test_calc_difference3(self):
        self.date1 = Date(1, 1, 2000)
        self.date2 = Date(17, 1, 2000)
        self.assertEqual(self.date1.calc_difference(self.date2), 16)

    def test_calc_difference4(self):
        self.date1 = Date(1, 1, 2000)
        self.date2 = Date(1, 11, 2000)
        self.assertEqual(self.date1.calc_difference(self.date2), 305)

    def test_calc_difference5(self):
        self.date1 = Date(1, 1, 2000)
        self.date2 = Date(1, 1, 2000)
        self.assertEqual(self.date1.calc_difference(self.date2), 0)

    def test_calc_difference6(self):
        self.date1 = Date(1, 1, 2000)
        self.date2 = Date(31, 12, 2000)
        self.assertEqual(self.date1.calc_difference(self.date2), 365)

    def test_calc_difference7(self):
        self.date1 = Date(31, 12, 2000)
        self.date2 = Date(1, 1, 2001)
        self.assertEqual(self.date1.calc_difference(self.date2), 1)

    def test_calc_difference8(self):
        self.date1 = Date(1, 12, 2001)
        self.date2 = Date(2, 12, 2001)
        self.assertEqual(self.date1.calc_difference(self.date2), 1)

    def test_calc_difference9(self):
        self.date1 = Date(21, 11, 2001)
        self.date2 = Date(3, 12, 2001)
        self.assertEqual(self.date1.calc_difference(self.date2), 12)

    def test_lt1(self):
        self.date1 = Date(1, 1, 2000)
        self.date2 = Date(1, 1, 2000)
        self.assertFalse(self.date1 < self.date2)

    def test_lt2(self):
        self.date1 = Date(1, 1, 2000)
        self.date2 = Date(1, 1, 2001)
        self.assertTrue(self.date1 < self.date2)

    def test_lt3(self):
        self.date1 = Date(1, 1, 2000)
        self.date2 = Date(1, 5, 2000)
        self.assertTrue(self.date1 < self.date2)

    def test_lt4(self):
        self.date1 = Date(1, 1, 2000)
        self.date2 = Date(20, 1, 2000)
        self.assertTrue(self.date1 < self.date2)

    def test_lt5(self):
        self.date1 = Date(1, 1, 2000)
        self.date2 = Date(20, 6, 2006)
        self.assertTrue(self.date1 < self.date2)

    def test_gt1(self):
        self.date1 = Date(1, 1, 2000)
        self.date2 = Date(1, 1, 2000)
        self.assertFalse(self.date1 > self.date2)

    def test_gt2(self):
        self.date1 = Date(1, 1, 2000)
        self.date2 = Date(1, 1, 2001)
        self.assertTrue(self.date2 > self.date1)

    def test_gt3(self):
        self.date1 = Date(1, 1, 2000)
        self.date2 = Date(1, 5, 2000)
        self.assertTrue(self.date2 > self.date1)

    def test_gt4(self):
        self.date1 = Date(1, 1, 2000)
        self.date2 = Date(20, 1, 2000)
        self.assertTrue(self.date2 > self.date1)

    def test_gt5(self):
        self.date1 = Date(1, 1, 2000)
        self.date2 = Date(20, 6, 2006)
        self.assertTrue(self.date2 > self.date1)

    def test_eq1(self):
        self.date1 = Date(1, 1, 2000)
        self.date2 = Date(1, 1, 2000)
        self.assertTrue(self.date1 == self.date2)

    def test_eq2(self):
        self.date1 = Date(1, 1, 2000)
        self.date2 = Date(20, 6, 2000)
        self.assertFalse(self.date1 == self.date2)


if __name__ == '__main__':
    main()
