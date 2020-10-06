/*
 * We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
*/



fn main() {
    let mut i = 1;
    let mut curr_triangle_num = 1;
    let mut known_primes : Vec<i32> = Vec::new();

    loop {
        let divisors = find_divisors(curr_triangle_num, known_primes);

        println!("{0}, {1}\n", divisors, curr_triangle_num);
        if divisors > 500 {
            println!("{}", curr_triangle_num);
            break;
        }
        i += 1;
        curr_triangle_num += i;
    }
}

fn find_divisors(mut num : i32, mut known_primes : Vec<i32>) -> i32 {
    let mut prime_factors = Vec::new();
    prime_factors.push(1);
    prime_factors.push(num);

    while num > 1 {
        let smallest_prime : i32 = find_smallest_prime_factor(num, &mut known_primes);
        num /= smallest_prime;
        prime_factors.push(smallest_prime);
    }

    // should have the prime factorization here
    for i in prime_factors {
        println!("{}", i)
    }

    return 1;

}

/* Find the next smallest prime factor */
fn find_smallest_prime_factor(num : i32, known_primes : &mut Vec<i32>) -> i32 {
    for i in 2..num {
        if is_prime(i, &mut known_primes) {
            return i;
        }
    }

    num
}

/* Checks if a number is prime */
fn is_prime(num : i32, known_primes : &mut Vec<i32>) -> bool {
    if known_primes.contains(&num) {
        return true;
    }

    for i in 2..num {
        if num % i == 0 {
            return false;
        }
    }

    known_primes.push(num);
    true
}


// find prime factorization
// find all combinations of it and throw them into a set
// return the size of the set
