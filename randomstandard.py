import time
import random

from rlbot.agents.base_script import BaseScript
from rlbot.utils.game_state_util import GameState, BallState, CarState, Physics, Vector3, Rotator, GameInfoState
from rlbot.utils.structures.game_data_struct import GameTickPacket


# How high the ball is on kickoff.
kickoff_height = 100




class RandomStandard(BaseScript):
    def __init__(self):
        super().__init__("Random Standard")

    def start(self):
        while True:
         
            time.sleep(0.5)

            # when packet available
            packet = self.wait_game_tick_packet()

            if not packet.game_info.is_round_active:
                continue
                
            # Picks random mode on kickoff.
            if packet.game_info.is_kickoff_pause and round(packet.game_ball.physics.location.z) != kickoff_height:
             #random number between 0 and 4
             gameM = random.randint(1, 3)
             #Delay to make sure bots teleport
             time.sleep(0.1)
             #change height of ball
             ball_state = BallState(Physics(location=Vector3(z=kickoff_height), velocity=Vector3(0, 0, 0)))
             self.set_game_state(GameState(ball=ball_state))
             # self.set_game_state(GameState(game_info=GameInfoState(game_speed=1)))
        
            #Checks that there are 6 cars then teleports cars depending on mode
            if packet.num_cars == 6:
                 if gameM == 2:  
                     #2v2 (I just copied 1v1 code)
                     car_states = {}
                     for p in range(2,3):
                         car = packet.game_cars[p]
                         pos = Vector3((3000+p*25), 5500, 800)
                         car_state = CarState(boost_amount=0, physics=Physics(location=pos, rotation=Rotator(yaw=0, pitch=0, roll=0), velocity=Vector3(0, 0, 0), angular_velocity=Vector3(0, 0, 0)))
                         car_states[p] = car_state
                     for p in range(5,6):
                         car = packet.game_cars[p]
                         pos = Vector3(-(3000+p*25), -5500, 800)
                         car_state = CarState(boost_amount=0, physics=Physics(location=pos, rotation=Rotator(yaw=0, pitch=0, roll=0), velocity=Vector3(0, 0, 0), angular_velocity=Vector3(0, 0, 0)))
                         car_states[p] = car_state
                     self.paused_car_states = car_states
                     self.game_state = GameState(cars=car_states)
                     self.set_game_state(self.game_state)
                 if gameM == 1:  
                     #1v1
                     car_states = {}
                     for p in range(1,3):
                         car = packet.game_cars[p]
                         pos = Vector3((3000+p*25), 5500, 800)
                         car_state = CarState(boost_amount=0, physics=Physics(location=pos, rotation=Rotator(yaw=0, pitch=0, roll=0), velocity=Vector3(0, 0, 0), angular_velocity=Vector3(0, 0, 0)))
                         car_states[p] = car_state
                     for p in range(4,6):
                         car = packet.game_cars[p]
                         pos = Vector3(-(3000+p*25), -5500, 800)
                         car_state = CarState(boost_amount=0, physics=Physics(location=pos, rotation=Rotator(yaw=0, pitch=0, roll=0), velocity=Vector3(0, 0, 0), angular_velocity=Vector3(0, 0, 0)))
                         car_states[p] = car_state
                     self.paused_car_states = car_states
                     self.game_state = GameState(cars=car_states)
                     self.set_game_state(self.game_state)
   


if __name__ == "__main__":
    random_standard = RandomStandard()
    random_standard.start()
