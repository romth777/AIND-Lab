# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first
    [2nd Edition: p 75, 3rd Edition: p 87]

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm
    [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    def is_goal(x):
        return problem.isGoalState(x)

    init_state = problem.getStartState()

    stack = util.Stack()
    stack.push((init_state, []))
    visited = set()

    while not stack.isEmpty():
        (node, path) = stack.pop()
        if is_goal(node):  # <-- move to here
            return path
        visited.add(node)

        successors = problem.getSuccessors(node)
        for state, action, cost in successors:
            if state not in visited:
                stack.push((state, path + [action]))


def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    [2nd Edition: p 73, 3rd Edition: p 82]
    """
    "*** YOUR CODE HERE ***"
    def is_goal(x):
        return problem.isGoalState(x)

    init_state = problem.getStartState()

    queue = util.Queue()
    queue.push((init_state, []))
    visited = set()

    while not queue.isEmpty():
        (node, path) = queue.pop()
        successors = problem.getSuccessors(node)
        for state, action, cost in successors:
            if is_goal(node):  # <-- move to here
                return path
            visited.add(node)
            if state not in visited:
                queue.push((state, path + [action]))

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    def is_goal(x):
        return problem.isGoalState(x)

    init_state = problem.getStartState()

    priority_queue = util.PriorityQueue()
    priority_queue.push((init_state, []), 0)
    visited = set()

    while not priority_queue.isEmpty():
        priority, (node, path) = priority_queue.pop()
        successors = problem.getSuccessors(node)
        for state, action, cost in successors:
            new_cost = priority + cost
            if is_goal(node):  # <-- move to here
                return path
            visited.add(node)
            if state not in visited:
                priority_queue.push((state, path + [action]), new_cost)
            elif new_cost < priority:
                new_priority, (new_node, new_path) = priority_queue.pop()
                priority_queue.push((state, path + [action]), new_cost)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    def is_goal(x):
        return problem.isGoalState(x)

    init_state = problem.getStartState()

    open_list = util.PriorityQueue()
    open_list.push((init_state, []), 0)
    visited = set()

    while not open_list.isEmpty():
        priority, (node, path) = open_list.pop()
        if is_goal(node):  # <-- move to here
            return path
        successors = problem.getSuccessors(node)
        for state, action, cost in successors:
            new_score = priority + cost + heuristic(state, problem)
            visited.add(node)
            if state not in visited:
                open_list.push((state, path + [action]), new_score)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
