#'test_arthimetic_operations.py'
import pytest
from Basic_operation import ArthimeticClass

class TestArithmeticClass:
    def test_add(self ):
        # arrange
        x = 8.0
        y = 0
        expected_output = 11.0
        # act
        actual_output = ArthimeticClass.add(x, y)
        # assert
        with pytest.raises(TypeError):
            ArthimeticClass.add("8", 3)
        with pytest.raises(TypeError):
            ArthimeticClass.add(8, "3")
        with pytest.raises(TypeError):
            ArthimeticClass.add("8", "3")
        assert expected_output == actual_output


    def test_substract(self ):
        # arrange
        x = 8.0
        y = 3.0
        expected_output = 5.0
        # act
        actual_output = ArthimeticClass.substract(x, y)
        # assert
        with pytest.raises(TypeError):
            ArthimeticClass.substract("8", 3)
        with pytest.raises(TypeError):
            ArthimeticClass.substract(8, "3")
        with pytest.raises(TypeError):
            ArthimeticClass.substract("8", "3")
        assert expected_output == actual_output
    
    def test_multiply(self ):
        # arrange
        x = "8.0"
        y = 0
        expected_output = 24.0
        # act
        actual_output = ArthimeticClass.multiply(x, y)
        # assert
        with pytest.raises(TypeError):
            ArthimeticClass.multiply("8", 3)
        with pytest.raises(TypeError):
            ArthimeticClass.multiply(8, "3")
        with pytest.raises(TypeError):
            ArthimeticClass.multiply("8", "3")
        assert expected_output == actual_output
    
    def test_divide(self ):
        # arrange
        x = 8.0
        y = 3.0
        expected_output = 2.666667
        # act
        actual_output = ArthimeticClass.divide(x, y)
        # assert
        with pytest.raises(TypeError):
            ArthimeticClass.divide("8", 3)
        with pytest.raises(TypeError):
            ArthimeticClass.divide(8, "3")
        with pytest.raises(TypeError):
            ArthimeticClass.divide("8", "3")
        with pytest.raises(ZeroDivisionError):
            ArthimeticClass.divide(8, 0)
        assert expected_output == actual_output
