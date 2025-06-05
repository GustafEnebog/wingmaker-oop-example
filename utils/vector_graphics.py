def draw_wing_top_view(wing):
    print(f"Drawing top view of wing: {wing.name}")
    for i, panel in enumerate(wing.panels):
        print(f" Panel {i+1}: span={panel.span}, root_chord={panel.root_chord}, tip_chord={panel.tip_chord}")
