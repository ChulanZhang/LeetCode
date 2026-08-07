class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left represents the day on which we currently plan to buy.
        # It always points to the lowest stock price seen before or at `right`.
        left = 0

        # right represents the day on which we are considering selling.
        # Starting at index 1 guarantees that the selling day is after
        # the buying day.
        right = 1

        # The maximum profit found so far.
        # It starts at 0 because we can choose not to make a transaction
        # when all prices are decreasing.
        max_profit = 0

        # Move the selling pointer through every possible selling day.
        while right < len(prices):

            # If today's price is lower than our current buying price,
            # today is a better day to buy.
            #
            # For any future selling price:
            #
            # future_price - prices[right]
            #
            # will be greater than:
            #
            # future_price - prices[left]
            #
            # because prices[right] < prices[left].
            #
            # Therefore, the old buying day can never produce a better
            # future profit, so we safely replace it with `right`.
            if prices[right] < prices[left]:
                left = right

            else:
                # Compare the profit from selling today with the best
                # profit found from all previously examined selling days.
                max_profit = max(max_profit, prices[right] - prices[left])

            # Move to the next possible selling day.
            right += 1

        return max_profit
        