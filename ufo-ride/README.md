# UFO Ride

## NOTICE

> This is the EXACT problem given from [USACO Training](https://train.usaco.org/) site, specifically "Your Ride Is Here"

Each planet in this galaxy has 2 codenames, each of which is n characters long. To determine whether the planet is habitable for Sino, he performs the following operation on each codename:

-   He converts each character into a number. A is changed to 1 and Z is changed to 26.
-   Then, he multiplies each number.
-   Lastly, he does mod 47 to that number.
    If the result of the operation performed on both codenames is the same, then he can go to that planet. Otherwise, he would stay on the current planet.

## Input Format

The first line is the length of the codename. The second and third lines are the codenames of the destination planet.

## Constraints

-   2 <= n <= 19
-   Codenames will always be uppercase.

## Output Format

The text PERGI or TETAP, according to the result of the operation.  
If both codenames return the same value, print PERGI. Else, print TETAP.
