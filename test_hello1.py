from hello1 import hello

def test_defaule():
    assert hello() == "hello world"
    
def test_argument(): 
    for name in ["Arslan", "John", "Doe"]:  
        assert hello(name) == f"hello {name}"