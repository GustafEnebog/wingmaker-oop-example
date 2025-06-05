from .panel import WingPanel

class Wing:
    def __init__(self, name, num_panels):
        self.name = name
        self.panels = [WingPanel() for _ in range(num_panels)]
        self.aspect_ratio = None

    def set_panel(self, index, **kwargs):
        for key, value in kwargs.items():
            setattr(self.panels[index], key, value)

    def compute_overall_parameters(self):
        total_span = sum(p.span or 0 for p in self.panels)
        avg_mac = sum(p.mac() or 0 for p in self.panels) / len(self.panels)
        self.aspect_ratio = total_span**2 / (avg_mac * total_span) if avg_mac else None
        print(f"[{self.name}] Span: {total_span}, MAC: {avg_mac}, AR: {self.aspect_ratio}")
