from enum import Enum


class Neighbourhood(Enum):
    NEUMANN = 0
    NEUMANN_INCLUDE_SELF = 1
    MOORE = 2
    MOORE_INCLUDE_SELF = 3
    MANHATTAN2 = 4
    MANHATTAN2_INCLUDE_SELF = 5


neighbourhood_to_deltas = {
    Neighbourhood.NEUMANN: [(-1, 0), (1, 0), (0, -1), (0, 1)],
    Neighbourhood.MOORE: [(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1] if x != 0 or y != 0],
    Neighbourhood.MANHATTAN2: [(x, y) for x in range(-2, 3) for y in range(-2, 3) if 0 < abs(x) + abs(y) < 3]
}

neighbourhood_to_deltas[Neighbourhood.NEUMANN_INCLUDE_SELF] = \
    neighbourhood_to_deltas[Neighbourhood.NEUMANN].copy()
neighbourhood_to_deltas[Neighbourhood.NEUMANN_INCLUDE_SELF].append((0, 0))

neighbourhood_to_deltas[Neighbourhood.MOORE_INCLUDE_SELF] = \
    neighbourhood_to_deltas[Neighbourhood.MOORE].copy()
neighbourhood_to_deltas[Neighbourhood.MOORE].append((0, 0))

neighbourhood_to_deltas[Neighbourhood.MANHATTAN2_INCLUDE_SELF] = \
    neighbourhood_to_deltas[Neighbourhood.MANHATTAN2].copy()
neighbourhood_to_deltas[Neighbourhood.MANHATTAN2].append((0, 0))
