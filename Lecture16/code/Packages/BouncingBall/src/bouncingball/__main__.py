from .bouncingball import BouncingBall

if __name__ == "__main__":
    ball = BouncingBall(1.0, (0, 10), (0, -2.0))
    for i in range(10):
        ball.update(0.01)
        print(ball.position)
