# problem taken from here: https://youtu.be/r4-cftqTcdI?si=4IWhbFx5hnl6fouf&t=2296


def bowling(pins):
    # dp[i] is the max score possible starting with pins i,i+1,...n-1
    # dp[i] = max( dp[i+1], pin[i] + dp[i+1], pin[i]*pin[i+1] + dp[i+2] )
    num_pins = len(pins)
    dp = [float("-inf")] * (num_pins + 1)

    # bottom up
    # when you start, this is the current score wherein there are no any pins
    dp[-1] = 0

    for i in range(num_pins - 1, -1, -1):
        dp[i] = max(
            dp[i + 1],
            pins[i] + dp[i + 1],
            (pins[i] * pins[i + 1] if i < num_pins - 1 else 0)
            + (dp[i + 2] if i < len(dp) - 2 else 0),
        )

    print(dp[0])


if __name__ == "__main__":
    """
    Problem: maximise the score by hitting a pin. Not neccesary to knock down all the pins
    You can hit a pin in three ways:
        1. Hit a single pin, add its pin[i] to the final score OR
        2. Hit two pins at a time(by bowing right at the middle of them), add their PRODUCT
            (pin[i] * pin[i+1]) to the final score.
        3. Don't hit a pin if hitting it decreases your current score.
    Return minimum number of throws which maximises the score?
    """
    pins = [1, 1, 9, 9, 2, -5, -5]
    bowling(pins)
