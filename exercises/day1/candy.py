"""Alice, Bob and Carol have agreed to pool their Halloween candy and 
split it evenly among themselves. For the sake of their friendship, any 
candies left over will be smashed. For example, if they collectively 
bring home 91 candies, they'll take 30 each and smash 1.
Write an arithmetic expression below to calculate how many candies 
they must smash for a given haul."""

alice_candies = 121
bob_candies = 77
carol_candies = 109

candies_to_smash = (alice_candies + bob_candies + carol_candies) % 3
print(f"Total candies to smash: {candies_to_smash}")