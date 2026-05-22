mport numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path

def create_portrait():
    # Set up the figure and artistic dark background
    fig, ax = plt.subplots(figsize=(8, 10), facecolor='#11131a')
    ax.set_facecolor('#11131a')
    
    # 1. Background Aura Glow
    aura = plt.Circle((0.5, 0.55), 0.35, color='#e2979c', alpha=0.15, transform=ax.transAxes)
    ax.add_patch(aura)

    # Helper function to easily draw smooth filled shapes using paths
    def draw_shape(points, codes, color, alpha=1.0, zorder=1):
        path = Path(points, codes)
        patch = patches.PathPatch(path, facecolor=color, edgecolor='none', alpha=alpha, zorder=zorder)
        ax.add_patch(patch)

    # 2. Neck & Shoulders
    neck_pts = [(160, 100), (175, 230), (225, 230), (240, 100), (200, 70), (160, 100)]
    neck_codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY]
    draw_shape(neck_pts, neck_codes, '#cca08a', zorder=2)
    
    # Shadow under the chin
    shadow_pts = [(173, 210), (200, 190), (227, 210), (225, 230), (175, 230), (173, 210)]
    draw_shape(shadow_pts, neck_codes, '#b5856f', zorder=3)

    # 3. Main Face Structure
    face_pts = [
        (160, 220),  # Left jaw
        (150, 310),  # Left cheek
        (165, 390),  # Left forehead
        (200, 410),  # Top head
        (235, 390),  # Right forehead
        (250, 310),  # Right cheek
        (240, 220),  # Right jaw
        (200, 185),  # Chin
        (160, 220)   # Close
    ]
    face_codes = [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.CURVE3, Path.CURVE3, Path.CURVE3, Path.CURVE3, Path.CURVE3, Path.CLOSEPOLY]
    draw_shape(face_pts, face_codes, '#dfb39d', zorder=4)

    # 4. Cheeks Blush / Highlights
    left_blush = patches.Ellipse((175, 260), 22, 14, angle=15, color='#e59a9c', alpha=0.4, zorder=5)
    right_blush = patches.Ellipse((225, 260), 22, 14, angle=-15, color='#e59a9c', alpha=0.4, zorder=5)
    ax.add_patch(left_blush)
    ax.add_patch(right_blush)

    # 5. Eyes (Elegant Minimalist Slits)
    # Left Eye
    le_pts = [(168, 295), (180, 303), (192, 295), (180, 298), (168, 295)]
    le_codes = [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.CURVE3, Path.CLOSEPOLY]
    draw_shape(le_pts, le_codes, '#2b1d1d', zorder=6)
    # Right Eye
    re_pts = [(208, 295), (220, 303), (232, 295), (220, 298), (208, 295)]
    draw_shape(re_pts, le_codes, '#2b1d1d', zorder=6)

    # Eyebrows
    leb_pts = [(165, 308), (180, 317), (195, 310)]
    reb_pts = [(205, 310), (220, 317), (235, 308)]
    eb_codes = [Path.MOVETO, Path.CURVE3, Path.LINETO]
    ax.add_patch(patches.PathPatch(Path(leb_pts, eb_codes), facecolor='none', edgecolor='#422d25', linewidth=3, capstyle='round', zorder=6))
    ax.add_patch(patches.PathPatch(Path(reb_pts, eb_codes), facecolor='none', edgecolor='#422d25', linewidth=3, capstyle='round', zorder=6))

    # 6. Nose Bridge & Tip Line
    nose_pts = [(200, 312), (196, 260), (204, 260)]
    nose_codes = [Path.MOVETO, Path.LINETO, Path.LINETO]
    ax.add_patch(patches.PathPatch(Path(nose_pts, nose_codes), facecolor='none', edgecolor='#ca957e', linewidth=2.5, capstyle='round', zorder=6))

    # 7. Lips (Classic Crimson Bold Shapes)
    # Upper Lip
    ul_pts = [(187, 230), (195, 236), (200, 232), (205, 236), (213, 230), (200, 227), (187, 230)]
    ul_codes = [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.CURVE3, Path.CURVE3, Path.CURVE3, Path.CLOSEPOLY]
    draw_shape(ul_pts, ul_codes, '#b83b4b', zorder=6)
    # Lower Lip
    ll_pts = [(187, 228), (200, 218), (213, 228), (200, 223), (187, 228)]
    ll_codes = [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.CURVE3, Path.CLOSEPOLY]
    draw_shape(ll_pts, ll_codes, '#9e2a39', zorder=6)

    # 8. Flowing Hair (Layered Shapes for depth)
    # Back Hair Layer
    back_hair_pts = [(120, 80), (110, 320), (150, 430), (250, 430), (290, 320), (280, 80), (200, 120), (120, 80)]
    back_hair_codes = [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4, Path.CURVE4, Path.CURVE4, Path.CURVE4, Path.CLOSEPOLY]
    draw_shape(back_hair_pts, back_hair_codes, '#1d1719', zorder=1)

    # Front Left Hair Strand
    fl_hair_pts = [(200, 412), (150, 390), (140, 250), (165, 130), (150, 250), (160, 370), (200, 412)]
    fl_hair_codes = [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.CURVE3, Path.CURVE3, Path.CURVE3, Path.CLOSEPOLY]
    draw_shape(fl_hair_pts, fl_hair_codes, '#2d2225', zorder=7)

    # Front Right Flowing Waves
    fr_hair_pts = [(190, 412), (250, 400), (265, 260), (235, 120), (255, 240), (240, 360), (190, 412)]
    draw_shape(fr_hair_pts, fl_hair_codes, '#3a2b2f', zorder=7)
    
    # Extra overlay stroke for dynamic hair volume
    top_wave_pts = [(180, 412), (220, 425), (260, 380), (270, 290)]
    top_wave_codes = [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.LINETO]
    ax.add_patch(patches.PathPatch(Path(top_wave_pts, top_wave_codes), facecolor='none', edgecolor='#473539', linewidth=4, capstyle='round', zorder=8))

    # 9. Final framing setup
    ax.set_xlim(90, 310)
    ax.set_ylim(60, 450)
    ax.axis('off') # Hide axes grid lines
    
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.show()

if _name_ == '_main_':
    create_portrait()