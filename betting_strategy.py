import random
import matplotlib.pyplot as plt


def simulate_betting(initial_money, target_money, bet, win_rate, max_attempts, multiplier):
    balance = initial_money
    attempts = 0
    balance_history = []

    # while 0 < balance < target_money and attempts < max_attempts: #资金无下限
    while balance < target_money and attempts < max_attempts:
        r = random.uniform(0, 1)
        if r < win_rate:
            win = True
        else:
            win = False

        if win:
            balance += bet
            bet = initial_bet  # 如果赢了，重置初始赌注
        else:
            balance -= bet
            bet *= multiplier  # 如果输了，将赌注翻倍

        attempts += 1
        balance_history.append(balance)  # 记录每次模拟的余额历史

    return balance_history


def simulate_multiple_runs(num_simulations, initial_money, target_money, initial_bet, win_rate, max_attempts,
                           multiplier):
    results = []
    count_success = 0
    count_failure = 0
    percent = 0.0

    for _ in range(num_simulations):
        result = simulate_betting(initial_money, target_money, initial_bet, win_rate, max_attempts, multiplier)
        results.append(result)
        if result[-1] >= target_money:
            count_success += 1
        else:
            count_failure += 1

    print("在" + str(num_simulations) + "次试验中：")
    print("成功了" + str(count_success) + "次")
    print("失败了" + str(count_failure) + "次")
    print("成功率为：" + str(count_success*1.0/(count_success+count_failure)))

    return results


def plot_results(results):
    plt.figure(figsize=(12, 6))
    for result in results:
        plt.plot(range(len(result)), result)

    plt.xlabel("Attempts")
    plt.ylabel("Balance")
    plt.title("Multiple Simulations of Betting Strategy")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    num_simulations = 10000  # 模拟次数
    initial_bet = 1  # 初始赌注
    max_attempts = 10000  # 最大尝试次数
    initial_money = 100  # 启动资金
    target_money = 1000  # 目标资金
    multiplier = 2  # 赌注翻倍倍数
    win_rate = 0.5  # 胜率

    results = simulate_multiple_runs(num_simulations, initial_money, target_money, initial_bet, win_rate, max_attempts,
                                     multiplier)
    plot_results(results)
