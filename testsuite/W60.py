#: W601
if a.has_key("b"):
    print a
#: W602
raise DummyError, "Message"
#: W602
raise ValueError, "hello %s %s" % (1, 2)
#: Okay
raise type_, val, tb
#: W603
if x <> 0:
    x = 0
#: W604
val = `1 + 2`
#: W605
try:
    pass
except KeyError, exc:
    pass
