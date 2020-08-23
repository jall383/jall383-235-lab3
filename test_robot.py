import pytest

from robot import Robot, Direction, IllegalMoveException


@pytest.fixture
def robot():
    return Robot()


def test_constructor(robot):
    state = robot.state()

    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1


# TURN TESTING
def test_east_turn(robot):
    robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.EAST


def test_south_turn(robot):
    robot.turn()
    robot.turn()
    state = robot.state()
    assert state['direction'] == Direction.SOUTH


def test_west_turn(robot):
    robot.turn()
    robot.turn()
    robot.turn()
    state = robot.state()
    assert state['direction'] == Direction.WEST


def test_full_turn(robot):
    robot.turn()
    robot.turn()
    robot.turn()
    robot.turn()
    state = robot.state()
    assert state['direction'] == Direction.NORTH


# END OF TURN TESTING


# MOVE TESTING
# Illegal moves
def test_illegal_move_south(robot):
    robot.turn()
    robot.turn()

    with pytest.raises(IllegalMoveException):
        robot.move()


def test_illegal_move_west(robot):
    robot.turn()
    robot.turn()
    robot.turn()
    with pytest.raises(IllegalMoveException):
        robot.move()


def test_illegal_move_north(robot):
    robot._state.row = 1
    with pytest.raises(IllegalMoveException):
        robot.move()


def test_illegal_move_east(robot):
    robot.turn()
    robot._state.col = 10
    with pytest.raises(IllegalMoveException):
        robot.move()


# Legal moves
def test_move_north(robot):
    robot.move()
    state = robot.state()
    assert state['row'] == 9
    assert state['col'] == 1


def test_move_east(robot):
    robot.turn()
    robot.move()
    state = robot.state()
    assert state['row'] == 10
    assert state['col'] == 2


def test_move_south(robot):
    robot._state.row = 1
    robot.turn()
    robot.turn()
    robot.move()
    state = robot.state()
    assert state['row'] == 2
    assert state['col'] == 1


def test_move_west(robot):
    robot._state.col = 10
    robot.turn()
    robot.turn()
    robot.turn()
    robot.move()
    state = robot.state()
    assert state['row'] == 10
    assert state['col'] == 9


# END OF MOVE TESTING


# BACKTRACK TEST CASES
def test_back_track_without_history(robot):
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1

def test_back_track_after_move(robot):
    robot.move()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 9
    assert state['col'] == 1

def test_back_track_after_turn(robot):
    robot.turn()
    state = robot.state()
    assert state['direction'] == Direction.EAST
    assert state['row'] == 10
    assert state['col'] == 1

def test_back_track_after_many_turns_and_moves(robot):
    robot.move()
    robot.turn()
    robot.move()
    robot.move()
    robot.turn()
    state = robot.state()
    assert state['direction'] == Direction.SOUTH
    assert state['row'] == 9
    assert state['col'] == 3

# END OF BACKTRACK TEST CASES
