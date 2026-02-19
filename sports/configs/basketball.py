from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class BasketballCourtConfiguration:
    width: int = 50   
    length: int = 94  
    
    key_length: int = 19
    key_width: int = 16

    three_point_distance: int = 28 # from baseline to top of the arc
    three_point_margin: int = 3 # distance from the three point line to the court outline
    three_point_line_length: int = 14 # length of the straight part of the three point line on the sides
    
    hoop_distance: int = 5.3
    

    @property
    def vertices(self) -> List[Tuple[int, int]]:
        w = self.width
        l = self.length
        kw = self.key_width
        kl = self.key_length
        tpd = self.three_point_distance
        tpm = self.three_point_margin
        hd = self.hoop_distance
        tpll = self.three_point_line_length

        return [
            # Court outline
            # Top (left to right)
            (0, 0),                # 1 left top corner of the court
            (tpd, 0),              # 2 halfway between baseline and middle top side LEFT
            (l / 2, 0),            # 3 Top middle of court
            (l - tpd, 0),          # 4 halfway between baseline and middle top side RIGHT
            (l, 0),                # 5 Right top corner of the court
            
            # Bottom (right to left)
            (l, w),                # 6 right bottom corner of the court
            (l - tpd, w),          # 7 halfway between baseline and middle bottom side RIGHT
            (l / 2, w),            # 8 Bottom middle of court
            (tpd, w),              # 9 halfway between baseline and middle bottom side LEFT
            (0, w),                # 10 left bottom corner of the court
            
            
            # Center dot
            (l / 2, w / 2),        # 11 center of the court

            # 3pt arc markers LEFT SIDE
            (0, tpm),             # 12 top corner of the arc sideline LEFT
            (tpll, tpm),          # 13 top corner of the arc away from baseline and sideline LEFT
            (tpd, w / 2),         # 14 top of the arc LEFT
            (tpll, w - tpm),      # 15 bottom corner of the arc away from baseline and sideline LEFT
            (0, w - tpm),         # 16 bottom corner of the arc sideline LEFT


            # 3pt arc markers RIGHT SIDE
            (l, tpm),             # 17 top corner of the arc sideline RIGHT
            (l - tpll, tpm),      # 18 top corner of the arc away from baseline and sideline RIGHT
            (l - tpd, w / 2),     # 19 top of the arc RIGHT
            (l - tpll, w - tpm),  # 20 bottom corner of the arc away from baseline and sideline RIGHT
            (l, w - tpm),         # 21 bottom corner of the arc sideline RIGHT

            
            # Left key (paint)
            (0, (w - kw) / 2),                     # 22 top left corner of the key
            (kl, (w - kw) / 2),                    # 23 top right corner of the key
            (kl, w / 2),                           # 24 ft line center of the key
            (kl, (w + kw) / 2),                    # 25 bottom right corner of the key
            (0, (w + kw) / 2),                     # 26 bottom left corner of the key
            
            
            # Right key (paint)
            (l, (w - kw) / 2),                         # 27 top right corner of the key
            (l - kl, (w - kw) / 2),                    # 28 top left corner of the key
            (l - kl, w / 2),                           # 29 ft line center of the key
            (l - kl, (w + kw) / 2),                    # 30 bottom left corner of the key
            (l, (w + kw) / 2),                         # 31 bottom right corner of the key
            
            
            

            # Hoops
            (hd, w / 2),                             # 32 left hoop
            (l - hd, w / 2),                         # 33 right hoop

        ]

    edges: List[Tuple[int, int]] = field(default_factory=lambda: [
        # Court outline TOP
        (1, 2), (2, 3), (3, 4), (4, 5),
        # Court outline BOTTOM
        (6, 7), (7, 8), (8, 9), (9, 10),
        # Center line
        (3, 11), (11, 8),
        
        # Left 3pt arc
        (12, 13), (13, 14), (14, 15), (15, 16),

        # Right 3pt arc
        (17, 18), (18, 19), (19, 20), (20, 21),

        # Left key
        (22, 23), (23, 24), (24, 25), (25, 26), (26, 22),

        # Right key
        (27, 28), (28, 29), (29, 30), (30, 31), (31, 27),
    ])

    labels: List[str] = field(default_factory=lambda: [
        "1", "2", "3", "4", "5",
        "6", "7", "8", "9", "10",
        "11",
        "12", "13", "14", "15", "16",
        "17", "18", "19", "20", "21",
        "22", "23", "24", "25", "26",
        "27", "28", "29", "30", "31",
        "32"
    ])

    colors: List[str] = field(default_factory=lambda: [
        "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF",
        "#00BFFF", "#00BFFF",
        "#FFD700", "#FFD700",
        "#FF6347", "#FF6347", "#FF6347", "#FF6347",
        "#32CD32", "#32CD32", "#32CD32", "#32CD32",
        "#FF1493", "#FF1493"
    ])
