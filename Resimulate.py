from solution import SOLUTION
import os

print("Available saved robots:")
files = [f for f in os.listdir("data/best_robots") if f.endswith("_weights.npy")]
robots = [f.replace("_weights.npy", "") for f in files]
for i, name in enumerate(robots):
    print(f"  {i}: {name}")

choice = int(input("\nEnter number to replay: "))
chosen = robots[choice]
print(f"Replaying: {chosen}")

s = SOLUTION(0)
s.Create_World()
s.Load_Leg_Values(f"data/best_robots/{chosen}")
s.Evaluate("GUI")