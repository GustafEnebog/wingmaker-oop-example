class WingPanel:
    def __init__(self, span=None, root_chord=None, tip_chord=None):
        self.span = span
        self.root_chord = root_chord
        self.tip_chord = tip_chord

    def mac(self):
        # Mean Aerodynamic Chord estimate
        if self.root_chord and self.tip_chord:
            return (2/3) * self.root_chord * ((1 + self.tip_chord/self.root_chord + (self.tip_chord/self.root_chord)**2) / (1 + self.tip_chord/self.root_chord))
        return None
