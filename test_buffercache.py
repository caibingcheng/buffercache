import unittest


class TestAPP(unittest.TestCase):
    def setUp(self):
        self.data = ((1, 2, 3), None, "", "123", (), [], {})

    def tearDown(self):
        pass

    def test_import_version(self):
        import buffercache
        self.assertIsNotNone(buffercache.__version__)

    def test_import_datacache(self):
        import buffercache
        from buffercache import BufferCache
        self.assertIsNotNone(buffercache)
        self.assertIsNotNone(BufferCache)

    def test_set_data(self):
        from buffercache import BufferCache as BC
        set_data = self.data
        for data in set_data:
            bc = BC().set(data)
            self.assertEqual(bc.get(), data)
            self.assertEqual(bc.data, data)
            self.assertEqual(bc.get_getter(), None)
            self.assertEqual(bc.getter, None)
            self.assertEqual(str(bc), str(data))

    def test_set_data_byone(self):
        from buffercache import BufferCache as BC
        set_data = self.data
        bc = BC()
        for data in set_data:
            bc.set(data)
            self.assertEqual(bc.get(), data)
            self.assertEqual(bc.data, data)
            self.assertEqual(bc.get_getter(), None)
            self.assertEqual(bc.getter, None)
            self.assertEqual(str(bc), str(data))

    def test_set_data_bygetter(self):
        def get(data):
            return data
        from buffercache import BufferCache as BC
        set_data = self.data
        bc = BC().set_getter(get)
        for data in set_data:
            bc.update(data)
            self.assertEqual(bc.get(), get(data))
            self.assertEqual(bc.data, get(data))
            self.assertEqual(bc.get_getter(), get)
            self.assertEqual(bc.getter, get)
            self.assertEqual(str(bc), str(get(data)))

    def test_set_data_bygetter_withmoreargs(self):
        def get(data, args):
            return data, args
        from buffercache import BufferCache as BC
        set_data = self.data
        bc = BC().set_getter(get)
        for data in set_data:
            bc.update(data, {'key': data})
            self.assertEqual(bc.get(), get(data, {'key': data}))
            self.assertEqual(bc.data, get(data, {'key': data}))
            self.assertEqual(bc.get_getter(), get)
            self.assertEqual(bc.getter, get)
            self.assertEqual(str(bc), str(get(data, {'key': data})))

    def test_set_data_bygetter_withtimeout(self):
        def get(data, args):
            return data, args
        from buffercache import BufferCache as BC
        import time
        set_data = self.data
        timeout = 500
        bc = BC(timeout=timeout).set_getter(get)
        for data in set_data:
            bc.update(data, {'key': data})
            self.assertEqual(bc.get(), get(data, {'key': data}))
            self.assertEqual(bc.data, get(data, {'key': data}))
            self.assertEqual(bc.get_getter(), get)
            self.assertEqual(bc.getter, get)
            self.assertEqual(str(bc), str(get(data, {'key': data})))
            time.sleep((timeout + 5) / 1000)

    def test_set_data_bygetter_withtimeout_withprint(self):
        def get(data, args):
            return data, True, args, True
        from buffercache import BufferCache as BC
        import time
        set_data = self.data
        timeout = 500
        bc = BC(timeout=timeout).set_getter(get)
        for data in set_data:
            bc.update(data, {'key': data})
            self.assertEqual(bc.get(), get(data, {'key': data}))
            self.assertEqual(bc.data, get(data, {'key': data}))
            self.assertEqual(bc.get_getter(), get)
            self.assertEqual(bc.getter, get)
            self.assertEqual(str(bc), str(get(data, {'key': data})))
            time.sleep((timeout + 5) / 1000)

    def test_set_data_bygetter_withtimeoutfast(self):
        def get(data, args):
            return data, args, True
        from buffercache import BufferCache as BC
        set_data = self.data
        timeout = 5000
        bc = BC(timeout=timeout).set_getter(get)
        for data in set_data:
            bc.update(data, {'key': data})
            self.assertEqual(bc.get(), get(set_data[0], {'key': set_data[0]}))
            self.assertEqual(bc.data, get(set_data[0], {'key': set_data[0]}))
            self.assertEqual(bc.get_getter(), get)
            self.assertEqual(bc.getter, get)
            self.assertEqual(str(bc), str(
                get(set_data[0], {'key': set_data[0]})))

    def test_sample_readme(self):
        from buffercache import BufferCache as BC

        set_data = ((1, 2, 3), None, "", "123", (), [], {})

        def get(data, args):
            return data, args

        bc = BC(timeout=0).set_getter(get)
        for data in set_data:
            bc.update(data, {'key': data})
            # print(bc.get())
            self.assertEqual(bc.get(), get(data, {'key': data}))
            self.assertEqual(bc.data, get(data, {'key': data}))
            self.assertEqual(bc.get_getter(), get)
            self.assertEqual(bc.getter, get)
            self.assertEqual(str(bc), str(get(data, {'key': data})))
