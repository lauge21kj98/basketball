from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class BasketballCourtConfiguration:
    width: int = 1524   # [cm]
    length: int = 2865  # [cm]

    center_circle_radius: int = 183
    key_width: int = 488
    free_throw_distance: int = 579
    backboard_distance: int = 122
    rim_distance: int = 157
    three_point_radius: int = 724
    corner_three_distance: int = 670

    @property
    def vertices(self) -> List[Tuple[int, int]]:
        w = self.width
        l = self.length
        kw = self.key_width

        return [
            # Court outline
            (0, 0),                # 1
            (0, w),                # 2
            (l, w),                # 3
            (l, 0),                # 4

            # Center line
            (l / 2, 0),            # 5
            (l / 2, w),            # 6

            # Center circle (top / bottom)
            (l / 2, w / 2 - self.center_circle_radius),  # 7
            (l / 2, w / 2 + self.center_circle_radius),  # 8

            # Left key (paint)
            (0, (w - kw) / 2),                     # 9
            (0, (w + kw) / 2),                     # 10
            (self.free_throw_distance, (w - kw) / 2),  # 11
            (self.free_throw_distance, (w + kw) / 2),  # 12

            # Right key
            (l, (w - kw) / 2),                     # 13
            (l, (w + kw) / 2),                     # 14
            (l - self.free_throw_distance, (w - kw) / 2),  # 15
            (l - self.free_throw_distance, (w + kw) / 2),  # 16

            # Rims
            (self.rim_distance, w / 2),            # 17
            (l - self.rim_distance, w / 2),        # 18
        ]

    edges: List[Tuple[int, int]] = field(default_factory=lambda: [
        # Court outline
        (1, 2), (2, 3), (3, 4), (4, 1),

        # Center line
        (5, 6),

        # Center circle markers
        (7, 8),

        # Left key
        (9, 10), (9, 11), (10, 12), (11, 12),

        # Right key
        (13, 14), (13, 15), (14, 16), (15, 16),
    ])

    labels: List[str] = field(default_factory=lambda: [
        "L_BL", "L_TL", "R_TR", "R_BR",
        "CENTER_B", "CENTER_T",
        "CIRCLE_TOP", "CIRCLE_BOTTOM",
        "L_KEY_BL", "L_KEY_TL", "L_KEY_BR", "L_KEY_TR",
        "R_KEY_TR", "R_KEY_BR", "R_KEY_TL", "R_KEY_BL",
        "L_RIM", "R_RIM"
    ])

    colors: List[str] = field(default_factory=lambda: [
        "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF",
        "#00BFFF", "#00BFFF",
        "#FFD700", "#FFD700",
        "#FF6347", "#FF6347", "#FF6347", "#FF6347",
        "#32CD32", "#32CD32", "#32CD32", "#32CD32",
        "#FF1493", "#FF1493"
    ])
