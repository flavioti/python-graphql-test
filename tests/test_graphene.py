from graphene.test import Client


def test_hey():
    client = Client()
    executed = client.execute("""{ hey }""")
    assert executed == {"data": {"hey": "hello!"}}


def tests_general(self):
    assert 1 == 1
