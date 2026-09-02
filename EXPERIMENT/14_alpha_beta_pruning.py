def alpha_beta(depth, node, alpha, beta, maximizing):
    if depth == 0:
        return node

    if maximizing:
        value = float("-inf")

        for i in [1, 2]:
            value = max(
                value,
                alpha_beta(depth - 1, node + i,
                            alpha, beta, False)
            )

            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value

    else:
        value = float("inf")

        for i in [1, 2]:
            value = min(
                value,
                alpha_beta(depth - 1, node + i,
                            alpha, beta, True)
            )

            beta = min(beta, value)

            if alpha >= beta:
                break

        return value


result = alpha_beta(3, 0, float("-inf"), float("inf"), True)

print("Best value using Alpha-Beta Pruning:", result)
