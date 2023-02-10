# Day 9
# Updated 2023, Jarid Prince

from days.day_009.files.helpers import *


def day_009():
    title("SILENT BID")
    gavel_logo()
    title("Silent Bid")

    bids = {}

    def sequence():
        name = nli("What is your name?")
        bid = int(nli("What is your bid? Type Numbers only."))
        bids[name] = bid
        more_bidders = nli("Are there any more bidders? Type y or n")
        if more_bidders in yes_array:
            cls()
            sequence()
        else:
            highest_bid = 0
            highest_bidder = ""
            for bidder in bids:
                bid_amount = bids[bidder]
                if bid_amount > highest_bid:
                    highest_bidder = bidder
                    highest_bid = bid_amount

            nls(f"The highest bid is {highest_bid} from {highest_bidder}!")

    sequence()
