import pytest
from task1.solution import strict

class TestStrictDecorator:
    def test_typeerror(self):
        @strict
        def add(x: int, y: int) -> int:
            return x + y

        with pytest.raises(TypeError):
            add(1, '2')

    def test_happy(self):
        @strict
        def multiply(x: int, y: int) -> int:
            return x * y

        assert multiply(2, 3) == 6
