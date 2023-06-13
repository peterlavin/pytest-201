'''

@author: peter

'''
import demo, pytest

""" Tests for a particular function/method in a class
can/should be grouped in a class in your test_ file, this
is for organisation only """
class TestAdd():
    
    def test_add(self):
        assert demo.add(1,2) == 3
        
    def test_error(self):
        """ Ex of using the pytest context manager for errors """
        with pytest.raises(demo.DemoError):
            assert demo.add(99, 1) == 100
    
    """ Ex of test using a list of parameters, if one test in the middle
    fails, the remainder will run """
    @pytest.mark.parametrize(
        'a, b, expected', [
            (1, 1, 2),
            (3, 5, 8),
            (10, 15, 25),
            (4, 4, 8),
            (16, 24, 40),])
    def test_with_params(self, a, b, expected):
        assert demo.add(a, b) == expected

class TestingWithFixtures():
    def test_fixture(self, my_fixture):
        assert my_fixture == 42
        
    def test_capsys(self, capsys):
        print('hello')
        """ Tests that hello appears in the std out, both 
        asserts pass """
        out, err = capsys.readouterr()
        assert 'hello\n' == out
        assert 'hello' in out
        
    def test_monkeypatch(self, monkeypatch):
        
        def fake_add(a, b):
            return 42
        
        """ Monkeypatch add in demo to use fake_add for this test """
        monkeypatch.setattr(demo, "add", fake_add)
        assert demo.add(2, 4) == 42
            
    def test_tempdir(self, tmpdir):
        """ Create a file handle to a file in tmpdir """
        some_file = tmpdir.join('something.txt')
        """ Write something to this file that is useful for 
        your test """
        some_file.write('{"mykey": "myval"}')
        
        """ str returns the file path to some_file """
        result = demo.read_json(str(some_file))
        
        """ result will be the json in the file """
        assert result["mykey"] == "myval"
    
    """ Because captured_print is included, both fixtures are called
    before the test is run """ 
    def test_fixture_with_fixtures(self,capsys, captured_print):
        print('more')
        """ At this point, hello and more are in the capsys fixture """
        out, err = capsys.readouterr()
        assert out == 'hello\nmore\n'
        # OR...
        assert 'hello' in out
        assert 'more' in out             
        
