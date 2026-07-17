You are given a 2D grid grid:

'X' = infected plant
'.' = healthy plant
At the end of each day, every infected plant infects its up to 8 neighboring cells (including diagonals) that are healthy ('.'). Infection is synchronous by day: newly infected cells on the same day do not spread until the next day.

A “stable (balanced) state” is reached when a day ends with no new infections.

Return the number of days needed to reach the stable state starting from day 0.

Input
Line 1: integers R C
Next R lines: strings of length C consisting of X and .
Output
An integer: days to reach stability
Constraints
Assume reasonable bounds if not specified by the interviewer.

Example
Input:

3 4
X...
....
..X.
Output:

2


part2:
Updated grid:

'X' = infected plant
'.' = healthy plant
'I' = immune plant

Rules:

X infects up to 8 neighbors each day.
Only '.' can become infected.
'I' never gets infected.
'I' never spreads infection.
Stable state = a day ends with no new infections.
Return days to stable.


part3
'X' = infected
'.' = healthy

Every infected plant infects 8-neighbor healthy plants.
Each infected plant recovers back to '.' exactly D days after it became infected.
Recovered plants can be infected again later.
Stable = no more infections and no more recoveries will ever happen.

part4:
'X' infect
'.' health
'I' immnue
'D' death
with recovery threshold and deathy threshold

Beginning of Day

Current Grid

↓

Compute neighbor counts

↓

Schedule every death

↓

Apply deaths

↓

Apply recoveries

↓

Spread infections

↓

Next day