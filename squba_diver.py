class squba_diver:
    STEP = 1
    AT_SURFACE = 0

    def __init__(self, deep=0):
        initial_oxigen_litres = 150
        self.oxigen = initial_oxigen_litres
        self.depth = deep

    def descend(self):
        self.depth -= self.STEP

    def ascend(self):
        self._emerge_step()
        self._consume_oxigen()

    def stays(self):
        pass

    def _is_at_surface(self):
        return self.depth >= self.AT_SURFACE

    def _emerge_step(self):
        if self._is_at_surface():
            self.depth = self.AT_SURFACE
        else:
            self.depth += self.STEP

    def _consume_oxigen(self, step=1):
        self.oxigen -= step


