# Copyright (c) 2023 Jarid Prince

from days.day_001.main import day_001

from days.day_002.main import day_002
from days.day_003.main import day_003
from days.day_004.main import day_004
from days.day_005.main import day_005
from days.day_006.main import day_006
from days.day_007.main import day_007
from days.day_008.main import day_008
from days.day_009.main import day_009
from days.day_010.main import day_010
from days.day_011.main import day_011
from days.day_012.main import day_012
from days.day_013.main import day_013
from days.day_014.main import day_014
from days.day_015.main import day_015
from days.day_016.main import day_016
from days.day_017.main import day_017
from days.day_018.main import day_018
from days.day_019.main import day_019
from days.day_020.main import day_020
from days.day_021.main import day_021
from days.day_022.main import day_022
from days.day_023.main import day_023
from days.day_024.main import day_024
from days.day_025.main import day_025
from days.day_026.main import day_026
from days.day_027.main import day_027
from days.day_028.main import day_028
from days.day_029.main import day_029
from days.day_030.main import day_030
from days.day_031.main import day_031
from days.day_032.main import day_032
from days.day_033.main import day_033
from days.day_034.main import day_034
from days.day_035.main import day_035
from days.day_036.main import day_036
from days.day_037.main import day_037
from days.day_038.main import day_038
from days.day_039.main import day_039
from days.day_040.main import day_040
from days.day_041.main import day_041
from days.day_042.main import day_042
from days.day_043.main import day_043
from days.day_044.main import day_044
from days.day_045.main import day_045
from days.day_046.main import day_046
from days.day_047.main import day_047
from days.day_048.main import day_048
from days.day_049.main import day_049
from days.day_050.main import day_050

from days.day_051.main import day_051
from days.day_052.main import day_052
from days.day_053.main import day_053
from days.day_054.main import day_054
from days.day_055.main import day_055
from days.day_056.main import day_056
from days.day_057.main import day_057
from days.day_058.main import day_058
from days.day_059.main import day_059
from days.day_060.main import day_060
from days.day_061.main import day_061
from days.day_062.main import day_062
from days.day_063.main import day_063
from days.day_064.main import day_064
from days.day_065.main import day_065
from days.day_066.main import day_066
from days.day_067.main import day_067
from days.day_068.main import day_068
from days.day_069.main import day_069
from days.day_070.main import day_070
from days.day_071.main import day_071
from days.day_072.main import day_072
from days.day_073.main import day_073
from days.day_074.main import day_074
from days.day_075.main import day_075
from days.day_076.main import day_076
from days.day_077.main import day_077
from days.day_078.main import day_078
from days.day_079.main import day_079
from days.day_080.main import day_080
from days.day_081.main import day_081
from days.day_082.main import day_082
from days.day_083.main import day_083
from days.day_084.main import day_084
from days.day_085.main import day_085
from days.day_086.main import day_086
from days.day_087.main import day_087
from days.day_088.main import day_088
from days.day_089.main import day_089
from days.day_090.main import day_090
from days.day_091.main import day_091
from days.day_092.main import day_092
from days.day_093.main import day_093
from days.day_094.main import day_094
from days.day_095.main import day_095
from days.day_096.main import day_096
from days.day_097.main import day_097
from days.day_098.main import day_098
from days.day_099.main import day_099
from days.day_100.main import day_100
import os, sys, traceback, re


class ProgramLauncher:
    def __init__(self, misc):
        self.misc = misc
        self.DAYS = [
            day_001,
            day_002,
            day_003,
            day_004,
            day_005,
            day_006,
            day_007,
            day_008,
            day_009,
            day_010,
            day_011,
            day_012,
            day_013,
            day_014,
            day_015,
            day_016,
            day_017,
            day_018,
            day_019,
            day_020,
            day_021,
            day_022,
            day_023,
            day_024,
            day_025,
            day_026,
            day_027,
            day_028,
            day_029,
            day_030,
            day_031,
            day_032,
            day_033,
            day_034,
            day_035,
            day_036,
            day_037,
            day_038,
            day_039,
            day_040,
            day_041,
            day_042,
            day_043,
            day_044,
            day_045,
            day_046,
            day_047,
            day_048,
            day_049,
            day_050,
        ]
        #   , day_051, day_052, day_053, day_054, day_055, day_056, day_057, day_058, day_059, day_060, day_061, day_062, day_063, day_064, day_065, day_066, day_067, day_068, day_069, day_070, day_071, day_072, day_073, day_074, day_075, day_076, day_077, day_078, day_079, day_080, day_081, day_082, day_083, day_084, day_085, day_086, day_087, day_088, day_089, day_090, day_091, day_092, day_093, day_094, day_095, day_096, day_097, day_098, day_099, day_100
        self.program_id = None
        self.selected = None

    # , day21, day22, day23, day24, day25, day26, day27, day28, day29, day30, day31, day32, day33, day34, day35, day36, day37, day38, day39, day40, day41, day42, day43, day44, day45, day46, day47, day48, day49, day50, day51, day52, day53, day54, day55, day56, day57, day58, day59, day60, day61, day62, day63, day64, day65, day66, day67, day68, day69, day70, day71, day72, day73, day74, day75, day76, day77, day78, day79, day80, day81, day82, day83, day84, day85, day86, day87, day88, day89, day90, day91, day92, day93, day94, day95, day96, day97, day98, day99, day100
    def set_program(self, program):
        self.program_id = int(program)
        self.selected = f"day{str(program)}"

    def launch(self):
        print(f"SELECTED: {self.selected}")
        print(f"ID: {str(self.program_id)}")
        try:
            print(f"{self.DAYS[self.program_id - 1]}")
            self.DAYS[self.program_id - 1]()
        except KeyboardInterrupt:
            self.misc.nls("Exiting...")
            sys.exit()
        except Exception as e:
            # self.misc.cls()
            self.misc.nls(f"{'*'*20} ERR! {'*'*20}\n")

            dir_path = os.path.dirname(os.path.realpath(__file__))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            # excdata = (traceback.extract_tb(exc_tb))
            # excdata = (traceback.print_stack())

            tbLines = traceback.format_exception(*sys.exc_info())
            f = "\n"
            # print(tbLines)
            for l in tbLines[:-1]:
                if l == "Traceback (most recent call last):\n":
                    #  or l == '  File "D:\\dev\\py100\\tools\\ProgramLauncher.py", line 122, in launch\n    self.DAYS[self.program_id - 1]()\n'
                    pass
                else:
                    l = str(l)
                    l.lstrip().rstrip().replace("\n", "#\n").replace(" ", "")
                    # print(l)

                    f += l
            f.lstrip().rstrip().replace("\n", "giggity")
            raw = re.sub(r"File \"D:\\dev\\py100\\tools\\days\\day_0\d+", "", f)
            raw = re.sub(r"\\main.py\", ", "", raw)
            raw = re.sub(r", in day_0\d+", " in main", raw)
            raw = re.sub(r"\\files\\", "", raw)
            raw = re.sub(r".py\",", " @", raw)

            print(
                f"{self.misc.bcolors.FAIL}FROM DIRECTORY:\t\t {dir_path}\{fname}@{exc_tb.tb_lineno}{self.misc.bcolors.ENDC}\n"
            )
            print(f"{self.misc.bcolors.FAIL}INFO:\n{raw}{self.misc.bcolors.ENDC}\n")
            print(
                f"{self.misc.bcolors.HEADER}{exc_type.__name__.upper()}:\t\t {exc_obj}{self.misc.bcolors.ENDC}\n"
            )
