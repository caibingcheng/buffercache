import unittest


class TestAPP(unittest.TestCase):
    def setUp(self):
        self.data = ((1, 2, 3), None, "", "123", (), [], {})

    def test_import_version(self):
        import datacache
        self.assertIsNotNone(datacache.__version__)

    def test_import_datacache(self):
        import datacache
        from datacache import DataCache
        self.assertIsNotNone(datacache)
        self.assertIsNotNone(DataCache)

    def test_set_data(self):
        from datacache import DataCache as DC
        set_data = self.data
        for data in set_data:
            dc = DC().set(data)
            self.assertEqual(dc.get(), data)
            self.assertEqual(dc.data, data)
            self.assertEqual(dc.get_getter(), None)
            self.assertEqual(dc.getter, None)

    def test_set_data_byone(self):
        from datacache import DataCache as DC
        set_data = self.data
        dc = DC()
        for data in set_data:
            dc.set(data)
            self.assertEqual(dc.get(), data)
            self.assertEqual(dc.data, data)
            self.assertEqual(dc.get_getter(), None)
            self.assertEqual(dc.getter, None)


    def test_set_data_bygetter(self):
        def get(data):
            return data
        from datacache import DataCache as DC
        set_data = self.data
        dc = DC().set_getter(get)
        for data in set_data:
            dc.update(data)
            self.assertEqual(dc.get(), get(data))
            self.assertEqual(dc.data, get(data))
            self.assertEqual(dc.get_getter(), get)
            self.assertEqual(dc.getter, get)

    def test_set_data_bygetter_withmoreargs(self):
        def get(data, args):
            return data, args
        from datacache import DataCache as DC
        set_data = self.data
        dc = DC().set_getter(get)
        for data in set_data:
            dc.update(data, {'key': data})
            self.assertEqual(dc.get(), get(data, {'key': data}))
            self.assertEqual(dc.data, get(data, {'key': data}))
            self.assertEqual(dc.get_getter(), get)
            self.assertEqual(dc.getter, get)

    def test_set_data_bygetter_withtimeout(self):
        def get(data, args):
            return data, args
        from datacache import DataCache as DC
        import time
        set_data = self.data
        timeout = 500
        dc = DC(timeout=timeout).set_getter(get)
        for data in set_data:
            dc.update(data, {'key': data})
            self.assertEqual(dc.get(), get(data, {'key': data}))
            self.assertEqual(dc.data, get(data, {'key': data}))
            self.assertEqual(dc.get_getter(), get)
            self.assertEqual(dc.getter, get)
            time.sleep((timeout + 5) / 1000)

    def test_set_data_bygetter_withtimeoutfast(self):
        def get(data, args):
            return data, args
        from datacache import DataCache as DC
        set_data = self.data
        timeout = 5000
        dc = DC(timeout=timeout).set_getter(get)
        for data in set_data:
            dc.update(data, {'key': data})
            self.assertEqual(dc.get(), get(set_data[0], {'key': set_data[0]}))
            self.assertEqual(dc.data, get(set_data[0], {'key': set_data[0]}))
            self.assertEqual(dc.get_getter(), get)
            self.assertEqual(dc.getter, get)

    def test_sample_readme(self):
        from datacache import DataCache as DC

        set_data = ((1, 2, 3), None, "", "123", (), [], {})

        def get(data, args):
            return data, args

        dc = DC(timeout=0).set_getter(get)
        for data in set_data:
            dc.update(data, {'key': data})
            # print(dc.get())
            self.assertEqual(dc.get(), get(data, {'key': data}))
            self.assertEqual(dc.data, get(data, {'key': data}))
            self.assertEqual(dc.get_getter(), get)
            self.assertEqual(dc.getter, get)
