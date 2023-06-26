from logging_monitor.common import add_log


def test_add_log():
    msg = add_log("ERROR", "This is a test message")
    assert msg == "ERROR | This is a test message"
