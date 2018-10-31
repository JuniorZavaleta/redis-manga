import unittest
import redis


class TestRedisLoad(unittest.TestCase):

    def test_labels_redis(self):
        r = redis.StrictRedis(host='localhost', port=6379, db=0)

        # Del 1 al 12
        for i in range(1, 13):
            self.assertTrue(r.exists('L{}'.format(i)))

    def test_mangas_redis(self):
        r = redis.StrictRedis(host='localhost', port=6379, db=0)

        # Del 1 al 7
        for i in range(1, 8):
            self.assertTrue(r.exists('L{}'.format(i)))


if __name__ == '__main__':
    unittest.main()