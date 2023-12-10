class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team
    
class All:
    def __init__(self):
        pass

    def test(self, player=None):
        return True

class Not:
    def __init__(self, condition):
        self.condition = condition

    def test(self, player):
        if self.condition.test(player):
            return False
        return True

class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value
    
class HasFewerThan:
    def __init__(self, value, attr):
        self.has_at_least = HasAtLeast(value, attr)

    def test(self, player):
        if self.has_at_least.test(player):
            return False
        
        return True
    
class Or:
    def __init__(self, *conditions):
        self.conditions = conditions

    def test(self, player):
        for condition in self.conditions:
            if condition.test(player):
                return True
        
        return False
    
class QueryBuilder:
    def __init__(self, query=All()):
        self.query = query

    def build(self):
        return self.query

    def playsIn(self, team):
        return QueryBuilder(And(self.query, PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self.query, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.query, HasFewerThan(value, attr)))

    def oneOf(self, *queries):
        if isinstance(self.query, All):
            return QueryBuilder(Or(*queries))
        else:
            return QueryBuilder(Or(self.query, *queries))
