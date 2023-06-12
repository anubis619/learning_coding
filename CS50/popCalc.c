// #include <cs50.h>
#include <stdio.h>

// Expected error as I have copied the code from the CS50 VSCode.

int main(void)
{
    // TODO: Prompt for start size
    int startPopulation;
    printf("Start size: ");
    scanf("%d", &startPopulation);

    while (startPopulation < 9)
    {
        // startPopulation = scanf("Start size: ");
        printf("Start size: ");
        scanf("%d", &startPopulation);
    }
    // TODO: Prompt for end size
    int endSize;
    printf("End size: ");
    scanf("%d", &endSize);

    while (endSize < startPopulation)
    {
        printf("End size: ");
        scanf("%d", &endSize);
    }
    // TODO: Calculate number of years until we reach threshold
    int bornPopulation = startPopulation / 3;
    int diedPopulation = startPopulation / 4;
    int endYear = startPopulation + bornPopulation - diedPopulation;
    int yearsPassed;

    if (startPopulation == endSize)
    {
        yearsPassed = 0;
    }
    else
    {
        yearsPassed = 1;
        while (endYear < endSize)
        {
            bornPopulation = endYear / 3;
            diedPopulation = endYear / 4;
            endYear = endYear + bornPopulation - diedPopulation;
            yearsPassed++;
        }
    }

    // TODO: Print number of years
    printf("Years: %i\n", yearsPassed);
}
