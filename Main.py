import Starting


def main():

    population = 200
    level = 6
    mutationPercentage = 10
    maxPossibilityOfReusingParent = 20

    Starting.start(population, level, mutationPercentage, maxPossibilityOfReusingParent)


if __name__ == "__main__":
    main()
