from squba_diver import squba_diver
import inspect


def test_its_working():
    assert True == True


def test_there_is_a_class():
    assert inspect.isclass(squba_diver)


def test_sd_has_150_oxigen_litres_at_start():
    # Arrange
    current_oxigen = 150

    # Act
    squbaDiver = squba_diver()
    expected_result = squbaDiver.oxigen

    # Assert
    assert expected_result == current_oxigen


def test_diver_starts_at_0_meters_level():
    current_depth = 0

    squbaDiver = squba_diver()
    expected_level = squbaDiver.depth

    assert expected_level == current_depth


def test_must_descend_1_step_each_step():
    current_depth = -6

    squbaDiver = squba_diver(-5)
    squbaDiver.descend()
    expected_level = squbaDiver.depth


    assert expected_level == current_depth


def test_must_stay_without_change_depth():
    current_depth = -8

    squbaDiver = squba_diver(-8)
    squbaDiver.stays()
    expected_level = squbaDiver.depth


    assert expected_level == current_depth


def test_must_ascend_1_step_each_step():
    current_depth = -4

    squbaDiver = squba_diver(-5)
    squbaDiver.ascend()
    expected_level = squbaDiver.depth


    assert expected_level == current_depth


def test_must_not_ascend_over_0_and_fly():
    current_depth = 0

    squbaDiver = squba_diver()
    squbaDiver.ascend()
    expected_level = squbaDiver.depth

    assert expected_level == current_depth


def test_consumes_1_oxigen_litre_when_ascends():
    current_oxigen = 149

    squbaDiver = squba_diver()
    squbaDiver.ascend()
    expected_oxigen = squbaDiver.oxigen

    assert expected_oxigen == current_oxigen


