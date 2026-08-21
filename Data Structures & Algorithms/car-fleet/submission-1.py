class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def catchUp(car1, car2):
            time1 = float(target - car1[0])/car1[1]
            time2 = float(target - car2[0])/car2[1]
            print(time1, time2)
            return time1 <= time2
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        fleetStack = []
        for pos, speed in cars:
            if not fleetStack or not catchUp((pos, speed), fleetStack[-1]):
                fleetStack.append((pos, speed))
        return len(fleetStack) 
