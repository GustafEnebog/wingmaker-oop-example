from airfoils.airfoil_library import LibraryAirfoil
from planforms.wing import Wing
from planforms.panel import WingPanel
from utils.vector_graphics import draw_wing_top_view

def main():
    airfoil1 = LibraryAirfoil(name="NACA2412")
    print(airfoil1)

    wing = Wing(name="Main Wing", num_panels=2)
    wing.set_panel(0, span=3.0, root_chord=1.2, tip_chord=0.8)
    wing.set_panel(1, span=2.0, root_chord=0.8, tip_chord=0.6)

    wing.compute_overall_parameters()
    draw_wing_top_view(wing)

if __name__ == "__main__":
    main()
