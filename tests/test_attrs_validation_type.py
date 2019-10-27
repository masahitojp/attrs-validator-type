import attr
from attrs_validation_type.validations import type_of

from pytest import raises


@attr.s
class Foo:
    a = attr.ib(type=int, validator=type_of(int))


def test_validation_success():
    baz = Foo(1)
    assert baz.a == 1


def test_validation_error():
    with raises(TypeError):
        baz = Foo(True)
