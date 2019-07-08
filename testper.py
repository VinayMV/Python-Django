from per import percentage
def test_percentage():
    perc=percentage(100.0,10.0)
    assert perc==10
    a='b'
    b='b'
    perc=percentage(a,b)
    assert perc == "Invalid arguments"
