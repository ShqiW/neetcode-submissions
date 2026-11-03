class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # time = (target - poistion) // speed
        # [i, time]  [3,3] spd1<=spd2 fleet+= 1

        zip_list = sorted(zip(position, speed), reverse = True)
        stk = []

        fleet = 1
        prev_spd = (target-zip_list[0][0])/zip_list[0][1]

        for i in range(1, len(zip_list)):
            spd = (target-zip_list[i][0])/zip_list[i][1]
            if spd > prev_spd:
                fleet += 1
                prev_spd = spd
        return fleet
