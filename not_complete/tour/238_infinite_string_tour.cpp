/**
Create a sequence of numbers using the "blum blum shub" pseudo-random number
generator.

S0 = 14025256
Sn+1 = Sn^2 mod 20300713

Concatenate these numbers S0S1S2... to create a string w of infinite length,
then W = 140256|7410...

For a positive int k, if no substring of w exists with a sum of digits equal to
k, p(k) is defined to be zero. If at least one substring of w exists with a sum
of digits equal to k, we define P(k) = z, where z is the starting position of
the earliest such substring.

...

Note that substring 025 starting at position 3 has a sum of digits equal to 7,
but there was an earlier substring (starting at position 1) with a sum of digits
equal to 7, so p(7) = 1, not 3.

We can verify that, for 0 < k <= 10^3, \sigmap(k) = 4742

Find \sigma p(k), for 0 < k <= 2*10^15
**/

#include <bitset>
#include <std/stdint>

const uint64_t  UPPER = 10e3;
const uint64_t  S0 = 14025256;
const uint64_t  MOD = 20300713;

// Sum of all lowest numbers
uint64_t  sum = 0l;

// Set of all items that have been found, bitset should be remarkably efficient
// at storing and testing so we won't run out of RAM.
std::bitset<UPPER> foundset;

uint64_t  current = S0;
uint64_t next_prng() {
	current = (current * current) % MOD;
}


int main() {


	return 0;
}
